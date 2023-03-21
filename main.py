from display import *
from keys import *


def main():

    state = 'login'
    running = True

    mail_check = False
    password_check = False
    first_name_check = False
    last_name_check = False

    mail_fill = ''
    password_fill = ''
    first_name_fill = ''
    last_name_fill = ''

    active_bar = ''
    active_bar2 = ''
    active_bar3 = ''
    active_bar4 = ''

    while running:

        events = pygame.event.get()

        if state == 'login':

            display_login(mail_fill, mail_check, active_bar,
                          password_fill, password_check, active_bar2)

            for event in events:

                running = ESC_KEYDOWN(event)

                if MOUSEBUTTONDOWN(event) and INPUT_MAIL.collidepoint(pygame.mouse.get_pos()):
                    mail_check = True
                    password_check = False

                if MOUSEBUTTONDOWN(event) and INPUT_PASSWORD.collidepoint(pygame.mouse.get_pos()):
                    mail_check = False
                    password_check = True

                mail_fill = display_mail_fill(event, mail_check, mail_fill)

                password_fill = display_password_fill(
                    event, password_check, password_fill)

                if MOUSEBUTTONDOWN(event) and CREATE_NEW_ACCOUNT.collidepoint(pygame.mouse.get_pos()):
                    print('create account')
                    state = 'create_account'

                #LOGIN CLICK
                if MOUSEBUTTONDOWN(event) and LOGIN_BUTTON.collidepoint(pygame.mouse.get_pos()):
                    print('username: ', mail_fill)
                    print('password: ', password_fill)

        if state == 'create_account':

            display_register(mail_fill, mail_check, active_bar, password_fill, password_check, active_bar2,
                             first_name_fill, first_name_check, active_bar3, last_name_fill, last_name_check, active_bar4)

            for event in events:

                running = ESC_KEYDOWN(event)


                if MOUSEBUTTONDOWN(event) and INPUT_MAIL.collidepoint(pygame.mouse.get_pos()):
                    mail_check = True
                    password_check = False
                    first_name_check = False
                    last_name_check = False

                if MOUSEBUTTONDOWN(event) and INPUT_PASSWORD.collidepoint(pygame.mouse.get_pos()):
                    mail_check = False
                    password_check = True
                    first_name_check = False
                    last_name_check = False

                if MOUSEBUTTONDOWN(event) and firstname_rect.collidepoint(pygame.mouse.get_pos()):
                    mail_check = False
                    password_check = False
                    first_name_check = True
                    last_name_check = False

                if MOUSEBUTTONDOWN(event) and lastname_rect.collidepoint(pygame.mouse.get_pos()):
                    mail_check = False
                    password_check = False
                    first_name_check = False
                    last_name_check = True
                
                #REGISTER CLICK
                if MOUSEBUTTONDOWN(event) and REGISTER_BUTTON.collidepoint(pygame.mouse.get_pos()):
                    print(
                        f'username: {mail_fill} password: {password_fill} first name: {first_name_fill} last name: {last_name_fill}'
                    )

                if MOUSEBUTTONDOWN(event) and RETURN_BUTTON.collidepoint(pygame.mouse.get_pos()):
                    print('return')
                    state = 'login'

                mail_fill = display_mail_fill(event, mail_check, mail_fill)
                password_fill = display_password_fill(
                    event, password_check, password_fill)
                first_name_fill = display_first_name_fill(
                    event, first_name_check, first_name_fill)
                last_name_fill = display_last_name_fill(
                    event, last_name_check, last_name_fill)

        if state == 'home':

            for event in events:
                running = ESC_KEYDOWN(event)

        pygame.display.update()


if __name__ == '__main__':
    main()
