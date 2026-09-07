# Changelog

## 1.7.0

Re-pinned to **Gen1WildUI 1.27.4**.

- **The box walks its POKéMON at the same speed the party list does.** The last
  release fixed *which* frames the walk uses; this is how fast it plays them.
  The box was running the icon clock at double rate — a number borrowed from
  Red's box, whose animation is a mirror rather than a walk.

## 1.6.0

Re-pinned to **Gen1WildUI 1.27.3**.

- **POKéMON in the box and the party walk south again** instead of turning to
  face you and away on the spot. The follower sheets hold six frames — south,
  north and side, standing and stepping — and the icon path was alternating the
  first two of them, which are the front and the back. Red has always stepped
  to the south walk frame on a tall sheet; Gold does now too.

## 1.5.0

Re-pinned to **Gen1WildQOL 1.32.0**. Both changes are TRAINER REMATCH's, and
both change what happens in a fight.

- **A rematch costs half of what winning pays**, which is four times what it
  was quoting. Crystal pays a trainer's reward in four quarters where Red pays
  it once, and this arm had been copying Red's arithmetic — so the stake was an
  eighth of the purse, not half.

- **MATCH LEVELS now reaches the battle.** It was scaling the *quote* but not
  the opponent: the levels moved, but their moves stayed the ones they knew at
  their original level and a trainer scaled up came in already damaged. A
  matched trainer is now the same opponent Red's is — right stats, right moves,
  full HP.

## 1.4.0

Re-pinned to **Gen1WildUI 1.27.2**.

- **"NOTHING LIVES HERE" no longer runs through the box border** on a POKéDEX
  AREA place with nothing in it.

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
