def move_zeros(lst):

    qtd_zeros = lst.count(0)
    new_lst = [num for num in lst if not num == 0]
    for _ in range(qtd_zeros):
        new_lst.append(0)
    return new_lst


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
