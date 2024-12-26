import random
numbers = []
for i in range(100):
    numbers.append(random.randint(0, 50))
result = None
result = 'Есть китайское несчастливое число' if 4 in numbers else result == 'Все нормально'
print('Результат:\n', result)
