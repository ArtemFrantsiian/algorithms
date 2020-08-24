import math
import unittest
from typing import List


def parsing(expression: str) -> (List[str], List[str]):
    operators = []
    fractions = []
    if not expression.startswith('-'):
        operators.append("+")

    fraction_start = False
    for char in expression:
        if char == "+" or char == "-":
            fraction_start = False
            operators.append(char)
            continue

        if not fraction_start:
            fraction_start = True
            fractions.append(char)
        else:
            fractions[-1] = fractions[-1] + char

    return operators, fractions


def to_base_denominator(fractions: List[str]) -> int:
    lcm = None
    for fraction in fractions:
        denominator = int(fraction.split("/")[1])
        lcm = (lcm * denominator) // math.gcd(lcm, denominator) if lcm is not None else denominator

    return lcm


def add(operators: List[str], fractions: List[str], lcm: int) -> int:
    result = 0
    for i in range(0, len(fractions)):
        fraction = fractions[i].split("/")
        multiplier = lcm // int(fraction[1])

        if operators[i] == "+":
            result += int(fraction[0]) * multiplier
        else:
            result -= int(fraction[0]) * multiplier
    return result


def solution(expression: str) -> str:
    operators, fractions = parsing(expression)
    lcm = to_base_denominator(fractions)
    result = add(operators, fractions, lcm)

    d = math.gcd(lcm, result)

    if d != 1:
        return f"{result // d}/{lcm // d}"
    else:
        return f"{result}/{lcm}"


class Test(unittest.TestCase):
    def test1(self):
        return self.assertEqual(solution("-1/2+1/2"), "0/1")

    def test2(self):
        return self.assertEqual(solution("-1/2+1/2+1/3"), "1/3")

    def test3(self):
        return self.assertEqual(solution("1/3-1/2"), "-1/6")

    def test4(self):
        return self.assertEqual(solution("5/3+1/3"), "2/1")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
