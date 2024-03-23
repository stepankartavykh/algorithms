from collections import defaultdict


def canFinish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    h = defaultdict(set)
    for c, prerequisite in prerequisites:
        h[c].add(prerequisite)

    visited_courses = set()

    def dfs(course_num) -> bool:
        if course_num in visited_courses:
            return False
        reqs = h.get(course_num)
        if not reqs:
            return True
        visited_courses.add(course_num)
        for req in reqs:
            if not dfs(req):
                return False
        visited_courses.remove(course_num)
        h[course_num].clear()
        return True

    for course in range(num_courses):
        if not dfs(course):
            return False
    return True


if __name__ == '__main__':
    print(canFinish(num_courses=2, prerequisites=[[1, 0]]))
    print(canFinish(num_courses=2, prerequisites=[[1, 0], [0, 1]]))
    print(canFinish(num_courses=7, prerequisites=[[0, 1], [1, 2], [2, 3], [2, 4], [1, 5], [5, 6], [3, 4], [3, 5]]))
