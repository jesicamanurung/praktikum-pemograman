import os
os.system('cls')

a = True

while a:
    jawab = input('Apakah ingin lanjutkan? (y/n)')
    if jawab == 'y':

        os.system('cls')
        print('Selamat Datang Lagi')

    elif jawab == 'n':

        print('Samapai Ketemu Lagi :D')
        a = False

    else:
        os.system('cls')
        print('Jangan Aneh-aneh deh:.)')
        a = False