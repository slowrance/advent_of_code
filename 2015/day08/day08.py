import re
with open('input.txt') as f:
    names = [line.strip() for line in f.readlines()]


# part1
total = 0
memory = 0
for name in names:
    total += len(name)
    print(name)
    new = re.sub(r'\\[\\\"]', 'X', name)
    new = re.sub(r'\\x..', 'O', new)
    new = re.sub('"', '', new)
    memory += len(new)


print(f'total: {total}, memory: {memory}, difference: {total - memory}')

# part2
total = 0
memory = 0
for name in names:
    total += len(name)
    print(name)

    new = re.sub(r'\\', r'\\\\', name)

    # new = re.sub(r'\\\"', r'\\\"', name)
    new = re.sub(r'\"', r'\\"', new)
    #
    #
    # new = re.sub(r'\\(x..)', r'\\\\\1', new)

    new = '"' + new + '"'

    # new = re.sub(r'\\x..', 'O', new)
    # new = re.sub('"', '', new)
    memory += len(new)
    print(new)


print(f'total: {total}, memory: {memory}, difference: {memory - total}')

#1872 is low