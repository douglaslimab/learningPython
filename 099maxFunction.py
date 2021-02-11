def howBig(* num):
    max_num = 0
    for index, item in enumerate(num):
        if index == 0:
            max_num = item
        if item > max_num:
            max_num = item
    print(max_num)

# main
howBig(1, 2, 3, 4, 5, 6, 7, 0)
howBig(2, 3, 5, 1, 6, 8, 9,)
howBig(90, 80, 22)