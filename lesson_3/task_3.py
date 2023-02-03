status_dict = {0: "обычный пользователь", 1: "администратор", 2: "владелец"}


def rights(login, status=0):
    print(login, "-", status_dict[status])


rights("sadasdsad")