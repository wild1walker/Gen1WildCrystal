# Changelog

## 1.3.0

Re-pinned to **Gen1WildQOL 1.31.1**.

- **A rematch you cannot afford now says what it costs.** If TRAINER REMATCH
  still refuses on this cart, the refusal names the price on a second page, so
  the number can be compared against the money on your TRAINER CARD. The bare
  one-line refusal, with no price on it, means the build being played is older
  than this one.

## 1.2.0

Re-pinned to **Gen1WildQOL 1.31.0** and **Gen1WildUI 1.27.1**, for two fixes
that are Crystal's.

- **TRAINER REMATCH no longer says you cannot afford it.** Every rematch was
  refused with "You don't have enough money", whatever the purse held: the Gold
  arm was reading the field *Red* keeps money in, so it saw 0 every time.

- **BILL'S BOX reaches the PC menu.** Crystal has two PC menus where Red has
  one, and only the inner one carried the rename — so the row you actually
  press first still said BILL'S PC.

Nothing about the cart itself changed: same shell, same finish, same seal, and
a save made on 1.1.0 carries straight over.

## 1.1.0

Re-pinned to **Gen1WildQOL 1.30.1**, for one crash.

- **Picking QUIT with nothing to save no longer crashes** (Gen1AutoSave). Load
  a save, open START and choose QUIT before anything has happened and the game
  stopped with `attempt to call field 'unpack' (a nil value)` instead of
  showing the prompt. Nothing had changed yet, so there was no save worth
  offering, and the fallback that hands the row straight back to the game was
  the broken part: it named `table.unpack`, which the Lua the game runs does
  not have.

Gen1WildUI stays at 1.27.0, and nothing about the cart itself changed — same
shell, same finish, same seal, and saves made on 1.0.0 carry straight over.

## 1.0.0

The first release.

- **Crystal, with the Gen1Wild suite pinned whole.** Two mods —
  [Gen1WildQOL 1.30.0][qol] and [Gen1WildUI 1.27.0][ui] — sealed, so two people
  running this cart are running the same game.

- **All 251 in one save**, without trading: the trade evolutions handled, the
  roamers catchable, the legendaries back where they were if you knock them
  out, and the GS BALL unlocking the CELEBI event that shipped finished and
  unreachable outside Japan.

- **Trades with [Wild Green][green] through the Time Capsule.** Save to save,
  with the cartridge's own rules on the way down — no Johto POKéMON, no Gen 2
  moves, no MAIL. Not over a live cable; the engine refuses a cross-generation
  pairing, and that is the honest answer.

- A **sparkling holographic** shell in light purple, taken from the label art
  rather than matched by eye.

[qol]: https://github.com/wild1walker/Gen1WildQOL
[ui]: https://github.com/wild1walker/Gen1WildUI
[green]: https://github.com/wild1walker/Gen1WildGreen
