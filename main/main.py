with open('1.txt', 'r') as f:
    data1 = f.read()
    f.flush()

with open('3.txt', 'r', encoding='utf-8') as f1:
    data2 = f1.read()
    f1.flush()

with open('2.txt', 'r') as f:
    data3 = f.read()
    f.flush()

with open('4.txt', 'w') as f:
    f.write(f'1.txt\n1\n {data1}\n')
    f.flush()

with open('4.txt', 'a', encoding='utf-8') as f:
    f.write(f'3.txt\n8\n{data2}\n')
    f.flush()

with open('4.txt', 'a') as f:
    f.write(f'2.txt\n9\n{data3}\n')
    f.flush()