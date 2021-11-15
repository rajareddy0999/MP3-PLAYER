import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pygame

root = tk.Tk()
root.title('MUSIC PLAYER')
root.geometry('500x320')
root.config(bg='blue')
pygame.mixer.init()

song_list = tk.Listbox(root, width=60, bg='black', fg='white')
song_list.pack(pady=20)

def add_song():
    songs = filedialog.askopenfilenames(initialdir='C:/Users/puneeth_wel/OneDrive/Desktop/New folder/music/',title='Add Music',filetypes=(('mp3 Files', '*.mp3'),))
    for song in songs:
      songs = song.replace('C:/Users/puneeth_wel/OneDrive/Desktop/New folder/music/','')
      song_list.insert(END,songs)

def play_song():   
    song = song_list.get(ACTIVE)
    song = f'C:/Users/puneeth_wel/OneDrive/Desktop/New folder/music/{song}' 
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop_song():
    pygame.mixer.music.stop()   
    song_list.select_clear(ACTIVE) 

global paused
paused = False
def pause_song():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def play_next_song():
    next_song = song_list.curselection()
    next_song = next_song[0]+1
    song = song_list.get(next_song)
    song = f'C:/Users/puneeth_wel/OneDrive/Desktop/New folder/music/{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_list.selection_clear(0,END)
    song_list.selection_set(next_song,last=None)

def play_previous_song():
    next_song = song_list.curselection()
    next_song = next_song[0]-1
    song = song_list.get(next_song)
    song = f'C:/Users/puneeth_wel/OneDrive/Desktop/New folder/music/{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_list.selection_clear(0,END)
    song_list.selection_set(next_song,last=None)
   
def set_vol(val):
    volume = int(val) / 100
    pygame.mixer.music.set_volume(volume)



frame = tk.Frame(root,bg='white')
frame.pack()
play_button = tk.Button(frame,bg='pink',fg='black',text='play',padx=10,pady=10,command=play_song)
pause_button = tk.Button(frame,text='pause',bg='yellow',fg='black',padx=10,pady=10,command=pause_song)
stop_button = tk.Button(frame,text='stop',bg='red',fg='black',padx=10,pady=10,command=stop_song)
forward_button = tk.Button(frame,text='next',bg='black',fg='white',padx=10,pady=10,command=play_next_song)
backward_button = tk.Button(frame,text='prev',bg='black',fg='white',padx=10,pady=10,command=play_previous_song)

#volume control
scale = Scale(root,from_=100,to=0,orient=VERTICAL,command= set_vol,bg='green',fg='black')
scale.set(50)
scale.pack(side=RIGHT,padx=10,)
scale.place(x=445,y=40)

play_button.pack(side=LEFT,padx=5)
pause_button.pack(side=LEFT,padx=5)
stop_button.pack(side=LEFT,padx=5)
forward_button.pack(side=LEFT,padx=5)  
backward_button.pack(side=LEFT,padx=5) 

add_song_btn = tk.Button(root,text='Add Songs',padx=10,pady=3,command=add_song,bg='orange',fg='black')
add_song_btn.pack(pady=20)


root.mainloop()