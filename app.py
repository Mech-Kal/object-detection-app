import tkinter as tk
from tkinter import filedialog, messagebox
from detect import detecting  # Import your detection function
import os

def upload_image():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        image_path.set(file_path)

def process_image():
    if not image_path.get() or not image_name.get():
        messagebox.showwarning("Input Error", "Please select an image and enter a name.")
        return

    
    try:
        # Call the detect_objects function with the correct arguments

        do = detecting(image_path.get(), image_name.get())
        do.detect()
        messagebox.showinfo("Success", f"Detection completed. Images saved in {image_name}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Object Detection App")

# Variables to store image path and name
image_path = tk.StringVar()
image_name = tk.StringVar()

# Create and place widgets
tk.Label(root, text="Selected Image:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=image_path, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Upload Image", command=upload_image).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Image Name:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=image_name).grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Detect Objects", command=process_image).grid(row=2, column=1, padx=10, pady=20)

# Run the application
root.mainloop()