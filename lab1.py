# Вхідні дані ------
default_input_sample = [18, 27, 20, 18, 22, 20, 17, 24, 28, 23, 25, 22, 14, 24, 18, 33, 17, 19, 28, 23]
default_y = 0.57
default_working_probability_time = 1210
default_failure_intensity_time = 29
# Вхідні дані ------


def calc_p_t(wpt, inp_sample):
    v_t = 0
    for ti in inp_sample:
        if ti <= wpt:
            v_t += 1

    q_t = v_t / len(inp_sample)
    p_t = 1 - q_t
    return p_t


try:
    if input("Введіть 1 для стандартних даних, 0 для свого вводу: ") == '0':
        default_y = float(input("Введіть Y: "))
        default_working_probability_time = int(input("Введіть час до безвідмовної роботи: "))
        default_failure_intensity_time = int(input("Введіть час для інтенсивності відмов: "))
except ValueError:
    print("Помилка даних")
    exit()

if len(default_input_sample) == 0 or not 0 <= default_y < 1:
    print("Помилка даних")
    exit()

default_input_sample = sorted(default_input_sample)
sample_length = len(default_input_sample)
T_avg = sum(default_input_sample) / sample_length
print(f"Середній наробіток до відмови Tср =", T_avg)
T_max = max(default_input_sample)

P_t = calc_p_t(default_working_probability_time, default_input_sample)
print(f"Ймовірність безвідмовної роботи на час {default_working_probability_time} годин =", round(P_t, 3))

h = T_max / 10
statistic_densities = []
intervals = []
for i in range(1, 11):
    Ni = 0
    for t in default_input_sample:
        if h * (i - 1) < t <= h * i:
            Ni += 1
    statistic_densities.append(Ni / (10 * h))
    intervals.append(h * i)
print(statistic_densities)

pts = []
for t in range(len(intervals)):
    pts.append(round(calc_p_t(intervals[t], default_input_sample), 3))

print("Ймовірності для інтервалів =", pts)
failure_intensity = 0

for i in intervals:
    if i - h < default_failure_intensity_time <= i:
        failure_intensity = statistic_densities[intervals.index(i)] / calc_p_t(default_failure_intensity_time,
                                                                               default_input_sample)

print(f"Інтенсивність відмов на час {default_failure_intensity_time} годин =", round(failure_intensity, 6))

prev_p = 1
curr_p = 0
for p in pts:
    curr_p = p
    if prev_p > default_y >= p:
        break
    prev_p = p

d_t = (prev_p - default_y) / (prev_p - curr_p)
T_y = prev_p + h * d_t
print(f"{round(default_y * 100, 1)}%-відсотковий наробіток на відмову Tγ =", round(T_y, 3))
