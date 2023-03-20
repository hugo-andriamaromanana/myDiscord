from pygame.locals import *
import pygame

mail_fill = ''
active_bar = ''
password_fill = ''
active_bar2 = ''


def display_mail_fill(event, mail_check, mail_fill):
    if mail_check:
        AUTHORIZED_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@.-_0123456789'
        if event.type == pygame.KEYDOWN:
            if event.key == K_BACKSPACE and len(mail_fill) > 0:
                mail_fill = mail_fill[:-1]
            if event.unicode in AUTHORIZED_LETTERS:
                mail_fill += event.unicode
    return mail_fill


def display_password_fill(event, password_check, password_fill):
    if password_check:
        AUTHORIZED_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@.-_0123456789'
        if event.type == pygame.KEYDOWN:
            if event.key == K_BACKSPACE and len(password_fill) > 0:
                password_fill = password_fill[:-1]
            if event.unicode in AUTHORIZED_LETTERS:
                password_fill += event.unicode
    return password_fill
