# Q-1

roll_number = "1024170085"

numbers = []
for digit in roll_number:
    if digit.isdigit():
        numbers.append(int(digit) * 10)

print("Original list:", numbers)

print("\nAdding elements:")
print("Before adding:", numbers)

numbers.append(12)
print("After append:", numbers)

numbers.insert(3, 43)
print("After insert:", numbers)

print("\nRemoving elements:")
numbers.remove(10)
print("After removing 10:", numbers)

deleted = numbers.pop(5)
print("Removed element:", deleted)
print("List now:", numbers)

print("\nSorting:")
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Ascending:", ascending)
print("Descending:", descending)

print("First three:", numbers[:3])
print("Last three:", numbers[-3:])

print("\nElements greater than average:")

total = 0
for value in numbers:
    total = total + value

avg = total / len(numbers)
print("Average:", round(avg, 2))

above_average = []
for value in numbers:
    if value > avg:
        above_average.append(value)

print("Greater than average:", above_average)


# Q-2

scores = tuple(numbers[:8])

highest = max(scores)
lowest = min(scores)

print("\nHighest score:", highest)
print("Index of highest score:", scores.index(highest))

print("Lowest score:", lowest)
print("Number of times lowest occurs:", scores.count(lowest))

backwards = []
for i in range(len(scores) - 1, -1, -1):
    backwards.append(scores[i])

print("Reversed tuple as list:", backwards)

search_score = int(input("Enter a score to search: "))

if search_score in scores:
    position = scores.index(search_score)
    print("Score found at index:", position)
else:
    print("Score not found")

try:
    scores[0] = 100
except TypeError as error:
    print("Tuple cannot be changed:", error)

first_score = scores[0]
second_score = scores[1]
remaining_scores = scores[2:]

print("First:", first_score)
print("Second:", second_score)
print("Remaining:", list(remaining_scores))


# Q-3

import random
from collections import Counter

random.seed(1024170085)

values = []

for i in range(100):
    values.append(random.randint(100, 900))

odd = 0
even = 0

for value in values:
    if value % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("\nOdd numbers count:", odd)
print("Even numbers count:", even)


def prime_check(value):
    if value < 2:
        return False

    for divisor in range(2, value):
        if value % divisor == 0:
            return False

    return True


primes = []

for value in values:
    if prime_check(value):
        primes.append(value)

print("Prime numbers count:", len(primes))
print("Prime numbers:", primes)

frequency = Counter(values)
common = frequency.most_common(1)

if common:
    number, times = common[0]
    print("Most frequent number:", number)
    print("It occurs", times, "times")


# Q-4

roll_digits = [1, 0, 2, 4, 1, 7, 0, 0]

set_a = set()
set_b = set()

for digit in roll_digits:
    set_a.add(digit * 7)
    set_b.add(digit * 9)

print("\nSet A:", set_a)
print("Set B:", set_b)

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)

only_a = set_a - set_b
only_b = set_b - set_a

print("A - B:", only_a)
print("B - A:", only_b)

symmetric = set_a ^ set_b
print("Symmetric difference:", symmetric)

print("Is A a subset of B?", set_a <= set_b)
print("Is B a superset of A?", set_b >= set_a)

remove_value = int(input("Enter a value to remove from A: "))

set_a.discard(remove_value)

print("A after discard:", set_a)
print("discard() does not give an error if the value is not present.")


# Q-5

student = {
    "name": "Dhruv",
    "roll_no": "1024170085",
    "branch": "Computer Science",
    "age": 20,
    "city": "Chandigarh"
}

student["location"] = student.pop("city")

print("\nAfter changing city to location:")
print(student)

student["cgpa"] = 8.59
print("\nAfter adding CGPA:")
print(student)

student["age"] += 1
print("\nAfter increasing age:")
print(student)

copy_one = student.copy()
copy_two = student.copy()

branch_value = copy_one.pop("branch")

print("\nUsing pop():")
print("Removed value:", branch_value)
print("Dictionary:", copy_one)

del copy_two["branch"]

print("\nUsing del:")
print(copy_two)

print("\npop() returns the deleted value, while del only removes the key.")

print("\nDictionary contents:")

for item in student:
    print(item, "->", student[item])

if "email" in student:
    print("Email:", student["email"])
else:
    print("Email key not found")

friend = {
    "name": "Aditya Gupta",
    "roll_no": "1024170204",
    "branch": "COPC",
    "age": 20,
    "city": "faridabad"
}

combined = student.copy()
combined.update(friend)

print("\nMerged dictionary:")
print(combined)

print("If the same key exists in both dictionaries, the value from the second dictionary replaces the first.")

text_values = {}

for key, value in student.items():
    if type(value) == str:
        text_values[key] = value

print("\nDictionary containing only string values:")
print(text_values)
