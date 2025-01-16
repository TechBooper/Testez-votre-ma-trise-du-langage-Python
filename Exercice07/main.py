def square(number):
    if not isinstance(number, (int, float)):
        print("Le paramètre doit être un nombre !")
        return None
    return number ** 2

print(square(4))  # return 16
print(square("a"))  # Should print an error message and return None
