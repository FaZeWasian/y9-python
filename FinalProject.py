import tkinter as tk
from tkinter import messagebox
import math
root = tk.Tk()
root.title("My TKinter Program")
root.minsize(400,200)
root.geometry("500x200")  
Decklist = []
i = len(Decklist)
root.configure(bg="red")

    
def show_entries():
    print(Decklist)
    print("Total Cards Submitted ", len(Decklist))


def Next():
    list = root.grid_slaves()
    for l1 in list:
        l1.destroy()
    et1 = tk.Entry(root, bd=1)
    et1.grid(row=2, column=1)
    et2 = tk.Entry(root, bd=1)
    et2.grid(row=4, column=1)
    l9 = tk.Label(root, text="The Probability of This Occuring is...", bd=0, bg='black', fg='white').grid(row=2, column=3)
    
    def calculate():
        num = str
        num = (et2.get())
        if str.isnumeric(num) == False:
            messagebox.showwarning("showwarning", "Plese Submit a Positive Whole Number To The 'How Many Cards Are You Drawing' Box")
        else:
            card = (et1.get())
            if Decklist.count(card) < 1:
                messagebox.showwarning("Showwarning", "You Haven't Submitted This Card to Your Decklist")
            else:
                count = Decklist.count(card)
                N = 60
                k = (int(count))
                n = (int(num))
                x = 1
                probability1 = math.comb(k, x)
                probability2 = math.comb(N-k, n-x)
                probability3 = math.comb(N, n)
                probability4 = int(probability1) * int(probability2)
                probability5 = int(probability4)/int(probability3)
                probability6 = float(probability5) * 100
                probfinal = round(float(probability6))
                bob = probfinal, "%"
                l10 = tk.Label(root, text=bob, bd=0, bg='black', fg='white').grid(row=3, column=3)
                et1.delete(0, tk.END)
                et2.delete(0, tk.END)


    def calculateprize():
        card = (et1.get())
        if Decklist.count(card) < 1:
            messagebox.showwarning("Showwarning", "You Haven't Submitted This Card to Your Decklist")
        else:
            count = Decklist.count(card)
            Np = 60
            kp = (int(count))
            np = 6
            xp = 1
            probability1p = math.comb(kp, xp)
            probability2p = math.comb(Np-kp, np-xp)
            probability3p = math.comb(Np, np)
            probability4p = int(probability1p) * int(probability2p)
            probability5p = int(probability4p)/int(probability3p)
            probability6p = float(probability5p) * 100
            probfinalp = round(float(probability6p))
            bob = probfinalp, "%"
            l10 = tk.Label(root, text=bob, bd=0, bg='black', fg='white').grid(row=3, column=3)
            et1.delete(0, tk.END)
            et2.delete(0, tk.END)

    

    def calculatehand():
        card = (et1.get())
        if Decklist.count(card) < 1:
            messagebox.showwarning("Showwarning", "You Haven't Submitted This Card to Your Decklist")
        else:
            count = Decklist.count(card)
            Nh = 60
            kh = (int(count))
            nh = 7
            xh = 1
            probability1h = math.comb(kh, xh)
            probability2h = math.comb(Nh-kh, nh-xh)
            probability3h = math.comb(Nh, nh)
            probability4h = int(probability1h) * int(probability2h)
            probability5h = int(probability4h)/int(probability3h)
            probability6h = float(probability5h) * 100
            probfinalh = round(float(probability6h))
            bob = probfinalh, "%"
            l10 = tk.Label(root, text=bob, bd=0, bg='black', fg='white').grid(row=3, column=3)
            et1.delete(0, tk.END)
            et2.delete(0, tk.END)





    b1 = tk.Button(root, text = "Calculate", command=calculate, bd=0).grid(row=10, column=1)
    b2 = tk.Button(root, text = "Quit Program", command=root.quit, bd=0).grid(row=0, column=3)
    b3 = tk.Button(root, text = "Calculate for Prizes", command=calculateprize, bd=0).grid(row=11,column=1)
    b4 = tk.Button(root, text = "Calculate for Opening Hand", command=calculatehand, bd=0).grid(row=12,column=1)
    tk.Label(root, text = "Which Card Are You Looking For?", bd=0, bg='black', fg='white').grid(row=1, column=1)
    tk.Label(root, text = "How Many Cards Are You Drawing?", bd=0, bg='black', fg='white').grid(row=3, column=1)

def append():
    Decklist.append(e1.get())
    Decklist.append(e2.get())
    Decklist.append(e3.get())
    Decklist.append(e4.get())
    Decklist.append(e5.get())
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    e5.delete(0, tk.END)
    print("Total Cards Submitted ", len(Decklist))

    
l1=tk.Label(root, text = "Card 1", bg='black', bd=0, fg='white').grid(row=1)
l2=tk.Label(root, text = "Card 2", bg='black', bd=0, fg='white').grid(row=2)
l3=tk.Label(root, text = "Card 3", bg='black', bd=0, fg='white').grid(row=3)
l4=tk.Label(root, text = "Card 4", bg='black', bd=0, fg='white').grid(row=4)
l5=tk.Label(root, text = "Card 5", bg='black', bd=0, fg='white').grid(row=5)
l6=tk.Label(root, text="Enter Your Cards 5 at a Time", bg='black', bd=0, fg='white').grid(row=6, column=1)


e1 = tk.Entry(root, bd=1)
e2 = tk.Entry(root, bd=1)
e3 = tk.Entry(root, bd=1)
e4 = tk.Entry(root, bd=1)
e5 = tk.Entry(root, bd=1)


e1.grid(row=1, column =1)
e2.grid(row=2, column =1)
e3.grid(row=3, column =1)
e4.grid(row=4, column =1)
e5.grid(row=5, column =1)

    

Iput=tk.Button(root, text = "Show Input", bd=0, command=show_entries).grid(row=1, column=2)
add = tk.Button(root, text = "Add to List", command=append, bd=0).grid(row=2, column=2)
Next = tk.Button(root, text = "Next", command=Next, bd=0).grid(row=3,column=2)


root.mainloop()


