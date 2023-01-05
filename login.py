from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from time import strftime
import os
import wikipedia


try:
    Window=Tk()
    Window.title("Login")
    Window.attributes('-fullscreen',True)
    
    Window.configure(bg="black")
    c = Image.open(r'C:\Users\admin\Desktop\Important Files\Python\Projects\FastSilver\files\Chrome (3).png')
    c = c.resize((100, 100))
    click_btn = ImageTk.PhotoImage(c)
    #click_btn= PhotoImage(file=r'C:\Users\admin\Desktop\Important Files\Python\Projects\FastSilver\files\Chrome.png')
    img_label= Label(image=click_btn)
    img_label.configure(fg="black")

    c = Image.open(r'C:\Users\admin\Desktop\Important Files\Python\Projects\FastSilver\files\termux.png')
    c = c.resize((100, 100))
    click_btn_2 = ImageTk.PhotoImage(c)
    #click_btn= PhotoImage(file=r'C:\Users\admin\Desktop\Important Files\Python\Projects\FastSilver\files\Chrome.png')
    img_label= Label(image=click_btn)
    img_label.configure(fg="black")

    c = Image.open(r'C:\Users\admin\Desktop\Important Files\Python\Projects\FastSilver\files\info.png')
    c = c.resize((70, 70))
    click_btn_3 = ImageTk.PhotoImage(c)
    #click_btn= PhotoImage(file=r'C:\Users\admin\Desktop\Important Files\Python\Projects\FastSilver\files\Chrome.png')
    img_label= Label(image=click_btn)
    img_label.configure(fg="black")


    text_ = Label(Window, text="Please enter login details")
    text_.configure(font=('Helvetica bold', 26),fg="green",bg="black")
    text_.pack()

    text_ = Label(Window, text="l")
    text_.configure(font=('Helvetica bold', 26),fg="black",bg="black")
    text_.pack()
    
    text_ = Label(Window, text="Username")
    text_.configure(font=('Helvetica bold', 26),fg="green",bg="black")
    text_.pack()

    username_login_entry = Entry(Window, textvariable="username")
    username_login_entry.configure(fg="green",bg="black",insertbackground="white")
    username_login_entry.pack()
    text_ = Label(Window, text="l")
    text_.configure(font=('Helvetica bold', 26),fg="black",bg="black")
    text_.pack()
    text_ = Label(Window, text="Password")
    text_.configure(font=('Helvetica bold', 26),fg="green",bg="black")
    text_.pack()

    password__login_entry = Entry(Window, textvariable="password", show= '*')
    password__login_entry.configure(fg="green",bg="black",insertbackground="white")
    password__login_entry.pack()
    text_ = Label(Window, text="l")
    text_.configure(font=('Helvetica bold', 26),fg="black",bg="black")
    text_.pack()

    def check():
        if username_login_entry.get() == "Stutya Patwal" and password__login_entry.get() == "Stutya@11":
            okay()
        else:
            messagebox.showwarning("Incorrect credentials","Your username or password is incorrect!")


    def clean():
        for items in Window.winfo_children():
         items.destroy()

    def chrome():
        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    
    def terminals():
        def max():
                terminals_win.state('zoomed')
                
        main_element_info = Button(text="Info",command=max)
        main_element_info.configure(bg="black",fg="white")
        main_element_info.place(x=500,y=730)

        terminals_win = Tk()
        terminals_win.title("Terminals")
        terminals_win.configure(bg="black")
        
        terminals_win.mainloop()
    
    def info():
        def max():
                info_win.state('zoomed')

        main_element_info = Button(text="Info",command=max)
        main_element_info.configure(bg="black",fg="white")
        main_element_info.place(x=500,y=730)
        info_win = Tk()
        info_win.title("Information Gatherer")
        info_win.configure(bg="black")

        query = Entry(info_win)
        query.configure(background="black",insertbackground="white",fg="green")
        query.pack()

        def search_():
            try:
                result = wikipedia.summary(query.get(), sentences = 100)
                l = Text(info_win,wrap=WORD)
                l.insert(INSERT,result)
                l.configure(bg="black",fg="white")
                l.pack()
            except:
                result = "Sorry, no result found!"
                l = Text(info_win,wrap=WORD)
                l.insert(INSERT,result)
                l.configure(bg="black",fg="red")
                l.pack()
                

        search = Button(info_win,text="Search",command=search_)
        search.configure(background="black",fg="green")
        search.pack()

        def ds():
            main_element_info.destroy()
            info_win.destroy()


        info_win.protocol("WM_DELETE_WINDOW", ds)
        info_win.mainloop()

    def okay():
        clean()
        button= Button(Window, bg="black",image=click_btn,command= chrome,
        borderwidth=0,activebackground="black")
        button.config(font=('Helvetica bold', 1),bg="black")
        button.place(x=0,y=0)

        button= Button(Window, bg="black",image=click_btn_2,command= terminals,
        borderwidth=0,activebackground="black")
        button.config(font=('Helvetica bold', 1),bg="black")
        button.place(x=100,y=0)

        button= Button(Window, bg="black",image=click_btn_3,command= info,
        borderwidth=0,activebackground="black")
        button.config(font=('Helvetica bold', 1),bg="black")
        button.place(x=200,y=0)


        taskwidth = Window.winfo_screenwidth()
        taskheight = Window.winfo_screenheight()
        Port = Canvas(Window, height = 0.1 * (taskheight), width = 10000, bg = "#030059", highlightthickness = 0)
        Port.place(relx = 0.5, rely = 0.995, anchor = "center")

        def time():
            string = strftime('%H:%M %p')
            lbl.config(text=string)
            lbl.after(1000, time)

 
 
        # Styling the label widget so that clock
        # will look more attractive
        lbl = Label(Window, font=('calibri', 15, 'bold'),
                    background='#030059',
                    foreground='white',
                    )
        
        # Placing clock at the centre
        # of the tkinter window
        lbl.place(x=1260,y=730)
        time()

        def start():
            really = messagebox.askyesno("FastSilver Os","Do you want to shutdown?")
            if really == True:
                Window.destroy()
            else:
                pass
        Start = Button(text="START",command=start)
        Start.configure(background='#030059',foreground='white')
        Start.place(x=0,y=730)

    #okay()

        

    



    text_ = Button(Window, text="Login", width=10, height=1,command=check)
    text_.configure(font=('Helvetica bold', 13),fg="green",bg="black")
    text_.pack()





    



    Window.mainloop()

except Exception as e:
    print(e)
