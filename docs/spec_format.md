# Spec Format

Every spec in the dataset, and every spec the model generates, must follow these rules.

---

## Fields

Fields always appear in this order:

| # | Field | Required? | What it contains |
|---|-------|-----------|------------------|
| 1 | `Type` | required | Kind of project, e.g. `Web application (CRUD)`, `Mobile application`, `Command-line script (automation)` |
| 2 | `Auth` | optional | How users sign up and log in |
| 3 | `Data model` | optional | Stored entities, one per line: `Name(field, field, other_id -> Other)` |
| 4 | `Features` | required | What the project does, as a bullet list |
| 5 | `Input` | optional | What the program takes in (mainly for scripts) |
| 6 | `API` | optional | API style, then one endpoint per line: `METHOD /path` |
| 7 | `Storage` | optional | Where data is saved |
| 8 | `Tech stack` | required | Suggested languages, frameworks and libraries |

---

## Rules

1. **Leave out fields that don't apply.** Never write `None`, `N/A` or `not needed`.
2. **Keep the field order** from the table above, even when some fields are missing.
3. **Write field names exactly** as shown, followed by a colon: `Data model:`, not `Data Model:` or `Models:`.
4. **Align values.** Values start at column 13 (field name, colon, then spaces). Extra lines of the same field are indented to the same column.
5. **Each `Features` item** is a line starting with `- ` and a verb, e.g. `- Create`, `- Show`, `- Send`.
6. **Always include `Tech stack`.** If the user names tools, use them; otherwise suggest a common choice.
7. **No text before or after** the spec: no greetings, notes or explanations.

---

## Example

**Intent:**
something that renames all the photos in a folder by the date they were taken

**Spec:**
```
Type:       Command-line script (automation)
Features:   - Scan a folder for image files (.jpg, .jpeg, .png, .heic)
            - Read the "date taken" from each photo's EXIF metadata
            - Rename each file to YYYY-MM-DD_HHMMSS.ext
            - Add a number suffix when two photos share the same timestamp
            - Skip files with no EXIF date and report them
Input:      Path to a folder of image files
Tech stack: Python, Pillow (EXIF reading)
```

More examples: `data/raw/draft_examples.md`.
