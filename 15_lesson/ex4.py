def fizz_buzz(max_number: int) -> list:
    results = []
    for n in range(1, max_number + 1):
        if n % 3 == 0 and n % 5 == 0:
            results.append("FizzBuzz")
        elif n % 3 == 0:
            results.append("Fizz")
        elif n % 5 == 0:
            results.append("Buzz")
        else:results.append(str(n))
    return results

numbers = fizz_buzz(20)
print(numbers)