import json
person = {
    'name': 'Max',
    'age': 10,
    'phones': ['9111', '738333']
}
result = json.dumps(person)
print(result)
print(type(result))

Me = ['Dima', 16, 'Cheboksary']
result2 = json.dumps(Me)
print(result2)
print(type(result2))