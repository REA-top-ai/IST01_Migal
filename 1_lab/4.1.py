s = 'abcdefghijklmn'
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(''.join([s[i] for i in range(0, len(s), 2)]))
print(''.join([s[i] for i in range(1, len(s), 2)]))
print(''.join(reversed(list(s))))
print(''.join([s[i] for i in range(len(s)-1, -1, -2)]))
print(len(s))




