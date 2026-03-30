import tkinter as tk
from tkinter import messagebox

# Hàm xử lý Mã hóa
def encrypt_action():
    plaintext = entry_text.get()
    if not plaintext:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập văn bản cần mã hóa!")
        return
    # Logic mô phỏng ECC: Đảo ngược chuỗi và thêm tiền tố
    encrypted = f"ECC_ENCRYPTED[{plaintext[::-1]}]"
    label_result.config(text=f"Bản mã: {encrypted}", fg="blue")

# Hàm xử lý Giải mã
def decrypt_action():
    ciphertext = entry_text.get()
    if not ciphertext:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập bản mã cần giải!")
        return
    
    # Xử lý thông minh: Tự động loại bỏ tiền tố nếu người dùng copy nguyên cụm
    clean_text = ciphertext.replace("ECC_ENCRYPTED[", "").replace("]", "")
    # Đảo ngược lại để về bản rõ ban đầu
    decrypted = clean_text[::-1]
    
    label_result.config(text=f"Bản rõ: {decrypted}", fg="green")

# --- Giao diện chương trình ---
root = tk.Tk()
root.title("ECC Tool - Võ Nguyễn Huỳnh Hương")
root.geometry("450x350")

tk.Label(root, text="MÃ HÓA & GIẢI MÃ ECC", font=("Arial", 14, "bold")).pack(pady=15)

tk.Label(root, text="Nhập nội dung vào đây:", font=("Arial", 10)).pack()
entry_text = tk.Entry(root, width=45, font=("Arial", 10))
entry_text.pack(pady=10)

# Khung chứa 2 nút riêng biệt
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_encrypt = tk.Button(button_frame, text="MÃ HÓA ECC", command=encrypt_action, 
                        bg="#add8e6", width=15, font=("Arial", 9, "bold"))
btn_encrypt.grid(row=0, column=0, padx=10)

btn_decrypt = tk.Button(button_frame, text="GIẢI MÃ ECC", command=decrypt_action, 
                        bg="#90ee90", width=15, font=("Arial", 9, "bold"))
btn_decrypt.grid(row=0, column=1, padx=10)

tk.Label(root, text="--- KẾT QUẢ ---", font=("Arial", 10, "italic")).pack(pady=10)
label_result = tk.Label(root, text="Chưa có dữ liệu", font=("Arial", 11, "bold"), wraplength=400)
label_result.pack()

root.mainloop()