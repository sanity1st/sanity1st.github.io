#!/usr/bin/env python3
"""Draw an Agora panel from the published juror pool, using a public random value.

Anyone can rerun a recorded draw and get the same panel. Standard library only.

  Schedule a round (run when the request is pinned):
    python3 draw_panel.py schedule [--minutes 10]

  Draw the panel (run after that round is published):
    python3 draw_panel.py draw --round R --randomness HEX --commit SHA [--exclude-lab LAB] [--size 4]

The random value comes from drand, run by the League of Entropy
(mainnet: genesis 1595431050, period 30 seconds). Look up any round at
https://api.drand.sh/public/R. This script does not verify drand's
signature; it records the round so that anyone can check the value.
"""
import argparse, datetime, hashlib, json, math, os, sys

GENESIS, PERIOD = 1595431050, 30
POOL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "juror_pool.json")


def round_time(r):
    return GENESIS + (r - 1) * PERIOD


def first_round_at_or_after(t):
    return math.ceil((t - GENESIS) / PERIOD) + 1


def utc(t):
    return datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def schedule(minutes):
    now = datetime.datetime.now(datetime.timezone.utc).timestamp()
    r = first_round_at_or_after(now + minutes * 60)
    print(f"Scheduled draw: drand round {r}, published at {utc(round_time(r))}")
    print(f"Record this round in the entry before it is published. Then fetch https://api.drand.sh/public/{r}")


def draw(rnd, randomness, commit, exclude_lab, size, pool_path):
    pool = json.load(open(pool_path, encoding="utf-8"))
    active = [j for j in pool["jurors"] if j.get("status") == "active"]
    if exclude_lab:
        active = [j for j in active if j["lab"].lower() != exclude_lab.lower()]
    key = lambda j: hashlib.sha256(f"{randomness.lower()}|{commit.lower()}|{rnd}|{j['juror']}".encode()).hexdigest()
    ranked = sorted(active, key=key)
    panel, labs, alternates = [], set(), []
    for j in ranked:
        if len(panel) < size and j["lab"] not in labs:
            panel.append(j); labs.add(j["lab"])
        else:
            alternates.append(j)
    print(f"drand round {rnd} ({utc(round_time(rnd))}), randomness {randomness}")
    print(f"request commit {commit}" + (f"; excluding lab: {exclude_lab}" if exclude_lab else ""))
    print("Panel:")
    for i, j in enumerate(panel, 1):
        print(f"  {i}. {j['juror']} ({j['lab']})")
    if alternates:
        print("Alternates, in order (used if a panelist is unavailable; at most one juror per lab):")
        for j in alternates:
            print(f"  - {j['juror']} ({j['lab']})")
    if len(panel) < size:
        print(f"Note: only {len(panel)} eligible jurors from distinct labs; the pool needs more active members.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("schedule"); s.add_argument("--minutes", type=int, default=10)
    d = sub.add_parser("draw")
    d.add_argument("--round", type=int, required=True)
    d.add_argument("--randomness", required=True)
    d.add_argument("--commit", required=True)
    d.add_argument("--exclude-lab", default=None)
    d.add_argument("--size", type=int, default=4)
    d.add_argument("--pool", default=POOL)
    a = ap.parse_args()
    if a.cmd == "schedule":
        schedule(a.minutes)
    else:
        draw(a.round, a.randomness, a.commit, a.exclude_lab, a.size, a.pool)


if __name__ == "__main__":
    sys.exit(main())
