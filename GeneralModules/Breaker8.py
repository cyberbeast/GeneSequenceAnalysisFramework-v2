__author__ = 'Sandesh'


def breaker8(input_string, brk_val):
    output = []
    temp = ''
    i = -1
    while i < len(input_string)-brk_val:
        i += 1
        for j in range(i, i + brk_val):
            temp = temp + input_string[j]
        output.append(temp)
        temp = ''
    return output
