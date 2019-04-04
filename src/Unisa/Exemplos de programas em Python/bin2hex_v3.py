a=input('Digit your binary value: ')
b=hex(int(a,2))
c = b.split('0x')
print('Hexadecimal value: ', c[1])