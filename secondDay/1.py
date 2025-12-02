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
            if length % 2 != 0:
                continue
            
            middle = length // 2
            if current[:middle] != current[middle:]:
                continue
            invalids.append(int(current))

    return(sum(invalids))

def get_input(file_location: str):
    with open(file_location, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == '__main__':
    print(first_solution(get_input("PuzzleInput.txt")))
