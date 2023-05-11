#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = 0
    args_c = len(sys.argv)
    for pos in range(args_c - 1):
        current_argu = sys.argv[pos + 1]
        s = s + int(current_argu)
    print("{}".format(s))
