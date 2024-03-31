def expo(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(expo(2,3))
##Watch every line carefully