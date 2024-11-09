def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [3.14,'проба',False]
print_params(*values_list)
values_list_2 = [65,'число']
print_params(*values_list_2, 42)
values_dict = {'a' : 'дата','b' : 20,'c' : True}
print_params(**values_dict)
def print_params(**kwargs):
    print(kwargs)
print_params(**values_dict)
