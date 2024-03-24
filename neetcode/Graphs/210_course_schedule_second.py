from collections import defaultdict


def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    # TODO resolve later
    course_to_prers = defaultdict(set)
    for c, prerequisite in prerequisites:
        course_to_prers[c].add(prerequisite)

    visited_courses = set()
    current_path = set()
    ordering = []

    def dfs(course_num: int) -> bool:
        if course_num in current_path:
            return False
        if course_num in visited_courses:
            return True
        current_path.add(course_num)
        for course_to_visit in course_to_prers[course_num]:
            if not dfs(course_to_visit):
                return False
        current_path.remove(course_num)
        visited_courses.add(course_num)
        ordering.append(course_num)
        return True

    for course in range(num_courses):
        if not dfs(course):
            return []
    return ordering


if __name__ == '__main__':
    print(find_order(num_courses=2, prerequisites=[[1, 0]]))
    print(find_order(num_courses=2, prerequisites=[[1, 0], [0, 1]]))
    print(find_order(num_courses=7, prerequisites=[[0, 1], [1, 2], [2, 3], [2, 4], [1, 5], [5, 6], [3, 4], [3, 5]]))
