import random
numbers = []
for i in range(10):
    numbers.append(random.randint(0, 20))
print(numbers)
print('Вы нашли') if 13 in numbers else print('Вы проиграли')



