#!/usr/bin/python3

def factorize(n):
    return [(i, n // i) for i in range(2, n // 2 + 1) if n % i == 0]

def main():
    with open("tests/test00") as file:
        lines = file.readlines()

    for value in lines:
        numss = int(value.strip())
        facts = factorize(numss)
        [print(f"{numss}={p}*{q}") for p, q in facts]

main()
