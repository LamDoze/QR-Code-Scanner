import cv2
from pyzbar.pyzbar import decode
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def read_qr_code(image_path):
    try:
        image = cv2.imread(image_path)
        qr_codes = decode(image)
        
        for qr in qr_codes:
            data = qr.data.decode('utf-8')  
            return data  # Trả về dữ liệu mã QR đầu tiên tìm thấy
        
        return None  # Không tìm thấy mã QR
    except Exception as e:
        result_text.set(f"Lỗi: {str(e)}")
        return None
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", ".png;.jpg;*.jpeg;*.bmp")])
    if file_path:
        display_image(file_path)
        
        result = read_qr_code(file_path) 
        if result:
            result_text.set(f"Kết quả: {result}")
        else:
            result_text.set("Không nhận diện được mã QR")

def display_image(image_path):
    img = Image.open(image_path)
    img = img.resize((300, 300))  
    img_tk = ImageTk.PhotoImage(img)
    
    img_label.config(image=img_tk)
    img_label.image = img_tk  

# Tạo giao diện chính
root = tk.Tk()
root.title("QR Code Scanner")
root.geometry("500x700")
root.configure(bg="#2E2E2E")  # Đặt nền màu tối
root.resizable(False, False)

# Tiêu đề ứng dụng
title_frame = tk.Frame(root, bg="#2E2E2E")
title_frame.pack(pady=30)

title_label = tk.Label(title_frame, text="QR Scanner", font=("Helvetica", 30, "bold"), fg="#FFD700", bg="#2E2E2E")
title_label.pack()

# Nút chọn ảnh
btn_frame = tk.Frame(root, bg="#2E2E2E")
btn_frame.pack(pady=10)

btn_open = tk.Button(btn_frame, text="Chọn ảnh", command=open_image, font=("Helvetica", 15), bg="#FFD700", fg="#2E2E2E", padx=20, pady=10)
btn_open.pack()

# Khu vực hiển thị ảnh
img_label = tk.Label(root, bg="#2E2E2E")
img_label.pack(pady=20)

# Thông tin kết quả
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 12), fg="white", bg="#2E2E2E", wraplength=400, justify="center")
result_label.pack(pady=20)

# Bắt đầu vòng lặp chính của Tkinter
root.mainloop()
