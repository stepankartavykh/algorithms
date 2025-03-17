from collections import deque


def count_students(students: list[int], sandwiches: list[int]) -> int:
    students = deque(students)
    sandwiches = deque(sandwiches)

    exit_flag = False

    while students:
        k = 0
        while students:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                k = 0
            else:
                st = students.popleft()
                students.append(st)
                k += 1
            if k == len(students):
                exit_flag = True
                break
        if exit_flag is True:
            break

    return len(students)


if __name__ == '__main__':
    print(count_students([1, 1, 0, 0], [0, 1, 0, 1]))
