with open("PuzzleInput.txt", "r", encoding="utf-8") as file:
    puzzle_input = file.read().split()

dial = 50
counter = 0

for rotation in puzzle_input:
    direction = rotation[0]
    amount = int(rotation[1::])
    
    if direction == "R":
        dial += amount
    else:
        dial -= amount

    dial = dial % 100

    if dial == 0:
        counter += 1
    print(dial)

print(counter)