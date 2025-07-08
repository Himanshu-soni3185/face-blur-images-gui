# 🖼️ Face Blur – Image GUI (Python + Tkinter + OpenCV)

A simple and user-friendly GUI application that detects and blurs faces in **PNG/JPG image files** using Python and OpenCV.

## 📌 Features

- ✅ Upload image files through a graphical interface (Tkinter)
- ✅ Detects human faces using Haar Cascade Classifier
- ✅ Applies Gaussian blur to detected face regions
- ✅ Saves the blurred image in a local folder
- ✅ Works offline, lightweight and fast

---

## 🛠️ Tech Stack

- **Python 3.13.2
- **OpenCV** (`cv2`) – For face detection and image processing
- **Tkinter** – For building the graphical user interface
- **PIL (Pillow)** – For image handling and preview in GUI
- **os** – For directory management


---

## 📷 GUI Preview

![GUI Screenshot](screenshorts\gui-image-blur.png)

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/face-blur-images-gui.git

# Install dependencies
pip install opencv-python Pillow

# Run the app
python app.py
