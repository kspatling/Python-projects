from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pygame



class GUI:

    def __init__(self):

        self.sport = {
            'iPhone 1': 'Released June 29, 2007',
            'iPhone 3': 'Released June 11, 2008',
            'iPhone 4': 'Released June 21, 2010',
            'iPhone 5': 'Released September 21, 2012',
            'iPhone 6': 'Released September 19, 2014'
        }

        self.phones = ['iPhone1', 'iPhone3', 'iPhone4', 'iPhone5', 'iPhone6']

        self.Y2007 = 'Music - Beyonce.mp3'
        self.Y2008 = 'Music - Flo Rida.mp3'
        self.Y2010 = 'Music - Kesha.mp3'
        self.Y2012 = 'Music - Gotye.mp3'
        self.Y2014 = 'Music - Pharrell Williams.mp3'

        self.Y2007Photo = 'Photo - Iphone1.png'
        self.Y2008Photo = 'Photo - Iphone3.png'
        self.Y2010Photo = 'Photo - Iphone4.png'
        self.Y2012Photo = 'Photo - Iphone5.png'
        self.Y2014Photo = 'Photo - Iphone6.png'


    def mainwindow(self):
        global window, lbl1, lbl3, e1, btn1, btn3, btn6

        window = Tk()
        window.title('Category Finder')
        window.geometry('500x500')
        window.configure(bg='#4bcf46')
        pygame.init()
        pygame.mixer.init()

        lbl1 = Label(window, text='Find A Category', font=('Helvetica', 20, 'bold'), bg='#4bcf46', fg='#d12421')
        lbl1.place(x=152, y=140)

        lbl3 = Label(window, text='Made by Kevin Spatling', font=('Helvetica', 8, 'bold'), bg='#4bcf46', fg='#d12421')
        lbl3.place(x=369, y=480)

        e1 = ttk.Combobox(window, value=self.phones)
        e1.place(x=157, y=200)

        btn1 = Button(window, text='Search', font=('Helvetica', 12, 'bold'), bg='#4bcf46', fg='#d12421', command=self.destroymain)
        btn1.place(x=300, y=200)

        btn3 = Button(window, text='Give Your Feedback', font=('Helvetica', 12, 'bold'), bg='#4bcf46', fg='#d12421', command=self.destroymainfeedback)
        btn3.place(x=172, y=400)

        btn6 = Button(window, text='Check Feedback', font=('Helvetica', 12, 'bold'), bg='#4bcf46', fg='#d12421', command=self.destroymainviewfeedback)
        btn6.place(x=184, y=350)

        mainloop()

    def displaydate(self):
        global lbl2, img1

        if e1.get() == 'iPhone1':

            lbl2 = Label(window, text=self.sport.get('iPhone 1'), font=('Helvetica', 12, 'bold'), bg='#4bcf46', fg='#d12421')
            lbl2.place(x=160, y=200)

            self.photo = PhotoImage(file=self.Y2007Photo)
            img1 = Label(window, image=self.photo)
            img1.place(x=160, y=50)

            pygame.mixer.music.load(self.Y2007)
            pygame.mixer.music.play()

            self.backbutton()

        elif e1.get() == 'iPhone3':

            lbl2 = Label(window, text=self.sport.get('iPhone 3'), font=('Helvetica', 12, 'bold'), bg='#4bcf46', fg='#d12421')
            lbl2.place(x=160, y=200)

            self.photo = PhotoImage(file=self.Y2008Photo)
            img1 = Label(window, image=self.photo)
            img1.place(x=160, y=50)

            pygame.mixer.music.load(self.Y2008)
            pygame.mixer.music.play()

            self.backbutton()

        elif e1.get() == 'iPhone4':

            lbl2 = Label(window, text=self.sport.get('iPhone 4'), font=('Helvetica', 12, 'bold'), bg='#4bcf46', fg='#d12421')
            lbl2.place(x=155, y=200)

            self.photo = PhotoImage(file=self.Y2010Photo)
            img1 = Label(window, image=self.photo)
            img1.place(x=160, y=50)

            pygame.mixer.music.load(self.Y2010)
            pygame.mixer.music.play()

            self.backbutton()

        elif e1.get() == 'iPhone5':

            lbl2 = Label(window, text=self.sport.get('iPhone 5'), font=('Helvetica', 12, 'bold'), bg='#4bcf46', fg='#d12421')
            lbl2.place(x=155, y=200)

            self.photo = PhotoImage(file=self.Y2012Photo)
            img1 = Label(window, image=self.photo)
            img1.place(x=160, y=50)

            pygame.mixer.music.load(self.Y2012)
            pygame.mixer.music.play()

            self.backbutton()

        elif e1.get() == 'iPhone6':

            lbl2 = Label(window, text=self.sport.get('iPhone 6'), font=('Helvetica', 12, 'bold'), bg='#4bcf46', fg='#d12421')
            lbl2.place(x=155, y=200)

            self.photo = PhotoImage(file=self.Y2014Photo)
            img1 = Label(window, image=self.photo)
            img1.place(x=160, y=50)

            pygame.mixer.music.load(self.Y2014)
            pygame.mixer.music.play()

            self.backbutton()


    def feedback(self):
        global lbl4, text1, btn5

        lbl4 = Label(window, text='Leave Your Feedback!', font=('Helvetica', 20, 'bold'), bg='#4bcf46', fg='#d12421')
        lbl4.place(x=105, y=20)

        text1 = Text(window, width=50, height=18)
        text1.config(state=NORMAL)
        text1.place(x=49, y=60)

        btn5 = Button(window, text='Submit', font=('Helvetica', 12, 'bold'), bg='#4bcf46', fg='#d12421', command=self.submitfeedback)
        btn5.place(x=217, y=360)

        self.backbutton2()


    def viewfeedback(self):
        global scrollbar, text2, lbl5

        f = open('Iphone Feedback File', 'r')

        lbl5 = Label(window, text='Wonderful Feedback!', font=('Helvetica', 20, 'bold'), bg='#4bcf46', fg='#d12421')
        lbl5.place(x=115, y=20)

        scrollbar = Scrollbar(window)
        scrollbar.place(x=450, y=60, relheight=0.5848)

        text2 = Text(window, width=50, height=18, yscrollcommand=scrollbar.set)
        text2.config(state=NORMAL)
        scrollbar.config(command=text2.yview)
        text2.place(x=49, y=60)

        while True:
            line = f.readline()

            if len(line) == 0:
                break

            text2.insert(INSERT, line)

        self.backbutton3()


    def backbutton(self):
        global btn2

        btn2 = Button(window, text='Back', font=('Helvetica', 12, 'bold'), bg='#4bcf46', fg='#d12421', command=self.backmain)
        btn2.place(x=225, y=470)


    def backbutton2(self):
        global btn4

        btn4 = Button(window, text='Back', font=('Helvetica', 12, 'bold'), bg='#4bcf46', fg='#d12421', command=self.backmainfeedback)
        btn4.place(x=225, y=470)


    def backbutton3(self):
        global btn7

        btn7 = Button(window, text='Back', font=('Helvetica', 12, 'bold'), bg='#4bcf46', fg='#d12421', command=self.backmainviewfeedback)
        btn7.place(x=225, y=470)


    def backmain(self):

        pygame.mixer.music.stop()
        lbl2.place_forget()
        btn2.place_forget()
        img1.place_forget()
        lbl1.place(x=152, y=140)
        lbl3.place(x=369, y=480)
        e1.place(x=157, y=200)
        btn1.place(x=300, y=200)
        btn3.place(x=174, y=400)
        btn6.place(x=184, y=350)

    def backmainfeedback(self):

        lbl4.place_forget()
        btn4.place_forget()
        text1.place_forget()
        btn5.place_forget()
        lbl1.place(x=152, y=140)
        lbl3.place(x=369, y=480)
        e1.place(x=157, y=200)
        btn1.place(x=300, y=200)
        btn3.place(x=174, y=400)
        btn6.place(x=184, y=350)

    def backmainviewfeedback(self):

        scrollbar.place_forget()
        text2.place_forget()
        lbl5.place_forget()
        btn7.place_forget()
        lbl1.place(x=152, y=140)
        lbl3.place(x=369, y=480)
        e1.place(x=157, y=200)
        btn1.place(x=300, y=200)
        btn3.place(x=174, y=400)
        btn6.place(x=184, y=350)


    def destroymain(self):

        self.displaydate()
        lbl1.place_forget()
        lbl3.place_forget()
        e1.place_forget()
        btn1.place_forget()
        btn3.place_forget()
        btn6.place_forget()

    def destroymainfeedback(self):

        self.feedback()
        lbl1.place_forget()
        lbl3.place_forget()
        e1.place_forget()
        btn1.place_forget()
        btn3.place_forget()
        btn6.place_forget()

    def destroymainviewfeedback(self):

        self.viewfeedback()
        lbl1.place_forget()
        lbl3.place_forget()
        e1.place_forget()
        btn1.place_forget()
        btn3.place_forget()
        btn6.place_forget()


    def submitfeedback(self):

        TextValue = text1.get('1.0', 'end-1c')

        if TextValue == '':
            messagebox.showerror('Invalid', 'Please enter a valid Feedback!')

        else:
            f = open('Iphone Feedback File', 'a+')

            f.write(TextValue + '\n\n')

            self.backmainfeedback()

            messagebox.showinfo('Successful Submition', 'Thank you for your feedback!')


def main():
    mw = GUI()
    mw.mainwindow()


if __name__ == "__main__":
    main()
