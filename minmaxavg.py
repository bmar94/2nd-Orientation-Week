numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

min=numbers[0]
max=numbers[0]
sum=0
        
for i in range(len(numbers)):
    if numbers[i] >max:
        max=numbers[i]
    if numbers[i] <min:
        min=numbers[i]
    sum+=numbers[i]

avg= sum/len(numbers)

print("Min: {}\nMax: {}\nAvg: {}".format(min, max, avg))