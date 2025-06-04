import tkinter as tk
from tkinter import messagebox

def proses_pembayaran():
    invoice = entry_invoice.get()
    if invoice and invoice != placeholder_text:
        status_label.config(text="Pembayaran Berhasil", fg="green")
        tampilkan_data_mahasiswa()
    else:
        status_label.config(text="Belum melakukan pembayaran", fg="red")

def tampilkan_data_mahasiswa():
    # Data dummy mahasiswa – bisa diganti sesuai kebutuhan
    nama_mahasiswa = "Dina Lestari"
    nim_mahasiswa = "231234567"
    prodi_mahasiswa = "Teknik Informatika"

    # Menampilkan data mahasiswa
    label_nama.config(text=f"Nama: {nama_mahasiswa}")
    label_nim.config(text=f"NIM: {nim_mahasiswa}")
    label_prodi.config(text=f"Prodi: {prodi_mahasiswa}")
   
def buka_pengisian_krs():
    messagebox.showinfo("Pengisian KRS", "Menu Pengisian KRS akan dibuka.")

def on_entry_click(event):
    if entry_invoice.get() == placeholder_text:
        entry_invoice.delete(0, "end")
        entry_invoice.config(fg="black")

def on_focusout(event):
    if entry_invoice.get() == "":
        entry_invoice.insert(0, placeholder_text)
        entry_invoice.config(fg="grey")

# Window utama
root = tk.Tk()
root.title("Pembayaran dan Pengisian KRS")
root.geometry("300x350")
root.configure(bg="white")

# Ikon user (menggunakan karakter Unicode)
icon_label = tk.Label(root, text="👤", font=("Arial", 20), bg="white")
icon_label.pack(pady=(10, 5))

# Tombol Bayar
btn_bayar = tk.Button(root, text="Bayar", bg="green", fg="white", font=("Arial", 10, "bold"),
                      command=proses_pembayaran)
btn_bayar.pack(pady=5)

# Entry No Invoice
placeholder_text = "NO. Invoice"
entry_invoice = tk.Entry(root, font=("Arial", 10), fg="grey")
entry_invoice.insert(0, placeholder_text)
entry_invoice.bind("<FocusIn>", on_entry_click)
entry_invoice.bind("<FocusOut>", on_focusout)
entry_invoice.pack(pady=5)

# Status pembayaran
status_label = tk.Label(root, text="Belum melakukan pembayaran", fg="red", font=("Arial", 9), bg="white")
status_label.pack(pady=5)

# Label info mahasiswa (kosong dulu, nanti muncul setelah bayar)
label_nama = tk.Label(root, text="", bg="white", font=("Arial", 10))
label_nama.pack()

label_nim = tk.Label(root, text="", bg="white", font=("Arial", 10))
label_nim.pack()

label_prodi = tk.Label(root, text="", bg="white", font=("Arial", 10))
label_prodi.pack()

label_krs_status = tk.Label(root, text="", bg="white", font=("Arial", 10, "italic"))
label_krs_status.pack(pady=(5, 10))

# Tombol KRS
btn_krs = tk.Button(root, text="Pengisian KRS", bg="blue", fg="white", font=("Arial", 10, "bold"),
                    command=buka_pengisian_krs)
btn_krs.pack(pady=5)

# Jalankan aplikasi
root.mainloop()
