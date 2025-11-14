numbrs = [1,2,3,4,5,6,7,8,9]

def cube_sorted(number):
    number = set(number)
    cubes = [n ** 3 for n in number]
    cubes.sort(reverse=True)
    return cubes

print(cube_sorted(numbrs))

