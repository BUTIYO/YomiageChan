import time
import pygame
import tkinter
import requests

from gtts import gTTS
from tkinter import font
from mutagen.mp3 import MP3 as mp3

ngrok = "1705b31ba3ec"
count = 0
comment_list = []
label_list = []

def main():
    # tkinter settings
    # root = tkinter.Tk()
    # root.title("Anonymous Joker")
    # root.geometry("1920x1080")
    # root.update()

    text = ""
    ex_text = ""
    while True:
        ex_text = text
        text = getText()
        if text != ex_text and text != "default":
            global count
            count += 1
            print("comment number is "+str(count))
            print(text)
            # tinker描画
            # comment_list.append(text)
            # label = tkinter.Label(root, text="匿名コメント"+str(count)+": "+text, font=("",30))
            # label = tkinter.Label(root, text="コメント"+str(count)+": "+text, font=("",30))
            # label.pack(side="top", anchor=tkinter.NW)
            # label_list.append(tkinter.Label(root, text="コメント"+str(count)+": "+text, font=("",30)))
            # for label in reversed(label_list):
                # label.pack()
                # label.pack(side="top", anchor=tkinter.NW)
            # root.update()

            # 読み上げ処理
            filename = saveVoice(text)
            playVoice(filename)

        time.sleep(1)

def getText():
    # get_url_info = requests.get('https://'+ngrok+'.ngrok.io/comment')
    get_url_info = requests.get('https://anonymous-joker.herokuapp.com/comment')
    return get_url_info.text[9:]

def saveVoice(text):
    global count
    hoge = gTTS(text, lang='ja')
    filename = "voice_"+ str(count)+".mp3"
    hoge.save(filename)
    return filename

def playVoice(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    mp3_length = mp3(filename).info.length
    pygame.mixer.music.play(1)
    time.sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()
    return

if __name__ == "__main__":
    main()
