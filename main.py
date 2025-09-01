import random, tkinter as tk

sum = 0
WIN_REQ = 50

root = tk.Tk()
root.title("PIG")
root.geometry("600x400") # Sets width to 400 pixels and height to 300 pixels
root.resizable(False, False)

label1 = tk.Label(
    root,
    text="Welcome to Pig.",
    font=("Arial", 20, "bold"))

label2 = tk.Label(
    root,
    text="Player keeps rolling a single die as many times as they wish adding all roll results to a running total,",
    font=("Arial", 9))

label3 = tk.Label(
    root,
    text="but losing their gained score for the turn if they roll a 1.",
    font=("Arial", 9))

label4 = tk.Label(
    root,
    text="The goal is to reach 50 points.",
    font=("Arial", 9))

label5 = tk.Label(
    root,
    text="Total Score: ",
    font=("Arial", 9))

label6 = tk.Label(
    root,
    text="Roll: ",
    font=("Arial", 9))

def onClick():
    global sum
    if sum > WIN_REQ:
       return
    roll = random.randint(1,6)

    label6.config(
        text="Roll: "+str(roll))

    if roll != 1:
        sum = sum + roll
        if sum > WIN_REQ:
            label5.config(
                text="YOU WIN!!!",
                font=("bold"),
                fg="Green"
                ) 
            label6.config(
                text="Roll: "+str(roll),
                fg="Green"
                )
            return
    else:
        sum = 0
    label5.config(text="Total Score: "+str(sum))



button = tk.Button(
    root,
    text="Roll the Die",
    command=onClick,
    width=40, 
    height=10)



label1.pack()
label2.pack()
label3.pack()
label4.pack()
button.pack(pady=20)
label5.pack()
label6.pack()

root.mainloop()
