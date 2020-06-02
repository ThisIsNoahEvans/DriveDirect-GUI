import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height = 230,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Google Drive Direct Download Link Generator')
label1.config(font=('helvetica', 20))
canvas1.create_window(250, 40, window=label1)

label2 = tk.Label(root, text='Enter your URL:')
label2.config(font=('helvetica', 10))
canvas1.create_window(250, 75, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(250, 125, window=entry1)

def getDownloadURL ():
	downloadLink = (((entry1.get().replace('file/d/', 'uc?export=download&id=')).replace('/view?usp=sharing', '')).replace('/view', ''))

	root.clipboard_clear()
	root.clipboard_append(downloadLink)

	label3 = tk.Label(root, text=downloadLink ,font=('helvetica', 10, 'bold'))
	label3.pack()

button1 = tk.Button(text='Get Your Link (And Copy To The Clipboard)', command=getDownloadURL, bg='white', fg='black', font=('helvetica', 9, 'bold'))
canvas1.create_window(250, 175, window=button1)

root.mainloop()
