
import random
import main

def game():
    while True:
        jekpot_position = random.randint(1,4)   
        bentuk_kotak = '[.]'
        kotak_kosong = [bentuk_kotak] * 4
        kotak = kotak_kosong.copy()
        kotak[jekpot_position - 1] = '19$'
        kotak_kosong = ' '.join(kotak_kosong)
        kotak = ' '.join(kotak)

        print(f'\nperhatikan kotak di bawah ini\n\n{kotak_kosong}')

        input_jawab = int(input("menurut anda dimana jekpot nya? (1/2/3/4)"))

        if input_jawab == jekpot_position:
            print(f'\nselamt you win\n{kotak}\n')
        else:
            print(f'\nyou lose\n{kotak}\n') 
        
        playing_again = input('mau lanjut? (y/n)')
        if playing_again == 'n':
            main.menu()

print('beres')

if __name__ == '__main__':
    game()