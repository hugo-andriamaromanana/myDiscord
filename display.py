import os
from colors import COLORS
from functions import *

pygame.font.init()

THEME = {
    'BACKGROUND': COLORS['DISCORD_GREY'],
    'BUTTON': COLORS['DISCORD_BLUE'],
    'FONT': {
        'ITALIC_SMOL': pygame.font.Font(os.path.join('fonts', 'discord_smol.otf'), 12),
        'ITALIC_DEFAULT': pygame.font.Font(os.path.join('fonts', 'discord_smol.otf'), 16),
        'ITALIC_BIG': pygame.font.Font(os.path.join('fonts', 'discord_smol.otf'), 24),
        'SMOL': pygame.font.Font(os.path.join('fonts', 'discord.otf'), 12),
        'DEFAULT': pygame.font.Font(os.path.join('fonts', 'discord.otf'), 16),
        'BIG': pygame.font.Font(os.path.join('fonts', 'discord.otf'), 24),

    },
}

screen = pygame.display.set_mode((980, 720))
DISPLAYSURF = pygame.display.set_mode((980, 720))
pygame.display.set_caption('Discord')

LOGIN_SURF = pygame.Surface((700, 400))
FONTS = THEME['FONT']

INPUT_MAIL = pygame.Rect(250, 300, 500, 40)
INPUT_PASSWORD = pygame.Rect(250, 370, 500, 40)
LOGIN_BUTTON = pygame.Rect(250, 430, 500, 40)
CREATE_NEW_ACCOUNT = pygame.Rect(250, 485, 120, 20)


def display_login(mail_fill, check, active_bar, password_fill, check2, active_bar2):
    DISPLAYSURF.fill(COLORS['LIGHT_BLUE'])
    DISPLAYSURF.blit(LOGIN_SURF, (150, 150))
    LOGIN_SURF.fill(COLORS['DISCORD_GREY'])
    DISPLAYSURF.blit(FONTS['BIG'].render(
        'Welcome back!', True, COLORS['WHITE']), (410, 180))
    DISPLAYSURF.blit(FONTS['SMOL'].render(
        'We are so excited to see you again!', True, COLORS['WHITE']), (400, 230))
    DISPLAYSURF.blit(FONTS['SMOL'].render(
        'Email', True, COLORS['WHITE']), (250, 280))
    DISPLAYSURF.blit(FONTS['SMOL'].render(
        'Password', True, COLORS['WHITE']), (250, 350))

    pygame.draw.rect(DISPLAYSURF, COLORS['DISCORD_DARK_GREY'], INPUT_MAIL)
    pygame.draw.rect(DISPLAYSURF, COLORS['DISCORD_DARK_GREY'], INPUT_PASSWORD)
    pygame.draw.rect(DISPLAYSURF, COLORS['DISCORD_BLUE'], LOGIN_BUTTON)

    pygame.draw.rect(DISPLAYSURF, COLORS['DISCORD_GREY'], CREATE_NEW_ACCOUNT)
    DISPLAYSURF.blit(FONTS['SMOL'].render(
        'Create an account', True, COLORS['CLEAR_BLUE']), (250, 490))

    DISPLAYSURF.blit(FONTS['BIG'].render(
        'Log in', True, COLORS['WHITE']), (450, 440))
    if check:
        active_bar = '|'
    if not check:
        active_bar = ''
    if check2:
        active_bar2 = '|'
    if not check2:
        active_bar2 = ''
    DISPLAYSURF.blit(FONTS['ITALIC_DEFAULT'].render(
        mail_fill+active_bar, True, COLORS['WHITE']), (INPUT_MAIL.x+10, INPUT_MAIL.y+10))
    DISPLAYSURF.blit(FONTS['ITALIC_DEFAULT'].render(
        password_fill+active_bar2, True, COLORS['WHITE']), (INPUT_PASSWORD.x+10, INPUT_PASSWORD.y+10))


