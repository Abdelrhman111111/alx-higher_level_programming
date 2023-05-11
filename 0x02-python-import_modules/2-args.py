#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_c = len(sys.argv) - 1
    if args_c == 0:
        print("{} arguments.".format(args_c))
    elif args_c == 1:
        print("{} argument:".format(args_c))
    elif args_c > 1:
        print("{} arguments:".format(args_c))
    for x in range(args_c):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
