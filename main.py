from libs import welcome_message, exit
from games import jeckpot
from tools import warung

def menu():
    user_option = input('\nDAR...\n\n1. Games\n2. warung\n3. keluar')
    if user_option == '1':
     jeckpot.game()
    elif user_option == '2':
       warung.start()
    elif user_option == '3':
       exit()
    else:
       print('jan aneh2 ')

def main():
    welcome_message()
    menu()

if __name__ == '__main__':
    main()