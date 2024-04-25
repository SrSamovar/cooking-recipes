with open('1.txt', 'r', encoding='utf-8') as f:
    data1 = f.read()
    f.flush()

with open('2.txt', 'r', encoding='utf-8') as f:
    data2 = f.read()
    f.flush()

with open('3.txt', 'r', encoding='utf-8') as f:
    data3 = f.read()
    f.flush()


def count_lines_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        line_count = sum(1 for line in f)
    return line_count



len1 = count_lines_in_file('1.txt')
len2 = count_lines_in_file('2.txt')
len3 = count_lines_in_file('3.txt')



if len(data1) < len(data2) and len(data1) < len(data3):
    with open('4.txt', 'wt', encoding='utf-8') as f:
        f.write(f'1.txt\n{len1}\n{data1}\n')
        f.flush()
    if len(data2) < len(data3):
        with open('4.txt', 'at', encoding='utf-8') as f:
            f.write(f'2.txt\n{len2}\n{data2}\n')
            f.flush()
        with open('4.txt', 'at', encoding='utf8') as f:
            f.write(f'3.txt\n{len3}\n{data3}\n')
            f.flush()
    else:
        with open('4.txt', 'at', encoding='utf-8') as f:
            f.write(f'3.txt\n{len3}\n{data3}\n')
            f.flush()
        with open('4.txt', 'at', encoding='utf8') as f:
            f.write(f'2.txt\n{len2}\n{data2}\n')
            f.flush()
elif len(data2) < len(data1) and len(data2) < len(data3):
    with open('4.txt', 'wt', encoding='utf8') as f:
        f.write(f'2.txt\n{len2}\n{data2}\n')
        f.flush()
    if len(data1) < len(data3):
        with open('4.txt', 'at', encoding='utf-8') as f:
            f.write(f'1.txt\n{len1}\n{data1}\n')
            f.flush()
        with open('4.txt', 'at', encoding='utf8') as f:
            f.write(f'3.txt\n{len3}\n{data3}\n')
            f.flush()
    else:
        with open('4.txt', 'at', encoding='utf-8') as f:
            f.write(f'3.txt\n{len3}\n{data3}\n')
            f.flush()
        with open('4.txt', 'at', encoding='utf8') as f:
            f.write(f'1.txt\n{len1}\n{data1}\n')
            f.flush()
elif len(data3) < len(data1) and len(data3) < len(data2):
    with open('4.txt', 'wt', encoding='utf8') as f:
        f.write(f'3.txt\n{len3}\n{data3}\n')
        f.flush()
    if len(data1) < len(data2):
        with open('4.txt', 'at', encoding='utf-8') as f:
            f.write(f'1.txt\n{len1}\n{data1}\n')
            f.flush()
        with open('4.txt', 'at', encoding='utf8') as f:
            f.write(f'2.txt\n{len2}\n{data2}\n')
            f.flush()
    else:
        with open('4.txt', 'at', encoding='utf-8') as f:
            f.write(f'2.txt\n{len2}\n{data2}\n')
            f.flush()
        with open('4.txt', 'at', encoding='utf8') as f:
            f.write(f'1.txt\n{len1}\n{data1}\n')
            f.flush()