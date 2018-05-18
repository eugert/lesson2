# Сравнение строк
# Написать функцию, которая принимает на вход две строки.
# Если строки одинаковые, возвращает 1.
# Если строки разные и первая длиннее, возвращает 2.
# Если строки разные и вторая строка 'learn', возвращает 3 (если не выполнено услровие 2)

def compare_str (p_str1, p_str2):
    p_str1 = str(p_str1)
    p_str2 = str(p_str2)

    if p_str1 == p_str2:
        v_result = 1
    elif len(p_str1) > len(p_str2):
        v_result = 2
    elif p_str2 == 'learn':
        v_result = 3

    return v_result


print(compare_str('python', 'python'))
print(compare_str('python', 'learn'))
print(compare_str('len', 'learn'))
