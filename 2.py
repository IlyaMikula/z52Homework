my_dict = {'a': 400, 'b': 58700, 'c': -560, 'd': 'one', 'e': 20000 , 'f': 2000, 'd': 400}
val = sorted(my_dict, key=my_dict.get)
print(val[3:])