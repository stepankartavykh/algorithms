import timeit

def test_update_list_values():
    setup = """
my_list = list(range(1000000))
new_value = 10
"""

    stmt_loop = """
for i in range(len(my_list)):
    my_list[i] = new_value
"""

    stmt_list_comp = """
my_list = [new_value for _ in my_list]
"""

    print("Time taken to update list values using a loop:")
    print(timeit.timeit(stmt_loop, setup=setup, number=1000))

    print("\nTime taken to update list values using a list comprehension:")
    print(timeit.timeit(stmt_list_comp, setup=setup, number=1000))


def test_update_dict_values():
    setup = """
my_dict = {i: i for i in range(1000000)}
new_value = 10
"""

    stmt_loop = """
for key in my_dict:
    my_dict[key] = new_value
"""

    stmt_dict_comp = """
my_dict = {key: new_value for key in my_dict}
"""

    print("Time taken to update dictionary values using a loop:")
    print(timeit.timeit(stmt_loop, setup=setup, number=1000))

    print("\nTime taken to update dictionary values using a dictionary comprehension:")
    print(timeit.timeit(stmt_dict_comp, setup=setup, number=1000))


test_update_dict_values()
test_update_list_values()
