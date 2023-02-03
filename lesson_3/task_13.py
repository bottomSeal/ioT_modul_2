def decrease_check(lst):
    if lst == sorted(lst, reverse=True):
        print("Элементы списка расположены в порядке убывания.")
    else:
        print("Элементы списка расположены не в порядке убывания.")


decrease_check([3, 0, 1])
