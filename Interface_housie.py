from tkinter import *
from tkinter import messagebox
from time import sleep
import random
l=[]
i=0
p=[str(j) for j in range(1,6)]
def count(stop_variable):
         for i in range(1,6):
                if(stop_variable):
                        j=random.choice(p)
                        sleep(2)
                        l.append(j)
                        p.remove(j)
                        result=messagebox.askokcancel("RandomNumber",str(j))
                        print(l,end="  ")
                        print(p)
                        if not result:
                            previous=",".join(l)
                            messagebox.askokcancel("RandomNumber",previous)
                            end()
                if(i==5 and stop_variable):
                    print("Number completed please restart . . .")
                    break
         if (i==6 and not stop_variable):
            print("Completed numbers")
            stop_variable=False
                    
def start():
    global stop_variable
    stop_variable=True
    count(stop_variable)
def end():
    global stop_variable
    stop_variable=False

top=Tk()
top.geometry("200x200")
b1=Button(top,text="Start",command=start)
b1.grid(row=5,column=1,padx=80,pady=20)
b2=Button(top,text="Stop",command=end)
b2.grid(row=6,column=1,padx=80,pady=50)
top.mainloop()

