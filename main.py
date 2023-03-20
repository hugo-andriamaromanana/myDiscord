from display import *
from keys import *


def main():
    running = True
    mail_check = False
    password_check = False
    mail_fill = ''
    password_fill = ''
    active_bar = ''
    while running:
        display_login(mail_fill, mail_check, active_bar,
                      password_fill, password_check, active_bar2)
        events = pygame.event.get()
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
        pygame.display.update()


if __name__ == '__main__':
    main()
