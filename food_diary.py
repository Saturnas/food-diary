import tkinter as tk 
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter.font as font
import sqlite3

# program font and size settings
root = tk.Tk()
myFont = font.Font(size=20)
font2 = font.Font(family='Helvetica',
        size=14, weight='bold')

# make data from database easy to understand
def fetching():
    for x in cursor.fetchall():
        x5 = str(x[5])
        x6 = str(x[6])
        newline0 = "Date:"+ str(x[0])
        newline1 = "Breakfast: " + str(x[1])\
         + " | Dinner: " + str(x[2]) + " | Supper: " + str(x[3])\
         + " | Snacks: "\
         + str(x[4])
        newline2 =  "Calories: " + x5 + " | Weight: " + x6\
         + " | Exercises: " + str(x[7])
        newline3 =  "Comments: " + str(x[8] + "\n")
        text_box.insert(tk.END, newline0)
        text_box.insert(tk.END, newline1)
        text_box.insert(tk.END, newline2)
        text_box.insert(tk.END, newline3)

# getting data from database
def viewdb():
    cursor.execute("SELECT * FROM Foods")
    fetching()
        
# pop-up window for new entry
def new():
    def add():
        # getting data from entry fields
        newdate = entry_box.get()
        newbreakfast = entry_box2.get()
        newdinner = entry_box3.get()
        newsupper = entry_box4.get()
        newsnack = entry_box5.get()
        newcalories = entry_box6.get()
        newweight = entry_box7.get()
        newexercises = entry_box8.get()
        newcomment = entry_box9.get()
        # submits data to databse
        cursor.execute("""INSERT INTO Foods (Data,Breakfast,Dinner,Supper,\
            Snacks,Calories,Weight,Exercises,Comment)
    VALUES (?,?,?,?,?,?,?,?,?)""",(newdate,newbreakfast,newdinner,newsupper,\
        newsnack,newcalories,newweight,newexercises,newcomment))
        db.commit()
        # clears entry fields after submit
        entry_box.delete(0, tk.END)
        entry_box2.delete(0, tk.END)
        entry_box3.delete(0, tk.END)
        entry_box4.delete(0, tk.END)
        entry_box5.delete(0, tk.END)
        entry_box6.delete(0, tk.END)
        entry_box7.delete(0, tk.END)
        entry_box8.delete(0, tk.END)
        entry_box9.delete(0, tk.END)
    
    # pop-up window settings    
    popup = tk.Tk()
    popup.wm_title("New entry")
    popup.geometry("300x420")
    
    # window entry fields
    label = ttk.Label(popup,text="Date: ")
    label.place(x = 10, y = 10, width=75, height=30)
    label['font'] = myFont
    entry_box = ttk.Entry(popup,text=0)
    entry_box.place(x = 100, y = 10, width=150, height=25)
    
    label2 = ttk.Label(popup,text="Breakfast: ")
    label2.place(x = 10, y = 50, width=75, height=25)
    label2['font'] = myFont
    entry_box2 = ttk.Entry(popup,text=1)
    entry_box2.place(x = 100, y = 50, width=150, height=25)
    
    label3 = ttk.Label(popup,text="Dinner: ")
    label3.place(x = 10, y = 90, width=75, height=25)
    label3['font'] = myFont
    entry_box3 = ttk.Entry(popup,text=2)
    entry_box3.place(x = 100, y = 90, width=150, height=25)
    
    label4 = ttk.Label(popup,text="Supper: ")
    label4.place(x = 10, y = 130, width=75, height=25)
    label4['font'] = myFont
    entry_box4 = ttk.Entry(popup,text=3)
    entry_box4.place(x = 100, y = 130, width=150, height=25)
    
    label5 = ttk.Label(popup,text="Snacks: ")
    label5.place(x = 10, y = 170, width=75, height=25)
    label5['font'] = myFont
    entry_box5 = ttk.Entry(popup,text=4)
    entry_box5.place(x = 100, y = 170, width=150, height=25)
    
    label6 = ttk.Label(popup,text="Calories: ")
    label6.place(x = 10, y = 210, width=75, height=25)
    label6['font'] = myFont
    entry_box6 = ttk.Entry(popup,text=5)
    entry_box6.place(x = 100, y = 210, width=150, height=25)

    label7 = ttk.Label(popup,text="Weight: ")
    label7.place(x = 10, y = 250, width=75, height=25)
    label7['font'] = myFont
    entry_box7 = ttk.Entry(popup,text=6)
    entry_box7.place(x = 100, y = 250, width=150, height=25)
    
    label8 = ttk.Label(popup,text="Exercises: ")
    label8.place(x = 10, y = 290, width=75, height=25)
    label8['font'] = myFont
    entry_box8 = ttk.Entry(popup,text=7)
    entry_box8.place(x = 100, y = 290, width=150, height=25)
    
    label9 = ttk.Label(popup,text="Comment: ")
    label9.place(x = 10, y = 330, width=75, height=25)
    label9['font'] = myFont
    entry_box9 = ttk.Entry(popup,text=8)
    entry_box9.place(x = 100, y = 330, width=150, height=25)
    
    button = ttk.Button(popup,width=35,text="Save entry",command = add)
    button.place(x = 40, y = 370)
    popup.mainloop()

