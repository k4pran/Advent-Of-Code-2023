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


def perform_op(p, operation, val):
    if operation == "<":
        return p < int(val)
    if operation == ">":
        return p > int(val)
    raise Exception(f"Unexpected operation {operation}")


def rate_part(part, wfs):

    print (f"PART {part}")
    wf = wfs["in"]
    print("in")
    while True:
        for step in wf:
            if len(step) == 1:
                return sum(part.values()) if step == 'A' else 0
            elif ":" not in step:
                wf = wfs[step]
                print(step)
                break
            else:
                left, right = step.split(":")
                if perform_op(part[left[0]], left[1], left[2:]):
                    if len(right) == 1:
                        return sum(part.values()) if right == 'A' else 0
                    elif ":" not in right:
                        wf = wfs[right]
                        print(right)
                        break

def solve(text):
    wfs, parts = text.split("\n\n")
    wfs = parse_workflows(wfs)
    parts = parse_parts(parts)

    total = 0
    for part in parts:
        total += rate_part(part, wfs)
    return total

with open("day19.txt", 'r') as f:
    text = f.read()

    total = solve(text)

    print(f"Day 19-1: {total}")
