from tkinter import *
from tkinter.messagebox import*
from qrcode import *
from PIL import Image,ImageTk

root = Tk()
root.title("QR Code Generator")
root.geometry("500x600+200+20")
f = ("Arial",30,"bold")

def gq():
	url = ent_url.get()
	if url =="":
		showerror("issue","url is empty")
		ent_url.focus()
		return
	img = make(url)
	img.save("qr.png")
	new_size = (300,300)
	resized_img = img.resize(new_size)
	resized_img.save("qr.png")
	img = Image.open("qr.png")
	imgtk = ImageTk.PhotoImage(image=img)
	lab_qr.configure(image=imgtk)
	lab_qr.photo = imgtk

lab_url = Label(root, text="enter url",font=f)
ent_url = Entry(root, font=f)
btn_generate = Button(root,text="Generate QR Code",font=f, command=gq)
lab_qr = Label(root, font=f)

lab_url.pack(pady=5)
ent_url.pack(pady=5)
btn_generate.pack(pady=5)
lab_qr.pack(pady=5)

root.mainloop()