from password_state_machine import PasswordStateMachine
from state import State


def main():
    letters = list('qwertyuiopasdfghjklzxcvbnm')
    digits = list('1234567890')
    special_chars = list('!@#$%^&*()')
    alphabet = letters + digits + special_chars

    end_state = State('q10', [(alphabet, 'self')])

    q2 = State('q2', [
        (letters + digits, 'self'),
        (special_chars, end_state)
    ])
    q3 = State('q3', [
        (letters + special_chars, 'self'),
        (digits, end_state)
    ])
    q1 = State('q1', [
        (letters, 'self'),
        (digits, q2),
        (special_chars, q3)
    ])

    q5 = State('q5', [
        (digits + special_chars, 'self'),
        (letters, end_state)
    ])
    q4 = State('q4', [
        (digits, 'self'),
        (letters, q2),
        (special_chars, q5)
    ])

    q6 = State('q6', [
        (special_chars, 'self'),
        (letters, q3),
        (digits, q5)
    ])

    start_state = State('q0', [
        (letters, q1),
        (digits, q4),
        (special_chars, q6)
    ])

    password = input('Введите пароль: ')
    password_state_machine = PasswordStateMachine(start_state, end_state)
    print('Пароль ' +
          ('' if password_state_machine.test(password) else 'не') +
          'корректный')


if __name__ == '__main__':
    main()
