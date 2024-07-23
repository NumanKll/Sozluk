from tkinter import *
from tkinter import messagebox
import db
import os
import translate

mainscreen = Tk()
mainscreen.geometry("320x250+300+300")
mainscreen.resizable(width=False,height=FALSE)
mainscreen.title("Sözlük")
mainscreen.image_names()

if not os.path.exists("./databases.db"):
    msg=messagebox.showwarning("Veritabanı Dosyası Bulunamadı")
    cvp=messagebox.askyesno("Veritabanı Oluşturulsun mu?")
    if cvp:
        db.veritabanı_olustur()
    else:
        quit()

def arama():
    kelime=kelimeAra.get()
    aranan=db.kelime_Arama(kelime)
    kelimeAnlamı2["text"] = aranan[0][0]
    kelimeAnlamı4["text"] = aranan[0][1]

def kelime_Ekle():
    if kelimeEkle.get() == "" and kelimeAnlam.get() == "":
        messagebox.showerror("Uyarı","Kelime ve Anlamı Boş Bırakılamaz")
    else:
        kelime = kelimeEkle.get()
        anlam = kelimeAnlam.get() 
        db.kelime_ekleme(kelime,anlam)

def trans():
    if kelimeEkle.get() == "":
        messagebox.showerror("Uyarı","Kelime Boş Bırakılamaz")
    anlam = translate.sorgula(kelimeEkle.get())
    kelime = kelimeEkle.get()
    kelimeAnlamı2["text"] = kelime
    kelimeAnlamı4["text"] = anlam
    db.kelime_ekleme(kelime,anlam)
        
aramaEtiket=Label(text="Aranacak Kelimeyi Girin :")
aramaEtiket.place(x=10,y=10)
kelimeAra= Entry()
kelimeAra.place(x=160,y=12,width=150)
kelimeAraButton=Button(text="Ara",bg="gray", command=arama)
kelimeAraButton.place(x=10,y=34,width=300)

kelimeEkleEtiket = Label(text="Eklenecek Kelimeyi girin :")
kelimeEkleEtiket.place(x=10,y=62)
kelimeEkle = Entry()
kelimeEkle.place(x=160,y=64,width=150)

kelimeAnlamEtiket = Label(text="Kelime Anlamı girin :")
kelimeAnlamEtiket.place(x=10,y=87)
kelimeAnlam = Entry()
kelimeAnlam.place(x=160,y=89,width=150)
kelimeAraButton=Button(text="Ekle",bg="gray",command=kelime_Ekle)
kelimeAraButton.place(x=10,y=112,width=300)
kelimeAraButton=Button(text="Translate Sorgula",bg="gray",command=trans)
kelimeAraButton.place(x=10,y=140,width=300)

kelimeAnlamı1=Label(text="Kelime :",fg="red")
kelimeAnlamı1.place(x=10,y=170)
kelimeAnlamı2=Label(text="",fg="blue")
kelimeAnlamı2.place(x=55,y=170)
kelimeAnlamı3=Label(text="Kelime Anlamı :",fg="red")
kelimeAnlamı3.place(x=10,y=190)
kelimeAnlamı4=Label(text="")
kelimeAnlamı4.place(x=95,y=190)
mainloop()