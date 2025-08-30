from libs import welcome_message, exit_program
from games import jeckpot
from tools import keuangan

def menu():
    user_option = input('\nDAR...\n\n1. Games\n2. Keuangan\n3. keluar')
    if user_option == '1':
     jeckpot.game()
    elif user_option == '2':
       keuangan.start()
    elif user_option == '3':
       exit_program()
    else:
       print('jan aneh2 ')

def main():
    welcome_message()
    menu()

if __name__ == '__main__':
    main()
