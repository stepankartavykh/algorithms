from typing import List


def cal_points(operations: List[str]) -> int:
    records = []
    total_sum = 0
    for operation in operations:
        if operation not in ('+', 'D', 'C'):
            score = int(operation)
            records.append(score)
            total_sum += score
        elif operation == '+':
            score = records[len(records) - 2] + records[len(records) - 1]
            records.append(score)
            total_sum += score
        elif operation == 'D':
            score = records[len(records) - 1] * 2
            records.append(score)
            total_sum += score
        elif operation == 'C':
            score = records.pop()
            total_sum -= score

    return total_sum


if __name__ == '__main__':
    print(cal_points(["5", "2", "C", "D", "+"]))