first_name = pygame.Rect(250, 300, 500, 40)
last_name = pygame.Rect(250, 370, 500, 40)

REGISTER_SURF = pygame.Surface((700, 600))

lastname_rect = pygame.Rect(250, 510, 500, 40)
firstname_rect = pygame.Rect(250, 440, 500, 40)

REGISTER_BUTTON = pygame.Rect(250, 580, 500, 40)
RETURN_BUTTON = pygame.Rect(200, 100, 120, 40)


def display_register(mail_fill, check, active_bar, password_fill, check2, active_bar2, first_name_fill, check3, active_bar3, last_name_fill, check4, active_bar4):
    DISPLAYSURF.fill(COLORS['LIGHT_BLUE'])
    DISPLAYSURF.blit(REGISTER_SURF, (150, 50))
    REGISTER_SURF.fill(COLORS['DISCORD_GREY'])
    DISPLAYSURF.blit(FONTS['BIG'].render(
        'Create an account', True, COLORS['WHITE']), (390, 200))
    DISPLAYSURF.blit(FONTS['SMOL'].render(
        'Email', True, COLORS['WHITE']), (250, 280))
    DISPLAYSURF.blit(FONTS['SMOL'].render(
        'Password', True, COLORS['WHITE']), (250, 350))
    DISPLAYSURF.blit(FONTS['SMOL'].render(
        'First name', True, COLORS['WHITE']), (250, 420))
    DISPLAYSURF.blit(FONTS['SMOL'].render(
        'Last name', True, COLORS['WHITE']), (250, 490))

    pygame.draw.rect(DISPLAYSURF, COLORS['DISCORD_DARK_GREY'], INPUT_MAIL)
    pygame.draw.rect(DISPLAYSURF, COLORS['DISCORD_DARK_GREY'], INPUT_PASSWORD)
    pygame.draw.rect(DISPLAYSURF, COLORS['DISCORD_DARK_GREY'], firstname_rect)
    pygame.draw.rect(DISPLAYSURF, COLORS['DISCORD_DARK_GREY'], lastname_rect)
    pygame.draw.rect(DISPLAYSURF, COLORS['DISCORD_GREY'], RETURN_BUTTON)

    DISPLAYSURF.blit(FONTS['BIG'].render(
        '<--', True, COLORS['WHITE']), (RETURN_BUTTON.x+30, RETURN_BUTTON.y+10))

    pygame.draw.rect(DISPLAYSURF, COLORS['DISCORD_BLUE'], REGISTER_BUTTON)
    DISPLAYSURF.blit(FONTS['BIG'].render(
        'Register', True, COLORS['WHITE']), (REGISTER_BUTTON.x+200, REGISTER_BUTTON.y+10))

    if check:
        active_bar = '|'
    if not check:
        active_bar = ''
    if check2:
        active_bar2 = '|'
    if not check2:
        active_bar2 = ''
    if check3:
        active_bar3 = '|'
    if not check3:
        active_bar3 = ''
    if check4:
        active_bar4 = '|'
    if not check4:
        active_bar4 = ''
    DISPLAYSURF.blit(FONTS['ITALIC_DEFAULT'].render(
        mail_fill+active_bar, True, COLORS['WHITE']), (INPUT_MAIL.x+10, INPUT_MAIL.y+10))
    DISPLAYSURF.blit(FONTS['ITALIC_DEFAULT'].render(
        password_fill+active_bar2, True, COLORS['WHITE']), (INPUT_PASSWORD.x+10, INPUT_PASSWORD.y+10))
    DISPLAYSURF.blit(FONTS['ITALIC_DEFAULT'].render(
        first_name_fill+active_bar3, True, COLORS['WHITE']), (firstname_rect.x+10, firstname_rect.y+10))
    DISPLAYSURF.blit(FONTS['ITALIC_DEFAULT'].render(
        last_name_fill+active_bar4, True, COLORS['WHITE']), (lastname_rect.x+10, lastname_rect.y+10))
