def first_solution(puzzle_input: list) -> int:
    """
    First brute force solution
    O(N*M) where N is the amount of inputs and M is the average turns 
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


if __name__ ==  '__main__':
    with open("PuzzleInput.txt", "r", encoding="utf-8") as file:
        puzzle_input = file.read().split()
    print(first_solution(puzzle_input))
