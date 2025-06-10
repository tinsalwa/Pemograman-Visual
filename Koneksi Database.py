import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3
from datetime import datetime

# Koneksi pembuatan database
conn = sqlite3.connect("ukt_pembayaran.db")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS pembayaran (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nim TEXT,
        nama TEXT,
        metode TEXT,
        invoice TEXT,
        tanggal TEXT,
        jam TEXT,
        hari TEXT
    )
""")
conn.commit()

# Struk pembayaran
def tampilkan_struk_pembayaran(nim, nama, metode, invoice, tanggal, jam, hari):
    struk_window = tk.Toplevel(root)
    struk_window.geometry("500x500")
    struk_window.configure(bg="#ffffff")

    # Header
    header = tk.Frame(struk_window, bg="#1976D2", height=60)
    header.pack(fill="x")
    tk.Label(header, text="Bukti Pembayaran UKT", font=("Arial", 14, "bold"), fg="white", bg="#1976D2").pack(pady=10)

    # Informasi jurusan
    subheader = tk.Frame(struk_window, bg="white")
    subheader.pack(pady=(5, 10))
    tk.Label(subheader, text="Pendidikan Teknologi Informasi", font=("Arial", 10, "bold"), bg="white").pack()
    tk.Label(subheader, text="Fakultas Tarbiyah dan Keguruan", font=("Arial", 10), bg="white").pack()
    tk.Label(subheader, text="UIN Ar-Raniry Banda Aceh", font=("Arial", 10), bg="white").pack()

    # Isi struk
    isi = tk.Frame(struk_window, bg="white", padx=20, pady=10)
    isi.pack(fill="both", expand=True)

    tk.Label(isi, text="Struk Pembayaran", font=("Arial", 11, "bold"), bg="white", fg="black").pack(pady=(0, 10))

    data = [
        ("Tanggal", tanggal),
        ("Jam", jam),
        ("Hari", hari),
        ("NIM", nim),
        ("Nama", nama),
        ("Metode", metode),
        ("Invoice", invoice),
        ("Total Bayar", "Rp 3.400.000")
    ]

    for label, value in data:
        baris = tk.Frame(isi, bg="white")
        baris.pack(fill="x", pady=2)
        tk.Label(baris, text=f"{label}:", width=12, anchor="w", bg="white", font=("Arial", 9, "bold")).pack(side="left")
        tk.Label(baris, text=value, anchor="w", bg="white", font=("Arial", 9)).pack(side="left")

    tk.Label(isi, text="\nTransaksi berhasil!\nSimpan bukti ini sebagai arsip Anda.", bg="white", font=("Arial", 9), fg="green").pack(pady=15)

    tk.Button(struk_window, text="Selesai", command=struk_window.destroy, bg="#388E3C", fg="white", font=("Arial", 10, "bold"), width=15).pack(pady=10)

# Fungsi pilih metode
def pilih_metode(nama_bank):
    metode_pembayaran.set(nama_bank)
    messagebox.showinfo("Metode Pembayaran", f"Metode {nama_bank} dipilih.")

# Fungsi proses pembayaran
def proses_pembayaran():
    metode = metode_pembayaran.get()
    if not metode:
        messagebox.showwarning("Peringatan", "Silakan pilih metode pembayaran!")
        return

    invoice = simpledialog.askstring("Input Invoice", "Masukkan Nomor Invoice:")
    if not invoice:
        messagebox.showwarning("Peringatan", "Nomor Invoice tidak boleh kosong.")
        return

    nim = "230212018"
    nama = "Tin Salwa"

    waktu = datetime.now()
    tanggal = waktu.strftime("%Y-%m-%d")
    jam = waktu.strftime("%H:%M:%S")
    hari = waktu.strftime("%A")

    confirm = messagebox.askyesno("Konfirmasi", f"Data Anda:\nNIM: {nim}\nNama: {nama}\nInvoice: {invoice}\nMetode: {metode}\n\nLanjutkan?")
    if not confirm:
        return

    cur.execute("INSERT INTO pembayaran (nim, nama, metode, invoice, tanggal, jam, hari) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (nim, nama, metode, invoice, tanggal, jam, hari))
    conn.commit()

    messagebox.showinfo("Sukses", "Pembayaran berhasil dilakukan!")
    tampilkan_struk_pembayaran(nim, nama, metode, invoice, tanggal, jam, hari)

# Fungsi tampil histori
def tampil_histori():
    histori_window = tk.Toplevel(root)
    histori_window.title("Histori Pembayaran")
    histori_window.geometry("900x500")
    histori_window.configure(bg="#ffffff")

    columns = ("id", "NIM", "Nama", "Metode", "Invoice", "Tanggal", "Jam", "Hari")
    tree = ttk.Treeview(histori_window, columns=columns, show="headings", height=12)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=85 if col == "id" else 100)

    cur.execute("SELECT * FROM pembayaran")
    for row in cur.fetchall():
        tree.insert("", tk.END, values=row)

    tree.pack(fill="both", expand=True, padx=10, pady=10)

    def hapus_histori():
        if messagebox.askyesno("Hapus Histori", "Ingin menghapus seluruh histori pembayaran?"):
            cur.execute("DELETE FROM pembayaran")
            cur.execute("DELETE FROM sqlite_sequence WHERE name='pembayaran'")
            conn.commit()
            tree.delete(*tree.get_children())
            messagebox.showinfo("Berhasil", "Seluruh histori berhasil dihapus.")

    tk.Button(histori_window, text="Hapus Semua Histori", bg="#D32F2F", fg="white", font=("Arial", 10), command=hapus_histori).pack(pady=5)

# GUI Utama
root = tk.Tk()
root.title("Aplikasi Pembayaran UKT Mahasiswa")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

metode_pembayaran = tk.StringVar()

frame_header = tk.Frame(root, bg="#f0f0f0")
frame_header.pack(pady=15)
tk.Label(frame_header, text="TIN SALWA", font=("Arial", 16, "bold"), bg="#f0f0f0").pack()
tk.Label(frame_header, text="Dashboard Pembayaran UKT", font=("Arial", 10), bg="#f0f0f0").pack()

frame_content = tk.Frame(root, bg="#f0f0f0")
frame_content.pack(pady=10)

tk.Label(frame_content, text="Total Tagihan:", font=("Arial", 10), bg="#f0f0f0").grid(row=0, column=0, sticky="w")
tk.Label(frame_content, text="Rp 3.400.000", font=("Arial", 10, "bold"), bg="#f0f0f0").grid(row=0, column=1, sticky="w")

tk.Label(frame_content, text="Pilih Metode Pembayaran:", font=("Arial", 10), bg="#f0f0f0").grid(row=1, column=0, columnspan=2, pady=(15, 5), sticky="w")

frame_bank = tk.Frame(frame_content, bg="#f0f0f0")
frame_bank.grid(row=2, column=0, columnspan=2)

tk.Button(frame_bank, text="Bank Aceh", width=20, bg="#4CAF50", fg="white", font=("Arial", 9), command=lambda: pilih_metode("Bank Aceh")).pack(pady=5)
tk.Button(frame_bank, text="Bank BSI", width=20, bg="#2196F3", fg="white", font=("Arial", 9), command=lambda: pilih_metode("Bank BSI")).pack(pady=5)

tk.Label(frame_content, text="NIM:", font=("Arial", 10), bg="#f0f0f0").grid(row=3, column=0, sticky="w", pady=15)
tk.Label(frame_content, text="230212018", font=("Arial", 10), bg="#f0f0f0").grid(row=3, column=1, sticky="w")

tk.Button(root, text="Bayar Sekarang", width=25, bg="#FF5722", fg="white", font=("Arial", 10, "bold"), command=proses_pembayaran).pack(pady=10)
tk.Button(root, text="Lihat Histori Pembayaran", width=25, bg="#673AB7", fg="white", font=("Arial", 10), command=tampil_histori).pack(pady=5)

root.mainloop()
