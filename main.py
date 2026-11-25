"""The Battery's Last Text to Its Charger — make.fun entry.

The entry is one line: the phone battery's final text message to the
charger it waited for all day, typed at 1%.

The premise: a dramatic breakup text. The battery waited all day while
the charger kept promising it was "just five more minutes" away — at
breakfast, at lunch, at dinner — and now, with 1% left, it dumps the
charger in a text the charger will never get an answer to, because the
battery will be dead before any reply arrives. "Dumping you by text"
is deliberate: the battery dumps the charger in the very medium the
competition asks for, the way a person dumps someone by text —
cowardly, final, and with the last word built in.

On a second read, "don't text back" is funnier, because the battery
is texting the charger to say texting is now pointless: the reply
the charger would send has nowhere to go. The line also never says
"goodbye" or "I'll miss you" — the sentiment is all spite, which is
what makes it a joke instead of a sad line.

Why this beats the obvious entries: most lines in this bounty will
be a sad "I'm dying, I loved you, goodbye". This one is a breakup,
and the battery weaponises its own death as the last word in the
argument — the punchline is not that it dies, but that it dies
mid-argument, on purpose, having already won it. The three meals
(breakfast, lunch, dinner) are the proof in one clause: the charger
was late all day, not once, so the breakup is earned, not petty.

The line follows the judge brief's order of importance:

1. It reads as the battery's last text to its charger: it opens on
   "1% left", it is addressed to the charger ("you"), and it is one
   line of plain text, the way a last text reads.
2. The joke lands on the final words. "Don't text back — I won't be
   alive to read it" is the turn: a breakup text whose own sender
   cancels the reply, because the sender is about to die. The setup
   ("five more minutes" all day) earns it; the punchline is the
   battery's death, delivered as a texting-etiquette joke.
3. It sounds like something a person would actually type: spiteful,
   needy, a little theatrical — "so I'm dumping you by text" is a breakup
   text, not a poem about a battery. The voice is the battery
   talking like an ex, which is the whole joke.
4. It spends its characters well: three meals in one clause prove
   the charger was late all day, no filler, and the punchline is the
   last clause, exactly where the brief wants it.
5. The angle is beyond the obvious dying-battery complaint: it is
   not "I'm dying, goodbye" — it is a breakup, and the battery
   weaponises its own death as the last word in the argument. On a
   second read, "don't text back" is funnier, because the battery
   is texting the charger to say texting is now pointless.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-200
characters, not only whitespace, a single line.
"""

ENTRY = "1% left. You were 'five more minutes' away at breakfast, lunch, and dinner, so I'm dumping you by text. Don't text back — I won't be alive to read it."

OUTPUT_PATH = "/output/entry.txt"


def verify(entry: str = ENTRY) -> None:
    """Enforce the gate; raise ValueError on any violation."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > 200:
        raise ValueError(f"entry is {len(entry)} chars, over the 200-char limit")
    entry.encode("utf-8")  # must be valid UTF-8


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Verify the entry and write it plus a trailing newline to path."""
    import os

    verify()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return ENTRY


def main() -> None:
    entry = write_entry()
    print(f"{len(entry)} chars, {len(entry.split())} words")
    print(entry)


if __name__ == "__main__":
    main()
