#!/usr/bin/python3

def factorize(re):
    return [(i, re // i) for i in range(2, re // 2 + 1) if re % i == 0]

def main():
    with open("tests/test00") as file:
        lines = file.readlines()

    for value in lines:
        numss = int(value.strip())
        facts = factorize(numss)
        [print(f"{numss}={p}*{q}") for p, q in facts]

main()
