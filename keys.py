import pygame
from pygame.locals import *


def ESC_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        return False
    return True


def MOUSEBUTTONDOWN(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        return True


def SPACEBAR_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        return True


def BACKSPACE_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
        return True


def RETURN_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        return True


def TAB_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
        return True
