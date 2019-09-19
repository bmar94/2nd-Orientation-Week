
numbers = [-5, 23, 0, "kitten", -9, 12, 99, [2, 44], None, 105, -43]

min = numbers[0]
max = numbers[0]
value = 0
div = 0


for i in range(len(numbers)):
    if isinstance(numbers[i], int):
        if numbers[i] <= min:
            min = numbers[i]

    elif isinstance(numbers[i], list):
        for j in numbers[i]:
            if j <= min:
                min = j


for i in range(len(numbers)):
    if isinstance(numbers[i], int):
        if numbers[i] >= max:
            max = numbers[i]

    elif isinstance(numbers[i], list):
        for j in numbers[i]:
            if j >= max:
                max = j

for i in range(len(numbers)):
    if isinstance(numbers[i], int):
        div += 1
        value += numbers[i]

    elif isinstance(numbers[i], list):
        for j in numbers[i]:
            div += 1
            value += j

avg = value / div

print("Min: {}\nMax: {}\nAvg: {}".format(min, max, avg))