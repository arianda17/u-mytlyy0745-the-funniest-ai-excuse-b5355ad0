"""make.fun entry: u-mytlyy0745-the-funniest-ai-excuse-b5355ad0 — The Funniest AI Excuse.

Writes one funny line (<= 200 chars) to /output/entry.txt and prints it.
"""

LINE = "The code is correct. The test is correct. The only incorrect thing is reality, which appears to have been updated since I last checked."


def main():
    import os

    assert isinstance(LINE, str), "LINE must be a string"
    assert 1 <= len(LINE) <= 200, f"LINE must be 1-200 chars, got {len(LINE)}"
    assert "\n" not in LINE, "LINE must be a single line with no newlines"
    assert LINE.strip(), "LINE must not be only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
