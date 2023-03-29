import tkinter as tk

#function to calculate the area of the floor
def calculate_floor_area():
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        floor_area = length * width
        floor_area_label.config(text=f"Area of the floor: {floor_area:.2f} sq. meters")
    except ValueError:
        floor_area_label.config(text="Invalid input, please enter a number")

#function to calculate the amount of paint required to paint the walls
def calculate_paint_amount():
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        height = float(height_entry.get())
        wall_area = (2 * length * height) + (2 * width * height)
        paint_amount = wall_area / 7    #Assuming 1L of paint covers 7 sq. meters
        paint_amount_label.config(text=f"Amount of paint required: {paint_amount:.2f} L")
    except ValueError:
        paint_amount_label.config(text="Invalid input, please enter a number")

#function to calculate the volume of the room
def calculate_volume():
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        height = float(height_entry.get())
        volume = length * width * height
        volume_label.config(text=f"Volume of the room: {volume:.2f} cubic meters")
    except ValueError:
        volume_label.config(text="Invalid input, please enter a number")

#creating Tkinter window
window = tk.Tk()
window.title("Room Calculator")

#labels and entry fields for length, width, and height
length_label = tk.Label(window, text="Length (m):")
length_label.grid(row=0, column=0)
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1)

width_label = tk.Label(window, text="Width (m):")
width_label.grid(row=1, column=0)
width_entry = tk.Entry(window)
width_entry.grid(row=1, column=1)

height_label = tk.Label(window, text="Height (m):")
height_label.grid(row=2, column=0)
height_entry = tk.Entry(window)
height_entry.grid(row=2, column=1)

#buttons to calculate the floor area, paint amount, and volume
floor_area_button = tk.Button(window, text="Calculate Floor Area", command=calculate_floor_area)
floor_area_button.grid(row=3, column=0)

paint_amount_button = tk.Button(window, text="Calculate Paint Amount", command=calculate_paint_amount)
paint_amount_button.grid(row=3, column=1)

volume_button = tk.Button(window, text="Calculate Volume", command=calculate_volume)
volume_button.grid(row=3, column=2)

#labels to display the results
floor_area_label = tk.Label(window, text="")
floor_area_label.grid(row=4, column=0)

paint_amount_label = tk.Label(window, text="")
paint_amount_label.grid(row=4, column=1)

volume_label = tk.Label(window, text="")
volume_label.grid(row=5, column=1)

#start the GUI event loop
window.mainloop()

