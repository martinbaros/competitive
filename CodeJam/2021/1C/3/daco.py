#!/usr/bin/env python3

import sys

def run_with_file(input_file):
    scores = {}
    for line in input_file:
        line = line.strip()
        if (not line) or line.startswith('#'):
            continue
        parts = line.split()
        if parts[0] == 'summary':
            print(" ".join(parts[1:]))
            for name in sorted(scores):
                print("  {0}: {1}".format(name,scores[name]))
        elif parts[0] == 'add':
            if parts[1] in scores:
                scores[parts[1]] = scores[parts[1]] + int(parts[3])
            else:
                scores[parts[1]] = int(parts[3])
        elif parts[0] == 'podium':
            print("Medal podium")
            printed = 0
            for key in sorted(scores, key = scores.get, reverse=True):
                if printed >= 3:
                    break
                printed += 1
                print("  "+key)
        elif parts[0] == 'csv':
            with open(parts[1],"w") as f:
                print("team,score",file=f)
                for name in sorted(scores):
                    print("{0},{1}".format(name,scores[name]),file=f)
        else:
            print("Unknown command ('{}')!".format(parts[0]))

def main():
    if len(sys.argv) != 2:
        print("Run with exactly one argument - filename with commands.")
        return
    with open(sys.argv[1]) as inp:
        run_with_file(inp)

if __name__ == '__main__':
    main()
