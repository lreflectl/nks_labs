from itertools import product


def optimize_system(the_system):
    for i in range(len(the_system) - 1):
        the_system[i] = list(filter(lambda x: x > i, the_system[i]))
    return the_system


def get_index_combinations(the_system):
    system_indexes = []
    for i in the_system[:-1]:
        system_indexes.append([p for p in range(len(i))])
    params = system_indexes
    return list(product(*params))


def get_combinations(the_index_combinations):
    the_combinations = []

    for c in range(len(the_index_combinations)):
        combo = []
        current_state = system[0]
        current_index = 0

        while current_state != 'end':
            current_state = system[current_state[the_index_combinations[c][current_index]]]
            current_index = system.index(current_state)
            combo.append(current_index)
        the_combinations.append(tuple(combo[:-1]))

    return list(set(the_combinations))


def get_working_states(the_system, the_combinations):
    all_possible_system_states = list(product([1, 0], repeat=len(the_system) - 2))
    the_working_states = []
    for s in all_possible_system_states:
        for c in the_combinations:
            working_state = True
            for e in c:
                if s[e - 1] == 0:
                    working_state = False
                    break
            if working_state:
                the_working_states.append(s)
                break
    return the_working_states


def get_p_states(the_working_states, the_probabilities):
    p_states = []
    for state in the_working_states:
        p_state = 1
        for i in range(len(state)):
            if state[i]:
                p_state *= the_probabilities[i]
            elif not state[i]:
                p_state *= 1 - the_probabilities[i]
        p_states.append(round(p_state, 6))
    return p_states


if __name__ == '__main__':
    # input data, example
    probabilities1 = [.5, .6, .7, .8, .85, .9, .92, .94]
    system1 = [[1], [0, 2, 3], [1, 3, 4, 5], [1, 2, 4, 6, 8], [2, 3, 5, 6, 8],
               [2, 4, 6, 7], [3, 4, 5, 7, 8], [5, 6, 8, 9], [3, 4, 6, 7, 9], 'end']

    # input data, 24 variant
    probabilities = [.91, .16, .03, .91, .06, .44, .08]
    system = [[1, 2], [0, 2, 3, 4], [0, 1, 3, 5, 7], [1, 2, 4, 5, 7],
              [1, 3, 5, 6], [2, 3, 4, 6, 7], [4, 5, 7, 8], [2, 3, 5, 6, 8], 'end']

    try:
        inp = input('Введіть 1 для стандартних даних, 0 для ручного вводу: ')
        if int(inp) == 1:
            print('Вхідні дані 24-го варіанту.')
            pass
        elif int(inp) == 0:
            print(f'В заданій системі {len(system)-2} елементів')
            prob_input = input('Введіть ймовірності для них через пробіл: ')
            prob_input = prob_input.split()
            float_prob = []
            for p in range(len(prob_input)):
                float_prob.append(float(prob_input[p]))
                if not 0 < float_prob[p] < 1:
                    print('Некоректно задані ймовірності')
                    exit()
            probabilities = float_prob
        else:
            print('Некоректний ввід')
            exit()
    except ValueError:
        print('Помилка даних')
        exit()

    if len(probabilities) != len(system) - 2 or len(probabilities) == 0 or len(system) == 0:
        print('Невірні вхідні дані')
        exit()

    system = optimize_system(system)
    index_combinations = get_index_combinations(system)
    combinations = get_combinations(index_combinations)
    working_states = get_working_states(system, combinations)
    print("Всього працездатних станів знайдено:", len(working_states))
    P_states = get_p_states(working_states, probabilities)
    print("Ймовірність безвідмовної роботи системи P system =", round(sum(P_states), 6))
