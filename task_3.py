string_one = input("Enter two strings:\nFirst string:")
string_two = input("Second string:")

if len(string_one) > len(string_two):
    print(f"First string is longer by {len(string_one) - len(string_two)} characters.")
elif len(string_one) == len(string_two):
    print("Strings are equal length.")
else:
    print(f"Second string is longer by {len(string_two)- len(string_one)} characters.")