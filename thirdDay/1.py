def first_solution(puzzle_input):
    biggestList = []
    for number in puzzle_input.split():
        pointer_1 = -1
        pointer_2 = -2
        pointer_3 = -3
        while pointer_3 >= (len(number) * -1):
            if number[pointer_3] > number[pointer_2]:
                if number[pointer_1] < number[pointer_2]:
                    pointer_1 = pointer_2
                pointer_2 = pointer_3

            pointer_3 -= 1              
        biggestList.append(int(number[pointer_2] + number[pointer_1]))
    print(biggestList)
    return sum(biggestList)


def get_input(file_location: str):
    with open(file_location, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == '__main__':
    print(first_solution(get_input("PuzzleInput.txt")))
