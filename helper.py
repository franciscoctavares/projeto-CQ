def get_most_likely_state(counts):
    keys = list(counts.keys())
    keys = [str(i) for i in keys]

    values = list(counts.values())
    values = [float(i) for i in values]

    counts = list(zip(keys, values))
    counts = [[keys[i], values[i]] for i in range(len(keys))]

    return keys[values.index(max(values))]

def bin_state_to_grid_coordinates(str_state):
    state = int(str_state, 2)
    return state // 3, state % 3