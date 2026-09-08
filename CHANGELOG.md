# Changelog

## 1.14.0

Re-pinned to **Gen1WildUI 1.31.0**.

- **SEND is on the party half of the box screen.** Selecting a party member
  there offered STATS and CANCEL and nothing else. It makes the move the way
  the screen already makes it every time the cursor lifts a POKéMON out of the
  party — the same last-POKéMON refusal, the mail behind it moved up with it
  on Crystal, and back into the row it came from if the shared box turns it
  away. It confirms first, because out of the party is a POKéMON leaving your
  team rather than a move between pages.

## 1.13.0

Re-pinned to **Gen1WildUI 1.30.2**.

- **Moving several POKéMON out of the GLOBAL BOX took the wrong ones**, then
  said "That can't be sent." A mark records where a POKéMON is, which is
  enough in a cartridge box — those keep their arrangement, so taking one out
  leaves every other cell where it was. The GLOBAL BOX is a **queue**: a
  withdrawal closes it up and every cell after the gap moves down one. Mark
  ONE and TWO and you moved ONE and THREE. Marks on a global page carry the
  POKéMON's id now, and every take resolves it to where that POKéMON is at the
  moment of the take.

## 1.12.0

Re-pinned to **Gen1WildUI 1.30.1**.

- **The caught marker and the EXP bar under DARK, for real this time.** The
  last fix stopped the theme *painting* the one-pixel ring and left it *zoning*
  one: every marked rectangle was grown by a pixel on each side and painted
  through a palette whose both ends are black, which on Red's white HUD panel
  is a black pixel all the way round. Same ring, drawn by the palette instead
  of the brush. Art a mod painted itself is now zoned as exactly the rectangle
  it painted, so the POKéBALL keeps its corners and the blue bar has no box
  round it.

## 1.11.0

Re-pinned to **Gen1WildUI 1.30.0**.

- **Anything drawn over a POKéMON in the box came back inverted.** A popup
  over the grid came back with white blocks punched through it, in a grid,
  exactly the size and position of the cells underneath. A true-colour mark
  claims a rectangle to be re-blitted raw at composite time, and by then the
  popup is drawn over part of it. An icon a menu is covering does not claim
  true colour any more.

- **SELECT marks, and A moves everything marked.** Mark six in one box, walk
  to another, press A. The marks survive a box change; B clears them; a box
  with room for some but not all of them takes none and says so.

- **SORT moved from SELECT into the popup START opens**, beside the other
  verbs, with UNDO — which is what freed SELECT.

- **SEND is on the box popup too**, not only the party menu's, and it is the
  box's own move rather than the party's.

## 1.10.1

Re-pinned to **Gen1WildUI 1.29.1** and **Gen1WildQOL 1.32.2**.

- **The caught marker and the EXP bar under DARK.** The theme rings every
  true-colour mark to hide the seam where art it did not draw meets a shaded
  page. Neither of these has a seam — both are flat colour a mod painted
  itself — so the ring was filling the POKéBALL's corners in and drawing a
  black box round the blue bar. Both mark flat now. A level-up also stopped
  taking the rest of the frame's colour with it: the EXP burst was marking
  192 rectangles a frame against a cap of forty, and is three per particle now.

## 1.10.0

Re-pinned to **Gen1WildUI 1.29.0**.

- **The GLOBAL BOX holds both generations now.** Each POKéMON keeps the shape
  the game that sent it had it in, so a deposit converts nothing and nothing is
  ever loaded — a Johto POKéMON goes in from a Gen 2 game and comes back out of
  it unchanged. What a Gen 1 game will take out is still the Time Capsule’s
  rule, asked when it takes it. Also: a refusal that ran off the right edge of
  Gold’s message box now turns the page.

## 1.9.2

Re-pinned to **Gen1WildUI 1.28.2**.

- **The GLOBAL BOX is the box mod's feature, not this cartridge's.** It reads
  every save on your installation, plain playthroughs included — so a POKéMON
  can go between this and any other game that has the mod, not just between
  the Wild cartridges. Two refusal lines fixed with it: one named the wrong
  game to import, and one ran off the end of the text box.

## 1.9.1

Re-pinned to **Gen1WildUI 1.28.1**.

- **A POKéMON sent from Wild Green is in the GLOBAL BOX here.** It wasn't: the
  other cartridge's outbox was invisible, so the box read empty on every save
  but the one you were in. The bundle files each vendored mod's save data
  under a prefixed key, and the box was looking for the unprefixed one when it
  read another save. It goes by the shape of what it finds now, not the name.

## 1.9.0

Re-pinned to **Gen1WildUI 1.28.0**.

- **The GLOBAL BOX.** Past BOX 14 the box header keeps going: **GLOBAL 1**,
  and another page every time the last one fills. It is one box shared with
  every other save on your installation — so the POKéMON you sent from Wild
  Green are sitting there waiting, and anything you send from here is waiting
  on Wild Green. There is a **SEND** row on a POKéMON's own popup in the party
  menu too.

  It lives **inside the saves**, so it syncs, backs up and rolls back with
  them. What may live in it is the **Time Capsule's** rule, reused rather than
  restated: a Johto POKéMON, one holding MAIL, an EGG, or one that knows a
  move RED never heard of is refused, with the reason. Crystal converts on the
  way in and on the way out.

## 1.8.0

Re-pinned to **Gen1WildQOL 1.32.1**.

- **Under DARK, the caught marker is a POKéBALL again — and the EXP bar comes
  back with it.** The ball was reporting one true-colour mark per *pixel*: 37
  of them for a 7x7 icon. DARK draws a one-pixel skirt round every mark, which
  filled the ball's transparent corners in and made it a blob — and 37 rects
  emptied the frame's 40-rect budget, so the EXP bar's single mark fell off the
  end and lost the zone that themes it. One icon, both symptoms.

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
