def get_my_list():
    return [n for n in range(1, 1001) if "3" in str(n)]


print(get_my_list())