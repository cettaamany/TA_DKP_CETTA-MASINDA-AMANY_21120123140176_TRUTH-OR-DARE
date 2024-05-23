import random
import tkinter as tk
from queue import Queue
from tkinter import ttk, messagebox

class TruthOrDare:
    def __init__(self, master):
        self.master = master
        self.master.title("Truth or Dare by Cetta Masinda A. (21120123140176)")
        self.master.geometry("480x360")
        self.master.resizable(width=False, height=False)

        labelwelcome = tk.Label(self.master,
                 text = "Truth or Dare? either way, have FUNN!!<3",
                 font = ("calibri", 11)).place(x=30, y=20)
        labelnama = tk.Label(self.master,
                        text = "Knock, knock who's there?",
                        font = ("calibri", 10)).place(x=30, y=50)
        labelclose = tk.Label(self.master,
                        text = "How close are you guys?",
                        font = ("calibri", 10)).place(x=30, y=140)
        labelquotes = tk.Label(self.master,
                        text = '"truth, dare, spin bottles. you know how to ball, I know Aristotle"',
                        font = ("calibri", 10, "italic")).place(x=65, y=260)

        #insert nama
        self.strnama1 = tk.StringVar()
        entrynama = tk.Entry(self.master, textvariable=self.strnama1, font=("calibri", 10))
        entrynama.place(x=30, y=80)
        self.strnama2 = tk.StringVar()
        entrynama = tk.Entry(self.master, textvariable=self.strnama2, font=("calibri", 10))
        entrynama.place(x=30, y=105)

        #button
        self.radio = tk.IntVar()
        R1 = tk.Radiobutton(self.master,
                            text="we just knew each other!",
                            font=("calibri", 10),
                            variable=self.radio,
                            value=1).place(x=30, y=160)
        R2 = tk.Radiobutton(self.master,
                            text="we often get breakfast together",
                            font=("calibri", 10),
                            variable=self.radio,
                            value=2).place(x=30, y=180)
        R3 = tk.Radiobutton(self.master,
                            text="we go out to destress together",
                            font=("calibri", 10),
                            variable=self.radio,
                            value=3).place(x=30, y=200)
        R4 = tk.Radiobutton(self.master,
                            text="we're like long lost siblings",
                            font=("calibri", 10),
                            variable=self.radio,
                            value=4).place(x=30, y=220)

        #player 1
        strhobby1 = tk.StringVar(value='gender') 
        combobox1 = ttk.Combobox(self.master, 
                        width = 17,
                        font = ("calibri", 10), 
                        textvariable = strhobby1, 
                        state ="readonly")
        combobox1.place(x=180, y=80)
        combobox1['values'] = ('Woman','Man')
        #player 2
        strhobby2 = tk.StringVar(value='gender') 
        combobox2 = ttk.Combobox(self.master, 
                        width = 17,
                        font = ("calibri", 10), 
                        textvariable = strhobby2, 
                        state ="readonly")
        combobox2.place(x=180, y=105)
        combobox2['values'] = ('Woman','Man')

        self.master.protocol("WM_DELETE_WINDOW", self.close_window)
        self.queue = Queue()

        button_play = tk.Button(self.master,
                        text = "play",
                        font = ("calibri", 12),
                        command = self.open_name_window).place(x=220, y=290)

    def open_name_window(self):
        top = tk.Toplevel(self.master)
        top.title("Truth or Dare")
        top.geometry("300x100")
        tk.Label(top, text=f"{self.strnama1.get()}, what's your choice?").pack()
        self.choice1 = tk.StringVar()
        tk.Button(top, text="Truth", command=lambda: [self.truth(), top.destroy(), self.open_name_window2()]).place(x=100, y=30)
        tk.Button(top, text="Dare", command=lambda: [self.dare(), top.destroy(), self.open_name_window2()]).place(x=160, y=30)

    def open_name_window2(self):
        top = tk.Toplevel(self.master)
        top.title("Truth or Dare")
        top.geometry("300x100")
        tk.Label(top, text=f"{self.strnama2.get()}, what's your choice?").pack()
        self.choice2 = tk.StringVar()
        tk.Button(top, text="Truth", command=lambda: [self.truth(), top.destroy(), self.open_name_window()]).place(x=100, y=30)
        tk.Button(top, text="Dare", command=lambda: [self.dare(), top.destroy(), self.open_name_window()]).place(x=160, y=30)

  
    

    def truth(self):
        # random number
        n = random.randint(1, 15)
        if n == 1:
            tk.messagebox.showinfo("Truth", "what's your favourite movie?")
        elif n == 2:
            tk.messagebox.showinfo("Truth", "do you think, you have met your soulmate?")
        elif n == 3:
            tk.messagebox.showinfo("Truth", "What is the worst date you've ever been on?")
        elif n == 4:
            tk.messagebox.showinfo("Truth", "Have you ever peed in a pool?")
        elif n == 5:
            tk.messagebox.showinfo("Truth", "If you can choose between a bear and a man, what would you choose?")
        elif n == 6:
            tk.messagebox.showinfo("Truth", "Why did you start talking in your sleep?")
        elif n == 7:
            tk.messagebox.showinfo("Truth", "Is there someone here you find here you find attractive?")
        elif n == 8:
            tk.messagebox.showinfo("Truth", "What's your most embarrassing nickname?")
        elif n == 9:
            tk.messagebox.showinfo("Truth", "Have you ever been rejected?")
        elif n == 10:
            tk.messagebox.showinfo("Truth", "What would be a perfect world looks like for you?")
        elif n == 11:
            tk.messagebox.showinfo("Truth", "Who is your person?")
        elif n == 12:
            tk.messagebox.showinfo("Truth", "What's the most illegal thing you've ever done?")
        elif n == 13:
            tk.messagebox.showinfo("Truth", "What's the most expensive thing you've ever broken?")
        elif n == 14:
            tk.messagebox.showinfo("Truth", "Have you ever went to concert?")
        elif n == 15:
            tk.messagebox.showinfo("Truth", "Why did you stay out all night?")

    def dare(self):
        # random number
        n = random.randint(1, 15)
        if n == 1:
            tk.messagebox.showinfo("Dare", "Sing a song in front of your friends")
        elif n == 2:
            tk.messagebox.showinfo("Dare", "Do a cartwheel in front of your friends")
        elif n == 3:
            tk.messagebox.showinfo("Dare", "Confess to your favourite person")
        elif n == 4:
            tk.messagebox.showinfo("Dare", "Do tell the tea!")
        elif n == 5:
            tk.messagebox.showinfo("Dare", "Dance to the song that the other person choose")
        elif n == 6:
            tk.messagebox.showinfo("Dare", "Draw a ladybug in 5 seconds")
        elif n == 7:
            tk.messagebox.showinfo("Dare", "write a poem for the other person")
        elif n == 8:
            tk.messagebox.showinfo("Dare", 'Sing a song with your mouth in an "o" shape')
        elif n == 9:
            tk.messagebox.showinfo("Dare", "watch a horor movie without closing your eyes")
        elif n == 10:
            tk.messagebox.showinfo("Dare", "Do a sit-up in front of your friends")
        elif n == 11:
            tk.messagebox.showinfo("Dare", "Do a jumping jack in front of your friends")
        elif n == 12:
            tk.messagebox.showinfo("Dare", "Do a squat in front of your friends")
        elif n == 13:
            tk.messagebox.showinfo("Dare", "Give a controversial statement to the table")
        elif n == 14:
            tk.messagebox.showinfo("Dare", "Dress like your type tomorrow")
        elif n == 15:
            tk.messagebox.showinfo("Dare", "Do a wall sit in front of your friends")
        

    def close_window(self):
        self.master.destroy()

root = tk.Tk()
my_gui = TruthOrDare(root)
root.mainloop()