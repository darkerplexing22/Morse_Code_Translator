import tkinter
from tkinter import IntVar, END, DISABLED, NORMAL
from pygame import mixer
mixer.init()


#Define window
root = tkinter.Tk()
root.title('Morse Code Translator')
root.geometry('902x600+385+154')
root.config(background="#432242")
root.resizable(0,0)

#Define fonts colors
button_font  = ('Arial', 10)
root_color   = "white"
frame_color  = "#c48cc2"
button_color = "#432242"
text_color   = "white"
active_color = "#d4aad2"
# root.config(bg=root_color)

english_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ':' ', '|':'|', "":"" }

morse_to_english = dict([(value, key) for key, value in english_to_morse.items()])



def convert():
    """Call the appropriate conversion function based off radio button values"""
    if language.get() == 1:
        get_morse()
    elif language.get() == 2:
        get_english()

def get_morse():
    """Convert an English message to morse code"""
    
    output_text.delete("1.0", END)
    morse_code = ""

    text = input_text.get("1.0", END)
    text = text.lower()

    #Remove any letters of symbols not in our dict keys
    for letter in text:
        if letter not in english_to_morse.keys():
            text = text.replace(letter, '')
        if letter == '.' or letter == '-':
            break

    word_list = text.split(" ")

    for word in word_list:
        for letter in word:
            morse_char = english_to_morse[letter]
            morse_code += morse_char
            morse_code += " "  #Seperate individual letters with a space
        morse_code += "|"      #Seperate individual words with a |

    output_text.insert("1.0", morse_code)

def get_english():
    """Convert a morse code message to english"""

    output_text.delete("1.0", END)
    english = ""

    text = input_text.get("1.0", END)

    #Remove any letters or symbols not in our dict keys
    for letter in text:
        if letter not in morse_to_english.keys():
            text = text.replace(letter, '')
            break

    word_list = text.split("|")

    for word in word_list:
        letters = word.split(" ")
        for letter in letters:
            english_char = morse_to_english[letter]
            english += english_char
        english += " "  #Seperate individual words with a space

    output_text.insert("1.0", english)

def play_sound(file):
    mixer.music.load(file)
    mixer.music.play()
    while mixer.music.get_busy():
        continue

def play():
    """Play tones for corresponding dots and dashes"""

    #Determine where the morse code is
    if language.get() == 1:
        text = output_text.get("1.0", END)
    elif language.get() == 2:
        text = input_text.get("1.0", END)

    #Play the tones (., -, " " , |)
    for value in text:
        if value == ".":
            play_sound('dot.wav')
            root.after(100)
        elif value == "-":
            play_sound('dash.wav')
            root.after(200)
        elif value == " ":
            root.after(300)
        elif value == "|":
            root.after(50)


def clear():
    """Clear both text fields"""
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)

Label1 = tkinter.Label(root)
Label1.place(relx=0.356, rely=0.067, height=40, width=242)
Label1.configure(background="#432242", disabledforeground="#a3a3a3", foreground="white" )
Label1.configure(text='''Morse Code''',font=("Comic Sans MS",30,'italic'))


Label2 = tkinter.Label(root)
Label2.place(relx=0, rely=0.200, height=25, width=930)
Label2.configure(background="#432242", disabledforeground="#a3a3a3", foreground="white" )
Label2.configure(text='''Morse code is a method of converting plain text into a series of on-off tones, lights or''',font=("Comic Sans MS",12,'italic'))

Label3 = tkinter.Label(root)
Label3.place(relx=0, rely=0.250, height=25, width=930)
Label3.configure(background="#432242", disabledforeground="#a3a3a3", foreground="white" )
Label3.configure(text='''clicks or some dots & dashes format text which can be understood only by a skilled listener or observer.''',font=("Comic Sans MS",12,'italic'))

Label4 = tkinter.Label(root)
Label4.place(relx=0.0165, rely=0.355, height=26, width=418)
Label4.configure( background="#c48cc2", disabledforeground="#a3a3a3", foreground="#000000")
Label4.configure(text='''USER INPUT''',font=("arial",15,'bold')) 

Label5 = tkinter.Label(root)
Label5.place(relx=0.699, rely=0.355, height=26, width=255)
Label5.configure(background="#c48cc2", disabledforeground="#a3a3a3", foreground="#000000" )
Label5.configure(text='''OUTPUT''',font=("arial",15,'bold'))

Label6 = tkinter.Label(root)
Label6.place(relx=0.48, rely=0.355, height=26, width=200)
Label6.configure( background="#c48cc2", disabledforeground="#a3a3a3", foreground="#000000")


input_frame = tkinter.LabelFrame(root, bg=frame_color)
input_frame.place(relx=0.015, rely=0.400,height=174, relwidth=0.465)
output_frame = tkinter.LabelFrame(root, bg=frame_color)
output_frame.place(relx=0.48, rely=0.400,height=174, relwidth=0.500)
# input_frame.pack(padx=150, pady=(150,8))
# output_frame.pack(padx=150, pady=(8,150))



#Layout for the input frame
input_text = tkinter.Text(input_frame, height=7, width=50, bg=text_color)
input_text.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

language = IntVar()
language.set(1)
morse_button = tkinter.Radiobutton(input_frame, text="English --> Morse Code",variable=language, value=1, font=button_font, bg=frame_color)
morse_button.configure(font=("arial",10,'bold'))
morse_button.configure(activebackground=active_color)

english_button = tkinter.Radiobutton(input_frame, text="Morse Code --> English",variable=language, value=2, font=button_font, bg=frame_color)
english_button.configure(font=("arial",10,'bold'))
english_button.configure(activebackground=active_color)


morse_button.grid(row=1, column=0)
english_button.grid(row=1, column=1)

#Layout for the output frame
output_text = tkinter.Text(output_frame, height=9.2, width=30, bg=text_color)
output_text.grid(row=0, column=1, rowspan=3, padx=5, pady=5)

convert_button = tkinter.Button(output_frame, text="Convert", font=button_font,bg=button_color, foreground="white", activebackground=active_color, command=convert)
play_button = tkinter.Button(output_frame, text="Play Morse", font=button_font,bg=button_color, foreground="white", activebackground=active_color, command=play)
clear_button = tkinter.Button(output_frame, text="Clear", font=button_font,bg=button_color, foreground="white", activebackground=active_color, command=clear)
convert_button.grid(row=0, column=0, padx=10, ipadx=56 )
play_button.grid(row=1, column=0, padx=10, sticky="WE")
clear_button.grid(row=2, column=0, padx=10, sticky="WE")

root.mainloop()