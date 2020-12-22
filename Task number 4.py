import random


number = 0
while True:
    try:
        number = input("Enter number: ")
        number = int(number)
        break
    except:
        print("Enter integer number!")

array = []
for i in range(20):
    random_number = random.randint(1,5)

    if i % 2 == 0:
        random_number *= -1

    array.append(random_number)

print(array)

count = 0
for i in array:
    if number == i:
        count += 1

print(f"Number {number} repeat {count} times")