data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
k = 0
def calculate_structure_sum(*val):
    global k
    for i in range(len(val)):
        if isinstance(val[i], int):
            k += val[i]
        elif isinstance(val[i], str):
            k += len(val[i])
        elif isinstance(val[i], dict):
            key = list(dict.keys(val[i]))
            calculate_structure_sum(*key)
            value = list(dict.values(val[i]))
            calculate_structure_sum(*value)
        else:
            calculate_structure_sum(*val[i])

    return k;
    #print(k)

result = calculate_structure_sum(*data_structure)
print(result)


