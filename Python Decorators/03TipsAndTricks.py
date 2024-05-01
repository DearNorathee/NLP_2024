# https://www.youtube.com/watch?v=C-gEQdGVXbk&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=105&ab_channel=CoreySchafer
num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2 
print(f"{total:,}")

# with open('test.text','rt') as f:
#     # context manager
#     file_contents = f.read()


class Person():
    pass

person = Person()
person02 = Person()

first_key = 'first'
first_val = 'Corey'

setattr(person,first_key,first_val)

print(person.first)

person_info = {'first':'Corey','last':'Schafer'}

for key, value in person_info.items():
    setattr(person02, key, value)

print(person02.first)
print(person02.last)




