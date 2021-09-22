import tkinter as tk

root = tk.Tk()
root.title("Maths Calculator Version 2.0 // Home Page")
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg="#113e53")

header_label = tk.Label(root, text="Maths Calculator Version 2.0", fg="#73fbd3", bg="#113e53", font=("Calibri", 30, "underline", "bold"))
header_label.pack(pady=50)

choices_frame = tk.Frame(root, bg="#107e88", width=300, height=300)
choices_frame.pack(pady=20)
choices_frame.pack_propagate(False)

button_frame = tk.Frame(choices_frame, bg="#107e88")
button_frame.pack(pady=50)

real_numbers_button = tk.Button(button_frame, text="Real Numbers", bg="#73fbd3", width=20, height=2)
real_numbers_button.pack(pady=10)

imaginary_numbers_button = tk.Button(button_frame, text="Imaginary Numbers", bg="#73fbd3", width=20, height=2)
imaginary_numbers_button.pack(pady=10)

matricies_button = tk.Button(button_frame, text="Matricies", bg="#73fbd3", width=20, height=2)
matricies_button.pack(pady=10)

root.mainloop()
