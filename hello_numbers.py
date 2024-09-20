print('*** ints are implicitly converted to floats when used together ***')
print(1 + 9)
print(1 + 9.0)

print('\n*** viewing types ***')
print(type(float(99)))

print('\n*** int divisions always produce a floating result in Python 3 ***')
print(10.0 / 2.0)
print(10 / 2)
print(9 / 2)
print(99 / 100)

print("\n*** True is 1 ***")
print("True + 5 = ", True + 5) # 6
print("True - 5 = ", True - 5) # -4
print("True * 5 = ", True * 5) # 5
print("True / 5 = ", True / 5) # 0.2

print("\n*** False is 0 ***")
print("False + 5 = ", False + 5) # 5
print("False - 5 = ", False - 5) # -5
print("False * 5 = ", False * 5) # 0
print("False / 5 = ", False / 5) # 0.0
