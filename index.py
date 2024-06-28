from menu_login import menu_login
from menu_principal import menu_principal

while True:
    try:
        menu_login()
        menu_principal()
    except:
        print('Até breve! ')
        break