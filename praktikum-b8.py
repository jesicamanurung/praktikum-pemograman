import os
os.system('cls')

import os
os.system('clear')

pwd_benar = 'si23b'
a = True
i = 0
limit = 3
while a:
    i += 1
    pwd = input('Masukkan Password: ')
    if pwd == pwd_benar:
        print('Selamat Anda Login!')
        a = False
    else:
        print('Password Salah!')
        if i == limit:
            a = False
            print('Anda kehabisan kesempatan')
        else:
            print(f'Kesempatan anda tersisa {limit-i} kali')
        