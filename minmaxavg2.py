numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

min = numbers[0]
max = numbers[0]
value = 0

for i in numbers:
    if i <= min:
        min = i

for j in numbers:
    if j >= max:
        max = j

for k in numbers:
    value += k

avg = value / len(numbers)

print("Min: {}\nMax: {}\nAvg: {}".format(min, max, avg))