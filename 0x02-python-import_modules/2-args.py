#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    long = len(argv)
    if long == 1:
        print("0 arguments.")
    elif long > 1:
        if long == 2:
            print("{} argument:".format(long - 1))
            print("1: {:s}".format(argv[1]))
        else:
            for argc in range(1, long):
                print("{}: {}".format(argc, argv[argc]))
