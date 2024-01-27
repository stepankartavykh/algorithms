from typing import List

# TODO monotonic stack? What data structure is that?
# TODO must be resolved!


def daily_temperatures(temperatures: List[int]) -> List[int]:
    answer = []

    i_temp_index = 0
    while i_temp_index < len(temperatures):
        i_temp = temperatures[i_temp_index]
        for j in range(i_temp_index + 1, len(temperatures)):
            if temperatures[j] > i_temp:
                answer.append(j - i_temp_index)
                break
        else:
            answer.append(0)

        i_temp_index += 1

    return answer


def daily_temperatures_second_solution(temperatures: List[int]) -> List[int]:
    # TODO SOLVE THIS AGAIN LATER!
    answer = [0] * len(temperatures)
    stack_temps_and_indexes = []

    for index, temp in enumerate(temperatures):
        while stack_temps_and_indexes and temp > stack_temps_and_indexes[-1][0]:
            last_t, last_index = stack_temps_and_indexes.pop()
            answer[last_index] = index - last_index
        stack_temps_and_indexes.append((temp, index))

    return answer


if __name__ == '__main__':
    print(daily_temperatures_second_solution([73, 74, 75, 71, 69, 72, 76, 73]))
    print(daily_temperatures_second_solution([30, 40, 50, 60]))
    print(daily_temperatures_second_solution([30, 60, 90]))
    print(daily_temperatures_second_solution([30, 30]))
    print(daily_temperatures_second_solution([30]))
