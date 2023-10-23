from typing import List


def generate(num_rows: int) -> List[List[int]]:
    pascal_triangle = []
    stage = [1]
    pascal_triangle.append(stage)

    for row in range(1, num_rows):
        stage = [1]
        for index_row in range(1, row):
            element = pascal_triangle[row - 1][index_row - 1] + pascal_triangle[row - 1][index_row]
            stage.append(element)

        stage.append(1)
        pascal_triangle.append(stage)
    return pascal_triangle


if __name__ == '__main__':
    for i in range(20):
        print(generate(i))
