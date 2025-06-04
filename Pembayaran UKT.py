import tkinter as tk
from tkinter import messagebox, simpledialog

# 1. Fungsi Memilih Metode Pembayaran
def pilih_metode(nama_bank):
    metode_pembayaran.set(nama_bank)
    messagebox.showinfo("Info", f"Anda memilih {nama_bank}.\nKlik 'Bayar Sekarang' untuk melanjutkan.")

# 2. Fungsi Proses Pembayaran dengan Input Invoice
def bayar():
    metode = metode_pembayaran.get()
    if not metode:
        messagebox.showwarning("Peringatan", "Silakan pilih metode pembayaran terlebih dahulu.")
        return

    invoice = simpledialog.askstring("Input No. Invoice", "Masukkan No. Invoice Anda:")
    if invoice is None or invoice.strip() == "":
        messagebox.showwarning("Peringatan", "No. Invoice tidak boleh kosong.")
        return

    # Data mahasiswa sesuai Invoice 
    nim = "230212018"
    nama = "Tin Salwa"

    # Tampilkan data mahasiswa berdasarkan invoice
    konfirmasi_data = messagebox.askyesno(
        "Konfirmasi Data",
        f"Data Mahasiswa:\n\nNIM : {nim}\nNama: {nama}\n\nApakah data ini benar?"
    )

    if konfirmasi_data:
        messagebox.showinfo("Pembayaran Berhasil", f"Pembayaran berhasil menggunakan metode {metode}.")
        messagebox.showinfo("Bukti Pembayaran", f"Tagihan untuk NIM {nim} a.n. {nama} telah berhasil diproses.")
    else:
        messagebox.showinfo("Dibatalkan", "Silakan periksa kembali data Anda.")

root = tk.Tk()
root.title("GUI Pembayaran UKT")
root.geometry("420x400")
root.configure(bg="#f7f7f7")

# 4. Variabel untuk Menyimpan Metode Pembayaran
metode_pembayaran = tk.StringVar()

frame_header = tk.Frame(root, bg="#f7f7f7")
frame_header.pack(pady=10)

tk.Label(frame_header, text="Tin Salwa", font=("Arial", 14, "bold"), bg="#f7f7f7").pack()
tk.Label(frame_header, text="Dashboard Mahasiswa", font=("Arial", 10), fg="blue", bg="#f7f7f7").pack()

# 6. Frame Konten Utama
frame_content = tk.Frame(root, bg="#f7f7f7")
frame_content.pack(pady=10)

# Label Tagihan
tk.Label(frame_content, text="Total Tagihan:", font=("Arial", 10), bg="#f7f7f7").grid(row=0, column=0, sticky="w")
tk.Label(frame_content, text="Rp 3.400.000", font=("Arial", 10, "bold"), bg="#f7f7f7").grid(row=0, column=1, sticky="w")

# Label Metode Pembayaran
tk.Label(frame_content, text="Pilih metode pembayaran:", font=("Arial", 10), bg="#f7f7f7").grid(
    row=1, column=0, columnspan=2, sticky="w", pady=(15, 5)
)

# 7. Frame Bank dan Tombol Metode Pembayaran
frame_bank = tk.Frame(frame_content, bg="#f7f7f7")
frame_bank.grid(row=2, column=0, columnspan=2)

btn_aceh = tk.Button(
    frame_bank, text="Bank Aceh", width=18, font=("Arial", 8),
    bg="#4CAF50", fg="white", command=lambda: pilih_metode("Bank Aceh")
)
btn_aceh.pack(pady=3)

btn_bsi = tk.Button(
    frame_bank, text="Bank BSI", width=18, font=("Arial", 8),
    bg="#2196F3", fg="white", command=lambda: pilih_metode("Bank BSI")
)
btn_bsi.pack(pady=3)

# 8.  pemberitahuan
tk.Label(frame_content, text="NIM:", font=("Arial", 10), bg="#f7f7f7").grid(
    row=3, column=0, sticky="w", pady=15
)
tk.Label(frame_content, text="230212018", font=("Arial", 10), bg="#f7f7f7").grid(
    row=3, column=1, sticky="w"
)

# 9. Tombol Bayar Sekarang
btn_bayar = tk.Button(
    root, text="Bayar Sekarang", command=bayar,
    bg="#FF5722", fg="white", font=("Arial", 10, "bold"), width=20
)
btn_bayar.pack(pady=15)

# 10. Jalankan Aplikasi
root.mainloop()
