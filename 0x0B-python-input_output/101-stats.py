#!/usr/bin/python3
import sys


def print_info():
    print('File size: {:d}'.format(file_size))

    for scode, code_t in sorted(status_codes.items()):
        if code_t > 0:
            print('{}: {:d}'.format(scode, code_t))


status_c = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

l = 0
file_s = 0

try:
    for line in sys.stdin:
        if l != 0 and l % 10 == 0:
            print_info()

        piec = line.split()

        try:
            status = int(piec[-2])

            if str(status) in status_c.keys():
                status_c[str(status)] += 1
        except:
            pass

        try:
            file_s += int(piec[-1])
        except:
            pass

        l += 1

    print_info()
except KeyboardInterrupt:
    print_info()
    raise
