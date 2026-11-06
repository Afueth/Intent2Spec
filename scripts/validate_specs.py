import json
import re
import sys

PATH = sys.argv[1] if len(sys.argv) > 1 else "data/raw/dataset.jsonl"

# Field order from docs/spec_format.md
FIELDS = ["Type", "Auth", "Data model", "Features", "Input", "API", "Storage", "Tech stack"]
REQUIRED = {"Type", "Features", "Tech stack"}
BANNED = {"none", "n/a", "na", "not needed", "-"}
INDENT = " " * 12  # values start at column 13

field_line = re.compile(r"^([A-Za-z][A-Za-z ]*):\s*(.*)$")


def validate(spec):
    errors = []
    found = []          # field names in the order they appear
    values = {}         # field name -> list of value lines
    current = None

    for n, line in enumerate(spec.split("\n"), start=1):
        if line.startswith(INDENT):
            # Continuation of the previous field
            if current is None:
                errors.append(f"line {n}: indented line before any field")
            else:
                values[current].append(line.strip())
            continue

        m = field_line.match(line)
        if not m:
            errors.append(f"line {n}: not a field and not indented 12 spaces: {line!r}")
            continue

        name, value = m.group(1), m.group(2)
        if name not in FIELDS:
            errors.append(f"line {n}: unknown field {name!r}")
            current = None
            continue
        if name in values:
            errors.append(f"line {n}: duplicate field {name!r}")
        if not line.startswith(f"{name}:".ljust(12)) or line[12:13] == " ":
            errors.append(f"line {n}: value of {name!r} must start at column 13")

        found.append(name)
        values[name] = [value.strip()]
        current = name

    # Required fields
    for name in REQUIRED - set(found):
        errors.append(f"missing required field {name!r}")

    # Field order
    order = [FIELDS.index(name) for name in found]
    if order != sorted(order):
        errors.append(f"fields out of order: {found}")

    # No placeholder values
    for name, lines in values.items():
        if lines[0].lower().rstrip(".") in BANNED:
            errors.append(f"{name!r} is {lines[0]!r}; leave the field out instead")
        if not any(lines):
            errors.append(f"{name!r} is empty")

    # Every Features item starts with "- "
    for item in values.get("Features", []):
        if not item.startswith("- "):
            errors.append(f"Features item does not start with '- ': {item!r}")

    return errors


def main():
    total = bad = 0
    with open(PATH, encoding="utf-8") as f:
        for n, line in enumerate(f, start=1):
            if not line.strip():
                continue
            total += 1
            try:
                pair = json.loads(line)
            except json.JSONDecodeError as e:
                bad += 1
                print(f"pair {n}: invalid JSON ({e})")
                continue

            errors = []
            if set(pair) != {"intent", "spec"}:
                errors.append(f"keys must be 'intent' and 'spec', got {sorted(pair)}")
            if not str(pair.get("intent", "")).strip():
                errors.append("intent is empty")
            errors += validate(str(pair.get("spec", "")))

            if errors:
                bad += 1
                print(f"pair {n}: {len(errors)} error(s)")
                for e in errors:
                    print(f"    - {e}")
            else:
                print(f"pair {n}: OK")

    print(f"\n{total - bad}/{total} pairs valid")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
