import random

first_num = N//100000
second_num = (N//10000)%10
fhird_num = (N//1000)%10
fourth_num = (N//100)%10
fith_num = (N//10)%10
six_num = N%10
while not first_num == six_num and second_num == fith_num and fhird_num == fourth_num:
    N = random.randint(100000, 999999)

