import math
import unittest

import torch

from model.gpt import GPT, CausalSelfAttention, GPTConfig

# A tiny model so the tests run fast
SMALL = GPTConfig(vocab_size=50, context_len=32, n_layers=2, n_heads=2, d_embed=32, dropout=0.0)


class TestGPT(unittest.TestCase):
    def setUp(self):
        torch.manual_seed(0)

    def test_output_shapes(self):
        model = GPT(SMALL)
        x = torch.randint(0, 50, (3, 10))
        logits, loss = model(x)
        self.assertEqual(logits.shape, (3, 10, 50))
        self.assertIsNone(loss)  # no targets -> no loss

    def test_full_size_parameter_count(self):
        model = GPT(GPTConfig())
        self.assertEqual(sum(p.numel() for p in model.parameters()), 11_998_080)

    def test_weight_tying(self):
        model = GPT(SMALL)
        self.assertIs(model.head.weight, model.emb.tok.weight)

    def test_initial_loss_near_random_guessing(self):
        model = GPT(SMALL)
        x = torch.randint(0, 50, (4, 20))
        y = torch.randint(0, 50, (4, 20))
        _, loss = model(x, y)
        self.assertAlmostEqual(loss.item(), math.log(50), delta=0.3)

    def test_ignored_targets_do_not_change_loss(self):
        model = GPT(SMALL).eval()
        x = torch.randint(0, 50, (1, 10))
        y = torch.randint(0, 50, (1, 10))
        y_masked = y.clone()
        y_masked[0, :5] = -100
        _, loss_part = model(x, y_masked)
        logits, _ = model(x)
        expected = torch.nn.functional.cross_entropy(logits[0, 5:], y[0, 5:])
        self.assertAlmostEqual(loss_part.item(), expected.item(), places=5)

    def test_attention_is_causal(self):
        attn = CausalSelfAttention(SMALL).eval()
        x = torch.randn(1, 8, 32)
        x2 = x.clone()
        x2[0, 5:] = 0  # change only the future
        self.assertTrue(torch.allclose(attn(x)[0, :5], attn(x2)[0, :5]))

    def test_model_is_causal(self):
        model = GPT(SMALL).eval()
        a = torch.randint(0, 50, (1, 12))
        b = a.clone()
        b[0, 8:] = 7
        la, _ = model(a)
        lb, _ = model(b)
        self.assertTrue(torch.allclose(la[0, :8], lb[0, :8], atol=1e-5))

    def test_backward_reaches_every_parameter(self):
        model = GPT(SMALL)
        x = torch.randint(0, 50, (2, 10))
        y = torch.randint(0, 50, (2, 10))
        _, loss = model(x, y)
        loss.backward()
        for name, p in model.named_parameters():
            self.assertIsNotNone(p.grad, f"no gradient for {name}")

    def test_can_memorise_one_batch(self):
        model = GPT(SMALL)
        opt = torch.optim.AdamW(model.parameters(), lr=1e-2)
        x = torch.randint(0, 50, (2, 16))
        y = torch.randint(0, 50, (2, 16))
        _, first = model(x, y)
        for _ in range(100):
            _, loss = model(x, y)
            opt.zero_grad()
            loss.backward()
            opt.step()
        self.assertLess(loss.item(), first.item() * 0.2)


if __name__ == "__main__":
    unittest.main()
