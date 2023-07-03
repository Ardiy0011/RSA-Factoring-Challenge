#!/usr/bin/python3

import sys

def factorize(n):
    return [(i, n // i) for i in range(2, n // 2 + 1) if n % i == 0]

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    with open(sys.argv[1]) as file:
        lines = file.readlines()

    for line in lines:
        number = int(line.strip())
        factorizations = factorize(number)
        [print(f"{number}={p}*{q}") for p, q in factorizations]

if __name__ == "__main__":
    main()
