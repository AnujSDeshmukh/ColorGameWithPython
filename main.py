import customtkinter as ctk
from random import choice, shuffle
from playsound import playsound

#window
window = ctk.CTk(fg_color = "#9966cc")
window.title("The Color")
window.geometry("640x480")
window.resizable(False, False)
window._set_appearance_mode("light")
window.iconbitmap("icon.ico")

points = ctk.IntVar(value = 0)
timer = ctk.IntVar(value = 31)

def update_timer():
    global timer
    if timer.get() > 0:
        timer.set(timer.get() - 1)
        window.after(1000, update_timer)
    else:
        title_text.configure(text = "Time Up!!", text_color = "red", fg_color = "black")
        restart_button.configure(state = "normal")

def restart():
    global color_text
    global title_text
    global textbox
    points.set(0)
    timer.set(31)

    textbox.delete(0, ctk.END)
    restart_button.configure(state = "disabled")
    
    shuffle(colors)
    color_text.configure(text = "")
    color_text.configure(text = "")
    color_text.configure(text = choice(colors), text_color = choice(colors))
    title_text.configure(text = "Guess The Color:", fg_color = "black")
    update_timer()

def change(*args):
    global color_text
    global points
    global textbox
    global timer

    if timer.get() > 0:

        if textbox.get().lower() == color_text.cget("text_color").lower():
            textbox.delete(0, ctk.END)
            points.set(points.get() + 1)
            if points.get() > 9:
                points_text.place(relx = 0.9, rely = 0.99, anchor = "sw")
            
            shuffle(colors)
            color_text.configure(text = "")
            color_text.configure(text = choice(colors), text_color = choice(colors))


        else:
            textbox.delete(0, ctk.END)
            shuffle(colors)
            color_text.configure(text = "")
            color_text.configure(text = choice(colors), text_color = choice(colors))
        
update_timer()

#Title 
title_text = ctk.CTkLabel(window, text = "Guess The Color:",
                          font = ("Fira Code Medium", 60),
                          text_color = "red", fg_color = "black")
title_text.pack(pady = 10)


#colors list
colors = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Cyan']

#the changing color
color_font = ctk.CTkFont("Fira Code Medium", 55)

color_text = ctk.CTkLabel(window, text = choice(colors), 
                          text_color = choice(colors),
                          font = color_font)
color_text.place(relx = 0.5, rely = 0.4, anchor = "center")

#answer input
textbox = ctk.CTkEntry(window, width = 350, height = 60, 
                       justify = "right",
                       font = ("Fira Code Medium", 35),
                       )
textbox.pack(side = "bottom", pady = 100)

textbox.bind("<KeyPress-Return>", change)

#points
points_text = ctk.CTkLabel(window, text = 0,
                           textvariable = points,
                           font = ("Fira Code Medium", 40))
points_text.place(relx = 0.95, rely = 0.99, anchor = "sw")

timer_text = ctk.CTkLabel(window, text = "30",
                          text_color = "red",
                           font = ("Fira Code Medium", 40),
                           textvariable = timer)
timer_text.place(relx = 0.01, rely = 0.99, anchor = "sw")



restart_button = ctk.CTkButton(window, text = "Restart", command = restart,
                               font = ("Fira Code Medium", 40),
                               state = "disabled")
restart_button.place(relx = 0.36, rely = 0.87)

#mainloop
window.mainloop()