print("""ДВОИЧНАЯ СИСТЕМА""")
num_in_2_system = 0b11001
print("Число записанное в (num_in_2_system) в десятичной системе равно: {}\n".format(num_in_2_system))

print("""ВОСЬМЕРИЧНАЯ СИСТЕМА""")
num_in_8_system = 0o133
print("Число записанное в (num_in_8_system) в десятичной системе равно: {}\n".format(num_in_8_system))

print("""ШЕСТНАДЦАТИРИЧНАЯ СИСТЕМА""")
num_in_16_system = 0xFA0B
print("Число записанное в (num_in_16_system) в десятичной системе равно: {}\n".format(num_in_16_system))

num_for_refactoring = int(input("Введите число для преобразования его в разных системах исчисления: "))
print("\nЧисло {} в двоичном коде выглядит как {}".format(num_for_refactoring, bin(num_for_refactoring)))
print("\nЧисло {} в восьмиричном коде выглядит как {}".format(num_for_refactoring, oct(num_for_refactoring)))
print("\nЧисло {} в шестнадцатиричном коде выглядит как {}".format(num_for_refactoring, hex(num_for_refactoring)))

