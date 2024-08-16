import customtkinter as ctk
import tkinter as tk

def calculate():
    try:
        # Get Entry
        a_text = entry_a.get()
        b_text = entry_b.get()
        c_text = entry_c.get()
        d_text = entry_d.get()
        
        a = float(a_text) if a_text else None
        b = float(b_text) if b_text else None
        c = float(c_text) if c_text else None
        d = float(d_text) if d_text else None

        # Calculate
        if var.get() == "a" and b is not None and c is not None and d is not None:
            result = (b * c) / d
        elif var.get() == "b" and a is not None and c is not None and d is not None:
            result = (a * d) / c
        elif var.get() == "c" and a is not None and b is not None and d is not None:
            result = (a * d) / b
        elif var.get() == "d" and a is not None and b is not None and c is not None:
            result = (b * c) / a
        else:
            result_label.configure(text="Error: Incomplete Input")
            return

        # Result
        result_label.configure(text=f"Result: {result:.2f}")
    except ValueError:
        result_label.configure(text="Error: Invalid Input")
    except ZeroDivisionError:
        result_label.configure(text="Error: Division by Zero")
    except Exception as e:
        result_label.configure(text=f"Error: {str(e)}")

app = ctk.CTk()
app.title("比例計算器 Proportion-Calc")
app.geometry("350x450")
app.resizable(0, 0)

# Main Frame
frame = ctk.CTkFrame(app)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# LeftAB grid
frame_left = ctk.CTkFrame(frame)
frame_left.pack(side="left", padx=10)

label_a = ctk.CTkLabel(frame_left, text="A:")
label_a.pack(pady=5)
entry_a = ctk.CTkEntry(frame_left)
entry_a.pack(pady=5)

label_b = ctk.CTkLabel(frame_left, text="B:")
label_b.pack(pady=5)
entry_b = ctk.CTkEntry(frame_left)
entry_b.pack(pady=5)

# Right CD grid
frame_right = ctk.CTkFrame(frame)
frame_right.pack(side="right", padx=10)

label_c = ctk.CTkLabel(frame_right, text="C:")
label_c.pack(pady=5)
entry_c = ctk.CTkEntry(frame_right)
entry_c.pack(pady=5)

label_d = ctk.CTkLabel(frame_right, text="D:")
label_d.pack(pady=5)
entry_d = ctk.CTkEntry(frame_right)
entry_d.pack(pady=5)

# choose
var = tk.StringVar(value="a")
radio_a = ctk.CTkRadioButton(app, text="Calculate A", variable=var, value="a")
radio_a.pack(side="top", pady=5)
radio_b = ctk.CTkRadioButton(app, text="Calculate B", variable=var, value="b")
radio_b.pack(side="top", pady=5)
radio_c = ctk.CTkRadioButton(app, text="Calculate C", variable=var, value="c")
radio_c.pack(side="top", pady=5)
radio_d = ctk.CTkRadioButton(app, text="Calculate D", variable=var, value="d")
radio_d.pack(side="top", pady=5)

# Calc Button
calculate_button = ctk.CTkButton(app, text="Calculate", command=calculate)
calculate_button.pack(pady=10)


result_label = ctk.CTkLabel(app, text="Result: ")
result_label.pack(pady=10)

result_label = ctk.CTkLabel(app, text="————— | Dev By: Ransa | —————")
result_label.pack(pady=10)

app.mainloop()



