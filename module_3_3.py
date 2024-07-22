#Самостоятельная работа по уроку "Распаковка позиционных параметров".
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [1, True, "str"]
values_dict = {"a" : 5, "b" : False, "c" : "string"}
values_list_2 = [54.32, 'Строка' ]

# 1.Функция с параметрами по умолчанию:
print_params()
print_params(b=25)
print_params(c = [1,2,3])

# 2.Распаковка параметров:
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
print_params(*values_list_2, 42)
