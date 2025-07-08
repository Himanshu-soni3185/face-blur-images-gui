import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Face blur function
def blur_faces(image_path, output_path="face-blur/face-blur-images-gui/blurred_files/blurred_image.jpg"):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
    
    image = cv2.imread(image_path)
    if image is None:
        print("❌ Could not open or find the image:", image_path)
        return None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3)
    print(f"🧠 Faces Detected: {len(faces)}")

    if len(faces) == 0:
        print("⚠️ No faces detected.")
        return None

    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        blurred = cv2.GaussianBlur(face, (99, 99), 30)
        image[y:y+h, x:x+w] = blurred

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, image)
    print(f"✅ Blurred image saved at: {os.path.abspath(output_path)}")
    return output_path

# GUI App
class FaceBlurApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Blur Tool")
        self.root.geometry("1200x600")
        self.root.configure(bg="#f0f0f0")

        # Button
        self.select_button = tk.Button(
            root, text="Choose Image File", command=self.select_image, font=("Arial", 14)
        )
        self.select_button.pack(pady=20)

        # Frames for original and blurred image
        frame = tk.Frame(root)
        frame.pack()

        self.original_label = tk.Label(frame, text="Original Image", font=("Arial", 12))
        self.original_label.grid(row=0, column=0, padx=30)
        self.blurred_label = tk.Label(frame, text="Blurred Image", font=("Arial", 12))
        self.blurred_label.grid(row=0, column=1, padx=30)

        self.original_image_display = tk.Label(frame)
        self.original_image_display.grid(row=1, column=0, padx=30)

        self.blurred_image_display = tk.Label(frame)
        self.blurred_image_display.grid(row=1, column=1, padx=30)

    def select_image(self):
        filepath = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
        )
        if not filepath:
            return

        # Show original image
        self.display_image(filepath, self.original_image_display)

        # Process and blur
        output_path = "blurred_files/blurred_output.jpg"
        blurred_path = blur_faces(filepath, output_path)

        if blurred_path:
            self.display_image(blurred_path, self.blurred_image_display)
            messagebox.showinfo("Success", "Faces blurred successfully.")
        else:
            self.blurred_image_display.config(image='')
            messagebox.showwarning("No Faces", "No faces found or invalid image.")

    def display_image(self, img_path, label):
        img = Image.open(img_path)
        img.thumbnail((500, 400))
        img_tk = ImageTk.PhotoImage(img)
        label.config(image=img_tk)
        label.image = img_tk  # Prevent garbage collection

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = FaceBlurApp(root)
    root.mainloop()
