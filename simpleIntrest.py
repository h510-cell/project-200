from tkinter import *
windows = Tk()

#add widgets here

windows.title("Simple Intrest")
windows.geometry("380x400")
windows.configure(bg="red")

#function for button

intrest = []
   
def calculate_intrest():
    p = float(principle.get())
    r = float(rate.get())
    t = int(time.get())/100
    i = (p*r*t)/100
    i = round(intrest, 1)
    name = username.get()
    
    showLabel.destroy()

    msg = ""

if intrest < 18.5:
 msg = "2%"
elif intrest < 18.5 and intrest > 24.5:
  msg="5%"
elif intrest > 24.5:
  msg="10%"
elif intrest > 30:
  msg="15%"
else:
  msg="Something Went Wrong"

message = Label(result_frame,text="Intrest on Rs."+str(p)" at rate_of_intrest is "+str(r)" % for "+str(t)"years is Rs."+str(intrest),
bg ="lightcyan",font=("Calibari",12),width="42")
message.place(x=20,y=40)
message.pack()

app_label=Label(windows,text="Simple Intrest",bg ="red",font=("Calibari",12),bd=5)
app_label.place(x=50,y=20)

name_label=Label(windows,text="Your Name",bg ="red",font=("Calibari",12),bd=1)
app_label.place(x=20,y=90)

username=Entry(windows,text="",bd=5,width=22)
app_label.place(x=150,y=90)

rate_label=Label(windows, text="Enter rate ", fg = "black", bg = "red", font=("Calibri", 12))
rate_label.place(x=20, y=140)

rate_entry=Entry(windows, text="", bd=2, width=15)
rate_entry.place(x=150, y=142)

time_label=Label(windows, text="Enter Time", fg = "black", bg = "red", font=("Calibri", 12))
time_label.place(x=20, y=185)

time_entry=Entry(windows, text="", bd=2, width=15)
time_entry.place(x=150, y=187)

calculate_button=Button(windows,text="CALCULATE",fg = "black", bg = "cyan",bd=4,command=calculate_intrest)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(windows,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

showLabel=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
showLabel.place(x=20,y=20)
showLabel.pack()


windows.mainloop()