from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox

class ImageConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Image Converter")
        self.root.geometry("400x200")
        self.setup_ui()

    def setup_ui(self):
        # Create and pack widgets
        title_label = tk.Label(self.root, text="JPEG to PNG Converter", font=("Arial", 16))
        title_label.pack(pady=10)

        convert_button = tk.Button(self.root, text="Select Image", command=self.process_image)
        convert_button.pack(pady=20)

        self.status_label = tk.Label(self.root, text="", wraplength=350)
        self.status_label.pack(pady=10)

    def is_jpeg(self, filename):
        return filename.lower().endswith(('.jpg', '.jpeg'))

    def is_png(self, filename):
        return filename.lower().endswith('.png')

    def convert_to_png(self, input_path):
        # Get the directory and filename without extension
        output_dir = os.path.dirname(input_path)
        filename = os.path.splitext(os.path.basename(input_path))[0]
        
        # Create output path
        output_path = os.path.join(output_dir, f"{filename}.png")
        
        # Open and convert image
        with Image.open(input_path) as img:
            img.save(output_path, 'PNG')
        
        return output_path

    def process_image(self):
        input_file = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png")],
            title="Choose an image file"
        )
        
        if not input_file:
            return

        try:
            if self.is_jpeg(input_file):
                self.status_label.config(text="Converting JPEG to PNG...")
                self.root.update()
                
                output_path = self.convert_to_png(input_file)
                self.status_label.config(text=f"Conversion complete!\nSaved as: {os.path.basename(output_path)}")
                messagebox.showinfo("Success", "Image converted successfully!")
                
            elif self.is_png(input_file):
                self.status_label.config(text="File is already a PNG.")
                messagebox.showinfo("Info", "Selected file is already in PNG format.")
                
            else:
                self.status_label.config(text="Unsupported file format.")
                messagebox.showerror("Error", "Unsupported file format. Please select a JPEG or PNG file.")

        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def run(self):
        self.root.mainloop()

def main():
    app = ImageConverter()
    app.run()

if __name__ == "__main__":
    main()
