a = int(input("Введите первое двузначное число (AB): "))
b = int(input("Введите второе двузначное число (AB): "))
result = a * b
result_str = str(result)

if len(result_str) == 2:
    result_str = "0" + result_str

print(result_str)




