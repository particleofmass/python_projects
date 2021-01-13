from recursion import factorial
'''There's a frog wanting to cross a river and there are stones
placed 1feet apart on which the frog can jump and then cross the
river. The frog can also make a 2feet jump. In how many ways can the
frog cross the river.'''


def frog1(feet):
    if feet > 1:
        return frog(feet - 1) + frog(feet - 2)
    else:
        return 1


def frog(feet):
    feet += 1
    nums = [0] * feet
    nums[0], nums[1] = 1, 1
    for i in range(2, feet):
        nums[i] = nums[i - 1] + nums[i - 2]
    return nums[3]


print(frog(3))