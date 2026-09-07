#!/usr/bin/env python3
"""Check the things that can quietly drift apart in this cart.

    python3 tools/check.py [--online]

Three of them:

  * `cart.json` is what the ENGINE will accept.  Parsed through the same
    grammar `src/carts/CartManifest.lua` applies -- the shell is #RRGGBB,
    the finish is one the launcher can render, the base is a game it
    knows, every pinned mod carries a digest, and `load_order` names
    exactly the mods that are pinned.  A cart that only looks right in a
    diff is a cart the launcher rejects on import.
  * `label.png` is what `tools/make_label.py` draws from
    `art/wild_crystal_label.png`.  A committed PNG the tool no longer
    produces is a picture nobody can regenerate -- and the Gen1Wild index
    serves this same file as the cart's card thumbnail, so it is the
    listing too.
  * every pinned mod's digest matches the release it names.  A pin is a
    promise that two people running this cart are running the same game;
    a digest that has drifted from its release quietly breaks that, and
    the seal is what makes it matter.

The digest check needs the network, so `--online` asks for it and a bare
run says it was skipped rather than pretending it passed.  CI passes
`--online`.

Wild Green's copy of this file also compared `tools/palette.py` against
Gen1MakeItGreen's.  There is no such twin here: this cart pins no mod that
owns a palette, and its shell is taken from the label art rather than
derived from one.  A check that cannot fail is worse than no check, so it
is not carried over.

Exits non-zero on any finding, which is what CI wants.
"""

import hashlib
import json
import pathlib
import subprocess
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
CART = ROOT / "cart.json"

FINISHES = {"sparkle", "holo", "sparkle+holo"}
BASES = {"red", "blue", "yellow", "gold", "silver", "crystal"}

problems = []


def fail(where, message):
    problems.append("%s: %s" % (where, message))


def check_manifest(cart):
    shell = str(cart.get("shell", ""))
    if not (len(shell) == 7 and shell[0] == "#"
            and all(c in "0123456789abcdef" for c in shell[1:])):
        fail("cart.json", "shell must be a lowercase #rrggbb colour, got %r"
             % shell)
    finish = cart.get("finish")
    if finish is not None and finish not in FINISHES:
        fail("cart.json", "finish must be one of %s, got %r"
             % (", ".join(sorted(FINISHES)), finish))
    if cart.get("base") not in BASES:
        fail("cart.json", "base must be a game the engine knows, got %r"
             % cart.get("base"))
    if not (ROOT / str(cart.get("label", ""))).is_file():
        fail("cart.json", "label names %r, which is not in the repository"
             % cart.get("label"))

    pinned = [m.get("id") for m in cart.get("mods") or []]
    for mod in cart.get("mods") or []:
        digest = str(mod.get("sha256", ""))
        if len(digest) != 64 or not all(c in "0123456789abcdef" for c in digest):
            fail("cart.json", "%s has no usable sha256" % mod.get("id"))
        if not mod.get("version"):
            fail("cart.json", "%s is pinned to no version" % mod.get("id"))
    order = cart.get("load_order") or []
    if sorted(order) != sorted(pinned):
        fail("cart.json", "load_order is %s but the cart pins %s -- a mod in "
             "one and not the other either never loads or has no rules"
             % (order, pinned))
    return pinned


def check_label():
    before = (ROOT / "label.png").read_bytes()
    subprocess.run([sys.executable, str(ROOT / "tools" / "make_label.py")],
                   check=True, capture_output=True)
    after = (ROOT / "label.png").read_bytes()
    if before != after:
        fail("label.png", "does not match what make_label.py draws from the "
             "art; run python3 tools/make_label.py and commit it")


def check_digests(cart, online):
    if not online:
        print("check: --online not given, so the pins are not fetched")
        return
    for mod in cart.get("mods") or []:
        url = ("https://github.com/%s/releases/download/v%s/%s-%s.zip"
               % (mod["repo"], mod["version"], mod["id"], mod["version"]))
        try:
            with urllib.request.urlopen(url, timeout=60) as response:
                body = response.read()
        except Exception as error:                       # pragma: no cover
            fail(mod["id"], "could not fetch %s (%s)" % (url, error))
            continue
        got = hashlib.sha256(body).hexdigest()
        if got != mod["sha256"]:
            fail(mod["id"], "pinned %s but %s is %s"
                 % (mod["sha256"], url, got))


def main(argv):
    online = "--online" in argv[1:]
    for arg in argv[1:]:
        if arg != "--online":
            raise SystemExit("usage: check.py [--online]")
    cart = json.loads(CART.read_text(encoding="utf-8"))
    pinned = check_manifest(cart)
    check_label()
    check_digests(cart, online)
    if problems:
        for line in problems:
            print("error: %s" % line)
        print("\n%d problem(s)." % len(problems))
        return 1
    print("check: cart.json is well formed, label.png is current, "
          "%d mod(s) pinned" % len(pinned))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
