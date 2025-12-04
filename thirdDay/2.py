def first_solution(puzzle_input):
    biggestList = []
    for number in puzzle_input.split():
        print(number)
        pointer_1 = -13
        pointer_2 = -12
        pointer_3 = -11
        pointer_4 = -10
        pointer_5 = -9
        pointer_6 = -8
        pointer_7 = -7
        pointer_8 = -6
        pointer_9 = -5
        pointer_10 = -4
        pointer_11 = -3
        pointer_12 = -2
        pointer_13 = -1
        pointer_list = [pointer_1, pointer_2, pointer_3, pointer_4, pointer_5, pointer_6, pointer_7, pointer_8, pointer_9, pointer_10, pointer_11, pointer_12, pointer_13]
        while pointer_1 >= (len(number) * -1):
            pointer_list[0] = pointer_1
            if number[pointer_1] >= number[pointer_2]:
                for index in range(len(pointer_list) - 2, -1, -1):
                    if number[pointer_list[index]] > number[pointer_list[index + 1]]:
                        pointer_list[index + 1] = pointer_list[index]

            pointer_1 -= 1


        # Yes, unoptimised, slow, but it's such a small amount so idc
        current = ""
        for pointer in pointer_list:
            current += number[pointer]
        biggestList.append(int(current))
        print(pointer_list)
    return sum(biggestList)


def get_input(file_location: str):
    with open(file_location, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == '__main__':
    # print(first_solution(get_input("PuzzleInput.txt")))
    print(first_solution(get_input("TestInput.txt")))
