for i in range(10):
    if i == 5:
        continue
    print(f'i={i}', end='\t')

print('\n')

for i in range(3):
    PassWord = input('PassWord:')
    if PassWord == '666':
        break
    else:  # else属于if判断
        print('')
else:  # else 属于for循环，在for循环结束后执行，如果for循环中途break跳出循环则不执行
    print('frieze')
