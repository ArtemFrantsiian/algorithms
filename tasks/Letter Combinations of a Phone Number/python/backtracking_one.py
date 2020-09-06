from typing import List


digitToLetter = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


def solution(digits: str, s: str) -> List[str]:
    if not digits:
        return []

    dtl = digitToLetter[digits[0]]

    combinationOptions = []
    for l in dtl:
        combinationOptions.append(s + l)

    result = [] if len(digits) > 1 else combinationOptions[:]
    for co in combinationOptions:
        result.extend(solution(digits[1:], co))

    return result

def letterCombinations(digits: str) -> List[str]:
    return solution(digits, "")
