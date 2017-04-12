import vk
from getpass import getpass
from pprint import pprint
APP_ID = 5980137  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    login = input('Введите логин: ')
    return login


def get_user_password():
    password = getpass(prompt='Введите пароль: ')
    return password

def filter_online_friends(user):
    if user['online']:
        return True

def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    friends = api.friends.get(fields=['nickname', 'online'])
    friends_online = filter(filter_online_friends, friends)
    return friends_online


def output_friends_to_console(friends_online):
    print()
    for friend in friends_online:
        print(friend['last_name'], friend['first_name'])

if __name__ == '__main__':
    print('Программа. Список друзей которые сейчас в сети.\n')
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
