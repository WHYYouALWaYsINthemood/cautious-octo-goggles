from tkinter import *
import random

root = Tk()
root.geometry("400x400")
root.title("Password Generator")

label = Label(root)

array_3d = [[['1', '2', '3', '4', '5', '6'], ["Head", "Tail"], ["A", "B", "C", "D", "E", "F", "G", "H"]]]
print(array_3d[0][2][3])

def newpassword():
    random_1 = random.randint(0, 5)
    random_2 = random.randint(0, 1)
    random_3 = random.randint(0, 7)
    
    letter1 = str(array_3d[0][0][random_1])
    letter2 = (array_3d[0][1][random_2])
    letter3 = (array_3d[0][2][random_3])
    label["text"] = letter1 + "" + letter2 + "" + letter3
    
btn = Button(root, text = "New password", command = newpassword)

btn.place(relx = 0.5,rely = 0.5,anchor = CENTER)
label.place(relx = 0.5,rely = 0.6,anchor = CENTER)

root.mainloop()