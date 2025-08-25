numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)

num1 =[]
for num in numbers:
    num1.append(numbers ** 2)
print(num1)

num2 = [num2 ** 2 for num2 in numbers]
print(num2)