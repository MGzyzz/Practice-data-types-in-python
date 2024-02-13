def check_remainder(a, b):
    remainder = a % b
    if remainder == 0:
        return False
    else:
        return True


number_one = input("Enter dividend:")

number_two = input("Enter divisor:")

print(check_remainder(int(number_one), int(number_two)))

