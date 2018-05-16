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
