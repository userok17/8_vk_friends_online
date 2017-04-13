import vk
from getpass import getpass
APP_ID = 123456  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    login = input('Введите логин: ')
    return login


def get_user_password():
    password = getpass(prompt='Введите пароль: ')
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    list_id = api.friends.getOnline()
    friends_online = api.users.get(user_ids=list_id)
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
