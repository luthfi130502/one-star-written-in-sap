#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing the human who owns it, to /output/entry.txt.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The review itself: one line, one star, one very patient plant.
REVIEW = (
    "One star. Bought me for being 'impossible to kill,' then set out to "
    "test the claim: nine days on one teaspoon of water, a windowsill "
    "facing a brick wall, and my pot still wears its price sticker. "
    "Sir, I am not hardy. I am evidence."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
