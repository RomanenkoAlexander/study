def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
#print_params(b = 25)
#print_params(c = [1,2,3])

values_list = [25, "Test", True]
values_dict = {'a':'Ivan', 'b': False, 'c': 12}
values_list_2 = [54.32, 'Строка']
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)



