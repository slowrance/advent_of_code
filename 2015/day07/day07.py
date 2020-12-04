with open('input.txt') as f:
    real_input = [line.strip() for line in f.readlines()]

test_input = ['123 -> x',
              '456 -> y',
              'x AND y -> d',
              'x OR y -> e',
              'x LSHIFT 2 -> f',
              'y RSHIFT 2 -> g',
              'NOT x -> h',
              'NOT y -> i']
def parse_instruction(instruction):
    pass

def process_instruction(instruction):
    parts = instruction.split()
    if len(parts) == 3:
        operand1, operator, operand2 = parts
        if signals.get(operand1) and not type(signals.get(operand1)) == int:
            signals[operand1] = process_instruction(signals[operand1])
            operand1 = signals[operand1]
        elif type(signals.get(operand1)) == int:
            operand1 = signals[operand1]
        if signals.get(operand2) and not type(signals.get(operand2)) == int:
            signals[operand2] = process_instruction(signals[operand2])
            operand2 = signals[operand2]
        elif type(signals.get(operand2)) == int:
            operand2 = signals[operand2]
        if operator == 'AND':
            return int(operand1) & int(operand2)
        if operator == 'OR':
            return int(operand1) | int(operand2)
        if operator == 'LSHIFT':
            return int(operand1) << int(operand2)
        if operator == 'RSHIFT':
            return int(operand1) >> int(operand2)


    elif len(parts) == 2:
        operator, operand1 = parts
        if not type(signals.get(operand1)) == int:
            signals[operand1] = process_instruction(signals[operand1])
            operand1 = signals[operand1]
        else:
            operand1 = signals[operand1]
        if operator == 'NOT':
            return 65535 - int(operand1)

    elif len(parts) == 1:
        operand = parts[0]
        if not type(signals.get(operand)) == int:
            signals[operand] = process_instruction(signals[operand])
            operand = signals[operand]
        else:
            operand = signals[operand]
        return operand

signals = {}
for input in real_input:
    instruction, output = input.split(' -> ')
    if instruction.isnumeric():
        signals[output] = int(instruction)
    else:
        signals[output] = instruction

for signal in signals:
    if type(signals[signal]) == int:
        continue
    signals[signal] = process_instruction(signals[signal])

for key in sorted(signals):
    print(f'{key}: {signals[key]}')

# original value for 'b' in input.txt was 1674