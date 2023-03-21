from pygame.locals import *
import pygame

mail_fill = ''
password_fill = ''
first_name_fill = ''
last_name_fill = ''

active_bar = ''
active_bar2 = ''
active_bar3 = ''
active_bar4 = ''



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

def display_first_name_fill(event, first_name_check, first_name_fill):
    if first_name_check:
        AUTHORIZED_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@.-_0123456789'
        if event.type == pygame.KEYDOWN:
            if event.key == K_BACKSPACE and len(first_name_fill) > 0:
                first_name_fill = first_name_fill[:-1]
            if event.unicode in AUTHORIZED_LETTERS:
                first_name_fill += event.unicode
    return first_name_fill

def display_last_name_fill(event, last_name_check, last_name_fill):
    if last_name_check:
        AUTHORIZED_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@.-_0123456789'
        if event.type == pygame.KEYDOWN:
            if event.key == K_BACKSPACE and len(last_name_fill) > 0:
                last_name_fill = last_name_fill[:-1]
            if event.unicode in AUTHORIZED_LETTERS:
                last_name_fill += event.unicode
    return last_name_fill

