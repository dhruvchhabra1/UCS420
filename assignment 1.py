# Q1.1
student_name = "Dhruv"

for count in range(3):
    print(student_name)


# Q2.1
a = 100
b = 200
c = 300

total = a + b + c
print("Sum of three numbers:", total)


# Q2.2
first = "Hello"
middle = " "
last = "World"

message = first + middle + last
print("Concatenated string:", message)


# Q4.1
print("Table of 7:")
number = 7

for j in range(1, 11):
    answer = number * j
    print(number, "x", j, "=", answer)

print("\nTable of 9:")
number = 9

for j in range(1, 11):
    answer = number * j
    print(number, "x", j, "=", answer)


# Q4.2
number = int(input("\nEnter a number: "))

for j in range(1, 11):
    answer = number * j
    print(number, "x", j, "=", answer)


# Q4.3
number = int(input("\nEnter a number: "))
total = 0

for j in range(1, number + 1):
    total = total + j

print("Sum from 1 to", number, "is", total)


# Q5.1
first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
third_num = float(input("Enter third number: "))

if first_num >= second_num and first_num >= third_num:
    largest = first_num
elif second_num >= first_num and second_num >= third_num:
    largest = second_num
else:
    largest = third_num

print("Maximum number is:", largest)


# Q5.2
limit = int(input("\nEnter a number: "))
total = 0

for value in range(1, limit + 1):
    if value % 7 == 0:
        if value % 9 == 0:
            total = total + value

print("Sum of numbers divisible by 7 and 9:", total)


# Q5.3
limit = int(input("\nEnter a number: "))
prime_sum = 0

for number in range(2, limit + 1):
    prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            prime = False
            break

    if prime:
        prime_sum = prime_sum + number

print("Sum of prime numbers:", prime_sum)


# Q6.1
def add_odd_numbers(limit):
    total = 0

    for number in range(1, limit + 1):
        if number % 2 == 1:
            total = total + number

    return total


limit = int(input("Enter a number: "))
answer = add_odd_numbers(limit)

print("Sum of odd numbers:", answer)


# Q6.2
def check_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def add_primes(limit):
    total = 0

    for number in range(2, limit + 1):
        if check_prime(number):
            total = total + number

    return total


limit = int(input("\nEnter a number: "))
answer = add_primes(limit)

print("Sum of prime numbers:", answer)
