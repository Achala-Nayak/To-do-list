from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("TO DO LIST")
root.geometry("700x300")

my_font=Font(
    family="Charter",
    size=20,
    weight="bold")

my_frame=Frame(root)
my_frame.pack(pady=10)

my_list=Listbox(my_frame,
    font=my_font,
    width=25,
    height=5,
    bg="SystemButtonFace",
    bd=0,#border
    fg="#171717",
    highlightthickness=0,
    selectbackground="#EED6D3",
    activestyle="none")

my_list.pack(side=LEFT,fill=BOTH)
todo=['Web Dev','Docker','Read']
for item in todo:
    my_list.insert(END,item)

my_scrollbar=Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT,fill=BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#entry box
my_entry=Entry(root,font=("Charter",20))
my_entry.pack(pady=20)

button_frame=Frame(root)
button_frame.pack(pady=20)

def delete_item():
    my_list.delete(ANCHOR) #deletes the selected item
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)
def strike_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg='#d3d3d3')
    my_list.selection_clear(0,END)
def unstrike_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg='#171717')
    my_list.selection_clear(0,END)
def deletecrossed_item():
    count=0
    while count < my_list.size():
        if my_list.itemcget(count,"fg") == "#d3d3d3":
            my_list.delete(my_list.index(count))
        else:
            count += 1

#adding buttons
delete_button=Button(button_frame,text="Delete Task",command=delete_item)
add_button=Button(button_frame,text="Add Task",command=add_item)
strike_button=Button(button_frame,text="Strike Task",command=strike_item)
unstrike_button=Button(button_frame,text="Unstrike Task",command=unstrike_item)
deletecrossed_button=Button(button_frame,text="Delete Crossed Task",command=deletecrossed_item)

delete_button.grid(row=0,column=0)
add_button.grid(row=0,column=1,padx=15)
strike_button.grid(row=0,column=2,padx=15)
unstrike_button.grid(row=0,column=3,padx=15)
deletecrossed_button.grid(row=0,column=4)

root.mainloop()
