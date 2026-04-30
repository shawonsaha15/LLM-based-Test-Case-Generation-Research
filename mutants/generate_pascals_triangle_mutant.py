def generate_pascals_triangle(num_rows: int) -> list[list[int]]:
    result = []

    for i in range(num_rows):
        result.append([1] * (i + 1))

    for i in range(2, num_rows):
        for j in range(1, len(result[i]) - 1):
            result[i][j] = result[i - 1][j - 1] - result[i - 1][j]

    return result