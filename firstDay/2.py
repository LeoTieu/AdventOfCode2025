def first_solution(puzzle_input: list) -> int:
    """
    First brute force solution
    O(N*M) where N is the amount of rotations and M is the average turns 
    """
    dial = 50
    counter = 0
    for rotation in puzzle_input:
        direction = rotation[0]
        amount = int(rotation[1::])

        if direction == "R":
            for _ in range(amount):
                dial += 1
                if dial == 100:
                    dial = 0
                    counter += 1
        else:
            for _  in range(amount):
                dial -= 1
                if dial == -1:
                    dial = 99
                elif dial == 0:
                    counter += 1
    return counter


def second_solution(puzzle_input: list) -> int:
    """
    Second solution
    O(N) where N is the amount of rotations
    """
    dial = 50
    counter = 0
    for rotation in puzzle_input:
        direction = rotation[0]
        amount = (rotation[1::])

        # highest number is 998
        if len(amount) == 3:
            counter += int(amount[0])
            amount = int(amount[1::])
        else:
            amount = int(amount)
            
        if direction == "R":
            dial += amount
            if dial >= 100:
                counter += 1
                dial = dial % 100
        else:
            if dial == 0:
                dial = (dial - amount) % 100
            else:
                dial -= amount
                if dial <= 0:
                    counter += 1
                    dial %= 100
    return counter


if __name__ ==  '__main__':
    with open("PuzzleInput.txt", "r", encoding="utf-8") as file:
        puzzle_input = file.read().split()
    print(first_solution(puzzle_input))
    print(second_solution(puzzle_input))
