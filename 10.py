N = int(input("Введите количество кубиков N (1 <= N <= 100): ")))
counter = 0
first_fl = N//2
second_fl = N - first_fl -1
third_fl = N - first_fl - second_fl
first_fl_pos = first_fl + 1
second_fl_pos = N - first_fl_pos - 1
third_fl_pos = N - first_fl_pos - second_fl_pos - 1
for i in range(1, N):
    if N//2