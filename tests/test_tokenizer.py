import json
import unittest

from tokenizer.bpe import BPETokenizer, get_stats, merge

TOKENIZER_PATH = "tokenizer/bpe_3000.json"
DATA_FILES = ["data/raw/train.jsonl", "data/raw/val.jsonl", "data/evaluation/test.jsonl"]


def load_pairs(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


class TestHelpers(unittest.TestCase):
    def test_get_stats(self):
        self.assertEqual(get_stats([1, 2, 3, 1, 2]), {(1, 2): 2, (2, 3): 1, (3, 1): 1})

    def test_merge(self):
        self.assertEqual(merge([1, 2, 3, 1, 2], (1, 2), 99), [99, 3, 99])

    def test_merge_does_not_overlap(self):
        self.assertEqual(merge([5, 5, 5], (5, 5), 9), [9, 5])


class TestTokenizer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tok = BPETokenizer.load(TOKENIZER_PATH)

    def test_vocab_size(self):
        self.assertEqual(len(self.tok), 3005)

    def test_special_tokens(self):
        for name in ["<pad>", "<bos>", "<eos>", "<intent>", "<spec>"]:
            self.assertIn(name, self.tok.special)
            self.assertEqual(self.tok.decode([self.tok.special[name]]), name)

    def test_round_trip_edge_cases(self):
        for text in ["", "a", "   ", "hello\n\nworld", "café ☕ 😀", "wnat teh app", "<eos> typed by a user"]:
            self.assertEqual(self.tok.decode(self.tok.encode(text)), text)

    def test_user_text_never_becomes_special(self):
        ids = self.tok.encode("<eos>")
        self.assertNotIn(self.tok.special["<eos>"], ids)

    def test_round_trip_all_data(self):
        for path in DATA_FILES:
            for pair in load_pairs(path):
                for key in ("intent", "spec"):
                    self.assertEqual(self.tok.decode(self.tok.encode(pair[key])), pair[key])

    def test_encode_pair_format(self):
        sp = self.tok.special
        ids = self.tok.encode_pair("an app", "Type:       App")
        self.assertEqual(ids[:2], [sp["<bos>"], sp["<intent>"]])
        self.assertEqual(ids[-1], sp["<eos>"])
        self.assertEqual(ids.count(sp["<spec>"]), 1)

    def test_prompt_ends_with_spec(self):
        ids = self.tok.encode_pair("an app")
        self.assertEqual(ids[-1], self.tok.special["<spec>"])
        self.assertNotIn(self.tok.special["<eos>"], ids)

    def test_save_load_gives_same_ids(self):
        import os
        import tempfile
        path = os.path.join(tempfile.mkdtemp(), "tok.json")
        self.tok.save(path)
        loaded = BPETokenizer.load(path)
        text = "Type:       Web application"
        self.assertEqual(loaded.encode(text), self.tok.encode(text))


if __name__ == "__main__":
    unittest.main()
