def add_commas(num):
    num_str = str(num)  
    result = ""

    for i, digit in enumerate(num_str[::-1]):
        result = digit + result
        if (i + 1) % 3 == 0 and i != len(num_str) - 1:
            result = "," + result

    return result

num = int(input("Nhập số nguyên : "))
print("Số nguyên với dấu phân cách hàng nghìn : ", add_commas(num))

