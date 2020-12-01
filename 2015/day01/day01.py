with open('input.txt') as f:
    text = f.readline()

floor = 0
first_found = False
for i, char in enumerate(text):
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
    if floor == -1 and not first_found:
        first_basement = i+1
        first_found = True  

print(floor, first_basement)