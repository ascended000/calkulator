from customtkinter import *

window = CTk()
window.geometry("300x300")
window.maxsize(300, 300)
window.title("calculator")

set_appearance_mode("dark")
set_default_color_theme("green")

def click(symbol):
    entry_calc.insert("end", str(symbol))
def delete():
    entry_calc.delete(0, "end")

def equals():
    try:
        exp = entry_calc.get()
        result = str(eval(exp))  # вычисление строки
        entry_calc.delete(0, "end")
        entry_calc.insert(0, result)
    except Exception:
        entry_calc.delete(0, "end")
        entry_calc.insert(0, "error")


entry_calc = CTkEntry(window, width=250)
entry_calc.grid(row=0, column=0, padx=25)


frame1 = CTkFrame(window, width=250, height=250)
frame1.grid(row=1, pady=50)

btn_1 = CTkButton(frame1, text="1", width=40, height=40, command=lambda symbol = 1:click(symbol))
btn_1.grid(row=0, column=0, padx=5, pady=5)

btn_2 = CTkButton(frame1, text="2", width=40, height=40, command=lambda symbol = 2:click(symbol))
btn_2.grid(row=0, column=1, padx=5, pady=5)

btn_3 = CTkButton(frame1, text="3", width=40, height=40, command=lambda symbol = 3:click(symbol))
btn_3.grid(row=0, column=2, padx=5, pady=5)

btn_divide = CTkButton(frame1, text="/", width=40, height=40, command=lambda symbol = "/":click(symbol))
btn_divide.grid(row=0, column=3, padx=5, pady=5)

btn_4 = CTkButton(frame1, text="4", width=40, height=40, command=lambda symbol = 4:click(symbol))
btn_4.grid(row=1, column=0, padx=5, pady=5)

btn_5 = CTkButton(frame1, text="5", width=40, height=40, command=lambda symbol = 5:click(symbol))
btn_5.grid(row=1, column=1, padx=5, pady=5)

btn_6 = CTkButton(frame1, text="6", width=40, height=40, command=lambda symbol = 6:click(symbol))
btn_6.grid(row=1, column=2, padx=5, pady=5)

btn_multiply = CTkButton(frame1, text="*", width=40, height=40, command=lambda symbol = "*":click(symbol))
btn_multiply.grid(row=1, column=3, padx=5, pady=5)

btn_7 = CTkButton(frame1, text="7", width=40, height=40, command=lambda symbol = 7:click(symbol))
btn_7.grid(row=2, column=0, padx=5, pady=5)

btn_8 = CTkButton(frame1, text="8", width=40, height=40, command=lambda symbol = 8:click(symbol))
btn_8.grid(row=2, column=1, padx=5, pady=5)

btn_9 = CTkButton(frame1, text="9", width=40, height=40, command=lambda symbol = 9:click(symbol))
btn_9.grid(row=2, column=2, padx=5, pady=5)

btn_plus = CTkButton(frame1, text="+", width=40, height=40, command=lambda symbol = "+":click(symbol))
btn_plus.grid(row=2, column=3, padx=5, pady=5)

btn_minus = CTkButton(frame1, text="-", width=40, height=40,command=lambda symbol = "-":click(symbol))
btn_minus.grid(row=3, column=0, padx=5, pady=5)

btn_0 = CTkButton(frame1, text="0", width=40, height=40,command=lambda symbol = 0:click(symbol))
btn_0.grid(row=3, column=1, padx=5, pady=5)

btn_dot = CTkButton(frame1, text=".", width=40, height=40,command=lambda symbol = ".":click(symbol))
btn_dot.grid(row=3, column=2, padx=5, pady=5)

btn_equals = CTkButton(frame1, text="=", width=40, height=40,command=equals)
btn_equals.grid(row=3, column=3, padx=5, pady=5)

btn_sbros = CTkButton(frame1, text="C", width=40, height=40,command=delete)
btn_sbros.grid(row=3, column=4, padx=5, pady=5)

window.mainloop()