# pop-up window for sorting data by weight or by calories
def sort():
    def dialog():
        x = cbtn.state()
        y = cbtn2.state()
        if 'selected' in x:
            c = 0
            cursor.execute("""SELECT * FROM Foods WHERE Weight>?\
             ORDER BY Weight""",[c])
            fetching()

        if 'selected' in y:
            c = 0
            cursor.execute("""SELECT * FROM Foods WHERE Calories>?\
             ORDER BY Calories""",[c])
            fetching()
    
    # pop-up window settings        
    popup = tk.Tk()
    popup.wm_title("Sort by")
    popup.geometry("300x130")
    myvar = tk.IntVar()
    
    # buttons and button positions
    cbtn = ttk.Checkbutton(popup, text='Sort by weight',\
    variable=myvar, onvalue=1)
    cbtn.place(x = 10, y = 10, width=150, height=40)
    cbtn2 = ttk.Checkbutton(popup, text='Sort by calories',\
    variable=myvar, onvalue=2)
    cbtn2.place(x = 10, y = 40, width=150, height=40)
    button = ttk.Button(popup,width=45,text="Choose", command = dialog)
    button.place(x = 10, y = 80)
    popup.mainloop()

# pop-up window for removing data from database by date
def delete():
    def delete():
        datedelete = entry_box.get()
        cursor.execute("DELETE FROM Foods WHERE Data=?",[datedelete])
        db.commit()
        entry_box.delete(0, tk.END)
    
    # pop-up window settings   
    popup = tk.Tk()
    popup.wm_title("Delete")
    popup.geometry("260x150")
    label = ttk.Label(popup,text="Choose entry BY DATE to delete: ")
    label.place(x = 10, y = 10, width=250, height=30)
    label['font'] = myFont
    entry_box = ttk.Entry(popup,text=0)
    entry_box.place(x = 50, y = 50, width=150, height=25)
    button = ttk.Button(popup,width=20,text="Delete", command = delete)
    button.place(x = 60, y = 90)
    popup.mainloop()

# connecting database to program
with sqlite3.connect("food.db") as db:
    cursor = db.cursor()

# creating database if doesn't exist already
cursor.execute(""" CREATE TABLE IF NOT EXISTS Foods(
Data text PRIMARY KEY,
Breakfast text,
Dinner text,
Supper text,
Snacks text,
Calories real,
Weight real,
Exercises text,
Comment text);""")

# program settings
img = Image.open("food.png")
image1 = img.resize((400, 200), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(image=test)
label1.image = test
label1.grid(column=1, row=1, columnspan=2, rowspan=2)

canvas = tk.Canvas(root, width=900, height=800)
canvas.grid(columnspan=6, rowspan=6)
root.resizable(False, False)

text_box = tk.Listbox(root, height=30, width=80,bg='#efefef', font = font2)
text_box.grid(column=1, row=3, sticky='n', columnspan=4, rowspan=2)

browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command = viewdb,\
 font="Raleway", bg="#067331", fg="white", height=3, width=15)
browse_text.set("Show data")
browse_btn.grid(column=3, row=2, sticky='e'+'w')

browse_text1 = tk.StringVar()
browse_btn1 = tk.Button(root, textvariable=browse_text1,command = new,\
 font="Raleway", bg="#507ef2", fg="white", height=2, width=25)
browse_text1.set("New entry")
browse_btn1.grid(column=1, row=6, sticky='n')

browse_text2 = tk.StringVar()
browse_btn2 = tk.Button(root, textvariable=browse_text2, command = sort,\
 font="Raleway", bg="#507ef2", fg="white", height=2, width=25)
browse_text2.set("Sort by")
browse_btn2.grid(column=2, row=6, sticky='n')

browse_text3 = tk.StringVar()
browse_btn3 = tk.Button(root, textvariable=browse_text3, command = delete,\
 font="Raleway", bg="#e20d0d", fg="black", height=2, width=25)
browse_text3.set("Delete")
browse_btn3.grid(column=3, row=6, sticky='n')

root.mainloop()
db.close()