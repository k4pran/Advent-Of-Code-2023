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


cache = set()

def perform_con(inp, mod, cons, pulse, press_nb):
    global cache
    cons[mod][0][inp] = pulse
    sending_pulse = 0 if all(c == 1 for c in cons[mod][0].values()) else 1

    mods = []
    if mod == "th":
        if str(cons[mod][0]) not in cache:
            print(press_nb)
            cache.add(str(cons[mod][0]))
            # manual console calc o_O using LCM:
            # 3739 * 3793 * 3923 * 4027
            # 224046542165867
        # print(inp + " -- " + "".join(cons[mod][0].values()))
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


def push_button(broadcaster, ffs, cons):

    presses = 0
    while True:
        presses += 1
        q = deque()
        for mod in broadcaster:
            q.append((0, "broadcaster", mod))

        # print(f"button -> 0 -> broadcaster")
        while True:
            if len(q) == 0:
                break
            pulse, inp, mod = q.popleft()
            # print(f"{inp} -> {pulse} -> {mod}")

            if mod in ffs:
                for n_mod in perform_flip_flop(mod, ffs, pulse):
                    q.append(n_mod)
            elif mod in cons:
                for n_mod in perform_con(inp, mod, cons, pulse, presses):
                    if n_mod == "rx" and n_mod[1] == 1:
                        return presses
                    q.append(n_mod)

            if is_complete(cons, ffs):
                break

def solve(lines):
    broadcaster, ffs, cons = parse_configs(lines)
    return push_button(broadcaster, ffs, cons)


with open("day20.txt", 'r') as f:
    lines = f.read().splitlines()

    total = solve(lines)

    print(f"Day 20-1: {total}")
