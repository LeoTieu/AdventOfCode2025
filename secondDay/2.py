def first_solution(puzzle_input):
    puzzle_input = puzzle_input.split(",")
    puzzle_input = [x.split("-") for x in puzzle_input]

    invalids = []
    for interval in puzzle_input:
        start = int(interval[0])
        end = int(interval[1])

        for current in range(start,end + 1):
            current  = str(current)
            length = len(current)
            for size in range(1, length // 2 + 1):
                if helper(size, current) is False:
                    invalids.append(int(current))
                    break
    return sum(invalids)


def helper(size, number):
    n = len(number)
    if size <= 0:
        return True
    if n % size != 0:
        return True
    first_block = number[:size]
    blocks = n // size
    for i in range(1, blocks):
        if number[i * size:(i + 1) * size] != first_block:
            return True
    return False


def get_input(file_location: str):
    with open(file_location, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == '__main__':
    print(first_solution(get_input("PuzzleInput.txt")))
