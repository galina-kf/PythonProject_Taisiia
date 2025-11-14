numbers =  [15, 5, 8, 46, 13, 26, 14, 587]

def square_with_search(numbers_: list[int], search_number: int) -> list[int]:
    square_results = []
    for n in numbers_:
        if n == search_number:
            break
        square_results.append(n*n)
    return square_results

print(square_with_search(numbers,26))

