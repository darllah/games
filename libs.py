import socket
from time import sleep

PC_NAME = socket.gethostname()

def welcome_message():
    bintang = '*' * (len(PC_NAME) + 6)
    print(f'{bintang}\n** {PC_NAME} **\n{bintang}')

def exit():
    print('program berhenti')
    sleep(1)
    print('3...')
    sleep(1)
    print('2....')
    sleep(1)
    print('1....')
    sleep(1)
    print('Selesai...')

if __name__ == '__main__':
     welcome_message()
     exit()