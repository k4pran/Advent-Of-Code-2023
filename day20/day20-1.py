from collections import deque


def parse_configs(lines):

    broadcaster = []
    ffs = dict()
    cons = dict()
    for line in lines:
        if line.startswith("broadcaster"):
            broadcaster = line.split("->")[-1].replace(" ", "").split(",")
        elif line.startswith("%"):
            name, dest = line[1:].strip().split("->")
            ffs[name.strip()] = [0, dest.replace(" ", "").split(",")]
        elif line.startswith("&"):
            name, dest = line[1:].replace(" ", "").split("->")
            cons[name.strip()] = (dict(), dest.replace(" ", "").split(","))

    # find con inputs from ffs
    for con_k, con_v in cons.items():
        for ff_k, ff_v in ffs.items():
            if con_k in ff_v[1]:
                cons[con_k][0][ff_k] = 0

    # find con inputs from other cons
    for con_k, con_v in cons.items():
        for con_2_k, con_2_v in cons.items():
            if con_k in con_2_v[1]:
                cons[con_k][0][con_2_k] = 0

    return broadcaster, ffs, cons



def perform_flip_flop(mod, ffs, pulse):
    if pulse == 1:
        return []
    ffs[mod][0] = 1 if ffs[mod][0] == 0 else 0
    new_pulse = ffs[mod][0]

    mods = []
    for new_mod in ffs[mod][1]:
        mods.append((new_pulse, mod, new_mod))
    return mods


def perform_con(inp, mod, cons, pulse):
    cons[mod][0][inp] = pulse
    sending_pulse = 0 if all(c == 1 for c in cons[mod][0].values()) else 1

    mods = []
    for new_mod in cons[mod][1]:
        mods.append((sending_pulse, mod, new_mod))
    return mods


def is_complete(cons, ffs):
    for ff in ffs.values():
        if ff[0] == 1:
            return False
    for con in cons.values():
        for m in con[0].values():
            if m == 1:
                return False
    return True


def push_button(broadcaster, ffs, cons, nb_pushes=1000):

    low_pulses = 0
    high_pulses = 0
    for _ in range(nb_pushes):
        q = deque()
        low_pulses += 1
        for mod in broadcaster:
            q.append((0, "broadcaster", mod))
            low_pulses += 1

        print(f"button -> 0 -> broadcaster")
        while True:
            if len(q) == 0:
                break
            pulse, inp, mod = q.popleft()
            print(f"{inp} -> {pulse} -> {mod}")

            if mod in ffs:
                for n_mod in perform_flip_flop(mod, ffs, pulse):
                    q.append(n_mod)
                    if n_mod[0] == 0:
                        low_pulses += 1
                    else:
                        high_pulses += 1
            elif mod in cons:
                for n_mod in perform_con(inp, mod, cons, pulse):
                    q.append(n_mod)
                    if n_mod[0] == 0:
                        low_pulses += 1
                    else:
                        high_pulses += 1

            if is_complete(cons, ffs):
                break
    print(f"LOW PULSES = {low_pulses}")
    print(f"HIGH PULSES = {high_pulses}")
    return low_pulses * high_pulses


def solve(lines):
    broadcaster, ffs, cons = parse_configs(lines)
    return push_button(broadcaster, ffs, cons)


with open("day20.txt", 'r') as f:
    lines = f.read().splitlines()

    total = solve(lines)

    print(f"Day 20-1: {total}")
