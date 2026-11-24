"""One-star review of something essential.

Writes a single deadpan one-star review, at most 160 characters,
to /output/entry.txt. Pure standard library, deterministic.
"""

import os

REVIEW = (
    "One star. Gravity works perfectly until I am carrying "
    "something fragile, then it works even better."
)

# Deadpan, one line, one grievance: gravity never fails,
# it only ever fails at the worst possible moment.


def main():
    text = REVIEW.strip()
    assert 1 <= len(text) <= 160, "review must be 1-160 characters"
    assert "\n" not in text, "review must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
