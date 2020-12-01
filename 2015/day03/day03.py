with open('input.txt') as f:
    text = f.readline()

def follow_dirs(text):
    x = 0
    y = 0
    locations = [(x, y)]

    for dir in text:
        if dir == '<':
            x -= 1
        elif dir == '>':
            x += 1
        elif dir == '^':
            y += 1
        elif dir == 'v':
            y -= 1
        # print((x, y))
        locations.append((x, y))
    return locations

# part 1

print(len(follow_dirs(text)))
print(len(set(follow_dirs(text))))

# part 2
santa_x = 0
santa_y = 0
robo_x = 0
robo_y = 0
santa_locations = [(santa_x, santa_y)]
robo_location = [(robo_x, robo_y)]
santa_dirs = text[::2]
robo_dirs = text[1::2]

santa_locations = follow_dirs(santa_dirs)
robo_locations = follow_dirs(robo_dirs)

all_locations = santa_locations + robo_locations
print(len(set(all_locations)))
