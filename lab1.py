# Вхідні дані ------
default_input_sample = [123, 332, 916, 220, 412, 0, 127, 208, 635, 91,
                        477, 42, 121, 76, 643, 357, 70, 709, 666, 91,
                        70, 1166, 225, 555, 382, 116, 85, 1328, 133,
                        75, 377, 315, 72, 961, 43, 197, 635, 526, 20,
                        20, 1513, 93, 142, 150, 441, 634, 821, 1014,
                        1145, 107, 125, 856, 522, 175, 78, 2794, 47,
                        2996, 198, 1838, 149, 1476, 78, 715, 437, 467,
                        455, 91, 1052, 189, 523, 190, 2364, 14, 202,
                        2773, 1111, 45, 521, 161, 394, 825, 47, 300,
                        479, 36, 1017, 1125, 1062, 291, 295, 714,
                        1151, 331, 890, 38, 1814, 1077, 309, 1005]
default_y = 0.57
default_working_probability_time = 1210
default_failure_intensity_time = 1375
# Вхідні дані ------


def calc_p_t(wpt, inp_sample):
    v_t = 0
    for ti in inp_sample:
        if ti <= wpt:
            v_t += 1

    q_t = v_t / len(inp_sample)
    p_t = 1 - q_t
    return p_t


default_input_sample = sorted(default_input_sample)
sample_length = len(default_input_sample)
T_avg = sum(default_input_sample)/sample_length
print(f"Середній наробіток до відмови Tср =", T_avg)
T_max = max(default_input_sample)

P_t = calc_p_t(default_working_probability_time, default_input_sample)
print(f"Ймовірність безвідмовної роботи на час {default_working_probability_time} годин =", round(P_t, 3))

p_ts = []
for i in range(sample_length):
    p_ts.append(calc_p_t(i, default_input_sample))

prev_p = 0
curr_p = 0
for p in p_ts:
    if prev_p > default_y > p:
        curr_p = p
        break
    prev_p = p

interval = T_max/10

d_t = (prev_p - default_y)/(prev_p - curr_p)
T_y = prev_p + interval*d_t
print(f"γ-відсотковий наробіток на відмову Tγ =", round(T_y, 3))

statistic_densities = []
for i in range(1, 11):
    Ni = 0
    for t in default_input_sample:
        if interval*(i - 1) < t < interval*i:
            Ni += 1
    statistic_densities.append(Ni/(sample_length*interval))

P_t_failure = calc_p_t(default_failure_intensity_time, default_input_sample)
f_t_i = 0
for d in range(len(statistic_densities)):
    if default_failure_intensity_time < d*interval:
        f_t_i = d
failure_intensity = statistic_densities[f_t_i]/P_t_failure
print(f"Інтенсивність відмов на час {default_failure_intensity_time} годин =", round(failure_intensity, 6))
