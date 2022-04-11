def string_times(times, n):
    result = ""
    for i in range(n):
        result += times
    return result


def front_times(ft, n):
    output = ""
    for i in range(n):
        output += ft[:3]
    return output


def string_bits(bits):
    every_other = ""
    for i in range(len(bits)):
        if i % 2 == 0:
            every_other += bits[i]
    return every_other


def string_splosion(exp):
    exp2 = ""
    for i in range(len(exp)):
        exp2 += exp[:i + 1]
    return exp2


def last2(last):
    if len(last) < 2:
        return 0
    end = last[len(last) - 2:]
    count = 0
    for i in range(len(last) - 2):
        sub = last[i:i + 2]
        if sub == end:
            count = count + 1
    return count
