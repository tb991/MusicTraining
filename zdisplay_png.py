import tkinter as tk
from PIL import Image, ImageTk
import time
import rnd_image as f
def show_png_image(image_path):
    img = Image.open(image_path)
    img = img.resize((400, 1200))  # Optional: Resize the image to fit the window
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo

# Create the tkinter window
root = tk.Tk()
root.title("Display PNG Image")
path = '/home/tom/Pictures/notes/png/'
# Replace 'path/to/your/image.png' with the actual path to your first .png image file
first_image_path = path + f.getRndFile()

# Load and show the first image
label = tk.Label(root)
label.pack()
show_png_image(first_image_path)
root.update()

new_image_path = ""
while True:
	# Wait for 5 seconds before changing the image
	input()

	oldImg = new_image_path
	# Replace 'path/to/your/new_image.png' with the actual path to your new .png image file
	new_image_path = path + f.getRndFile()
	
	while oldImg == new_image_path:
		new_image_path = path + f.getRndFile()

	# Load and show the new image
	show_png_image(new_image_path)
	root.update()

# Start the tkinter event loop
root.mainloop()
