import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ExifTags

class ExifGoruntulemeUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Exif Kontrol")

        self.arayuz_olustur()

    def arayuz_olustur(self):
        self.etiket = tk.Label(self.root, text="0xc184 tarafından ♡ ile yapılmıştır ")
        self.etiket.pack(pady=10)

        self.dosya_secme_dugmesi = tk.Button(self.root, text="Exif Göster", command=self.resim_yukle)
        self.dosya_secme_dugmesi.pack(side=tk.LEFT, padx=5, pady=10)

        self.exif_silme_dugmesi = tk.Button(self.root, text="Exif Bilgilerini Sil", command=self.exif_sil)
        self.exif_silme_dugmesi.pack(side=tk.LEFT, padx=5, pady=10)

        self.metin_alani = tk.Text(self.root, wrap=tk.WORD, width=40, height=10)
        self.metin_alani.pack(pady=10)

    def resim_yukle(self):
        dosya_yolu = filedialog.askopenfilename(filetypes=[("Resim dosyaları", "*.jpg;*.jpeg;*.png")])

        if dosya_yolu:
            exif_bilgisi = self.exif_bilgisi_al(dosya_yolu)
            self.exif_bilgisini_goster(exif_bilgisi)

    def exif_bilgisi_al(self, dosya_yolu):
        exif_bilgisi = ""
        try:
            resim = Image.open(dosya_yolu)
            exif_info = resim._getexif()

            if exif_info:
                for tag, deger in exif_info.items():
                    tag_adi = ExifTags.TAGS.get(tag, tag)
                    exif_bilgisi += f"{tag_adi}: {deger}\n"

        except Exception as hata:
            exif_bilgisi = f"Hata: {str(hata)}"

        return exif_bilgisi

    def exif_bilgisini_goster(self, exif_bilgisi):
        self.metin_alani.delete(1.0, tk.END)
        self.metin_alani.insert(tk.END, exif_bilgisi)

    def exif_sil(self):
        dosya_yolu = filedialog.askopenfilename(filetypes=[("Resim dosyaları", "*.jpg;*.jpeg;*.png")])

        if dosya_yolu:
            try:
                resim = Image.open(dosya_yolu)
                resim.save(dosya_yolu, exif="")
                messagebox.showinfo("Bilgi", "Exif bilgileri başarıyla silindi.")
            except Exception as hata:
                messagebox.showerror("Hata", f"Exif bilgilerini silme başarısız: {str(hata)}")

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = ExifGoruntulemeUygulamasi(root)
    root.mainloop()