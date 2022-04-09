def array123(nums):

    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False


def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True
    return False

# return ((a_smile and b_smile) or (not a_smile and not b_smile))

# return (a_smile == b_smile)


def sum_double(a, b):
    if a != b:
        return a + b
    if a == b:
        return (a + b) * 2


def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2


def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)


