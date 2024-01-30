from tkinter import *
from random import randint
from snake import *
from ttt import *
from pong import *
import os
import pygame


def stop_music():
    pygame.mixer.music.stop()


def close():
    os._exit(0)


def play_music():
    pygame.mixer.music.load(r'assets/menu_music.mp3')
    pygame.mixer.music.play(-1)


def launch_game(game_function, on_exit_callback):
    stop_music()
    on_exit_callback()
    game_function()


def create_button(root, text, command, x, y):
    button = Button(root, text=text, font="Helvetica 15", command=command)
    window = main_cvs.create_window(x, y, anchor='nw', window=button)
    return button, window


def game_exit_callback():
    play_music()


pygame.mixer.init()

root = Tk()
root.geometry("701x527")
root.title("PyGameLauncher - By Gorakh")
root.iconbitmap("assets/icon_img.ico")

arr = [r'assets/bgmain1.png', r'assets/bgmain2.png',
       r'assets/bgmain3.png', r'assets/bgmain4.png']
bg_img = PhotoImage(file=arr[randint(0, 3)])

main_cvs = Canvas(root, width=701, height=527)
main_cvs.pack(fill='both', expand=True)
main_cvs.create_image((0, 0), image=bg_img, anchor='nw')

play_music()

buttons = [
    ("Snake Game", lambda: launch_game(snakest, game_exit_callback), 300, 243),
    ("Pong", lambda: launch_game(pongst, game_exit_callback), 330, 293),
    ("Tic Tac Toe", lambda: launch_game(play, game_exit_callback), 300, 343),
    ("Quit", close, 330, 393)
]

for button_info in buttons:
    create_button(root, *button_info)

root.mainloop()
