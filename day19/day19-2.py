from collections import deque
from functools import reduce


def parse_rules(rules):
    return rules.split(",")


def parse_workflows(wfs):
    wfs_dict = dict()
    for wf in wfs.splitlines():
        name, rules = wf.split("{")
        rules = parse_rules(rules[:-1])

        wfs_dict[name] = rules
    return wfs_dict


def parse_parts(parts_block):
    all_parts = []
    for parts in parts_block.splitlines():
        parsed_parts = dict()
        for part in parts[1:-1].split(","):
            p_name, p_val = part.split("=")
            parsed_parts[p_name] = int(p_val)
        all_parts.append(parsed_parts)
    return all_parts


def perform_op(operation, val, rnge):
    if operation == "<":
        return (rnge[0], int(val) - 1), (max(int(val), rnge[0]), rnge[1])
    if operation == ">":
        return (int(val) + 1, rnge[1]), (rnge[0], min(int(val), rnge[1]))
    raise Exception(f"Unexpected operation {operation}")


def rate_part(part, wfs):
    print (f"PART {part}")
    print("in")
    accepted_total = 0
    q = deque()
    q.append((wfs["in"], {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}))
    while True:
        if len(q) == 0:
            return accepted_total

        wf, rnges = q.popleft()
        for step in wf:
            if len(step) == 1:
                print()
                if step == "A":
                    accepted_total += reduce((lambda x, y: x * y), [(r[1] - r[0] + 1) for r in rnges.values()])
            elif ":" not in step:
                q.append((wfs[step], dict(rnges)))
            else:
                left, right = step.split(":")
                p = left[0]
                success_range, fail_range = perform_op(left[1], left[2:], rnges[p])
                if success_range and success_range[1] >= success_range[0]:
                    updated_rnges = dict(rnges)
                    updated_rnges[p] = success_range
                    if len(right) == 1:
                        print()

                        if right == "A":
                            accepted_total += reduce((lambda x, y: x * y), [(r[1] - r[0] + 1) for r in updated_rnges.values()])

                    if ":" not in right and len(right) != 1:
                        q.append((wfs[right], dict(updated_rnges)))
                if fail_range and fail_range[1] >= fail_range[0]:
                    rnges[p] = fail_range
                else:
                    break

def solve(text):
    wfs, parts = text.split("\n\n")
    wfs = parse_workflows(wfs)
    parts = parse_parts(parts)

    return rate_part(parts[0], wfs)

with open("day19.txt", 'r') as f:
    text = f.read()

    total = solve(text)

    print(f"Day 19-2: {total}")


#167010937327821
#167409079868000
#6795257395905