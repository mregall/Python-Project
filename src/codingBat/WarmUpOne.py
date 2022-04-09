def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
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


def near_hundred(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


def makes10(a, b):
    return (a == 10) or (b == 10) or (a + b == 10)


def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)


def not_string(not_str):
    if len(not_str) >= 3 and not_str[:3] == "not":
        return not_str
    return "not " + not_str


# str[:3] goes from the start of the string up to but not including index 3


# Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of
# n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str, n):
    begin = str[:n]
    rest = str[n + 1:]
    return begin + rest


def front_back(str):
    if len(str) <= 1:
        return str
    mid = str[1:len(str) - 1]
    return str[len(str) - 1] + mid + str[0]


def front3(str):
    if len(str) < 3:
        return str + str + str
    else:
        front = str[:3]
        return front + front + front
# did this one w/ looking at the answer!!
