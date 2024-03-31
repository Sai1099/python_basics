try:
    value = 10/0
    num = print(int(input("Enter the required Num: ")))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)