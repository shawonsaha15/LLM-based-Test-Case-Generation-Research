def letter_combinations(digits: str) -> list[str]:
    digit_map = {
        '2': "abc", '3': "def", '4': "ghi",
        '5': "jkl", '6': "mno", '7': "pqrs",
        '8': "tuv", '9': "wxyz"
    }

    if not digits:
        return []

    result = []
    n = len(digits)

    def backtrack(index: int, path: str):
        if index == n:
            result.append(path)
            return

        letters = digit_map.get(digits[index], "")

        for letter in letters:
            backtrack(index + 1, path + letter)

    backtrack(0, "")
    return result