from pprint import pprint

with open('input.txt') as f:
    instructions = [line.strip() for line in f.readlines()]

# instructions = ['turn on 499,499 through 500,500', 'toggle 499,500 through 500,500']

def decode_instruction(instruction):
    parts = instruction.split()
    command = ''.join(parts[:-3])
    start = parts[-3]
    start_x, start_y = start.split(',')
    end = parts[-1]
    end_x, end_y = end.split(',')
    # print(f'{command} {start_x} {start_y} {end_x} {end_y}')
    return command, int(start_x), int(start_y), int(end_x), int(end_y)


# part 1
grid = [[0] * 1000 for i in range(1000)]

for instruction in instructions:
    command, start_x, start_y, end_x, end_y = decode_instruction(instruction)
    # if start_x > end_x:
    #     start_x, end_x = end_x, start_x
    # if start_y > end_y:
    #     start_y, end_y = end_y, start_y
    if start_x > end_x or start_y > end_y:
        print('bad')
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if command == 'turnon':
                grid[x][y] = 1
            elif command == 'turnoff':
                grid[x][y] = 0
            elif command == 'toggle':
                grid[x][y] = int(not grid[x][y])

total_on = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        total_on += grid[x][y]
print(total_on)

# part 2
grid = [[0] * 1000 for i in range(1000)]

for instruction in instructions:
    command, start_x, start_y, end_x, end_y = decode_instruction(instruction)
    # if start_x > end_x:
    #     start_x, end_x = end_x, start_x
    # if start_y > end_y:
    #     start_y, end_y = end_y, start_y
    if start_x > end_x or start_y > end_y:
        print('bad')
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if command == 'turnon':
                grid[x][y] += 1
            elif command == 'turnoff':
                if grid[x][y] > 0:
                    grid[x][y] -= 1
            elif command == 'toggle':
                grid[x][y] += 2


total_on = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        total_on += grid[x][y]
print(total_on)

