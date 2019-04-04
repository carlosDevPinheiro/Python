a = raw_input('Digite o valor hexadecimal: ')
length = len(a)
ab = bin(int(a, 16))[2:]
while len(ab)<(length * 4):
    ab = '0' + ab
print ab