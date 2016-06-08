
    

n = 1000
numbers = range(2, n)
results = []
while numbers != []:
    results.append(numbers[0])
    temp = []
    for num in numbers:
        if num % numbers[0] != 0:
            temp.append(num)
    numbers = list(temp)
print len(results)