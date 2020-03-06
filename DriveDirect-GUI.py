#GUI Version

import tkinter as tk
import pandas as pd

root= tk.Tk()

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
    
    link = entry1.get()

    downloadLink = str('')

    #Create direct URL
    downloadLink = link.replace('file/d/', 'uc?export=download&id=')
    downloadLink = downloadLink.replace('/view?usp=sharing', '')    

    finalLink = str(downloadLink)
    #Copy to clipboard
    print('final URL:', finalLink)
    df = pd.DataFrame([downloadLink])
    df.to_clipboard(index=False, header=False)
    
    label3 = tk.Label(root, text= finalLink ,font=('helvetica', 10))
    canvas1.create_window(250, 210, window=label3)
    
    label4 = tk.Label(root, text= finalLink ,font=('helvetica', 10, 'bold'))
    canvas1.create_window(250, 230, window=finalLink)


    
    
button1 = tk.Button(text='Get Your Link (and copy to the clipboard)', command=getDownloadURL, bg='white', fg='black', font=('helvetica', 9, 'bold'))
canvas1.create_window(250, 175, window=button1)

#button2 = tk.Button(text='Copy Download Link', command=copyURL, bg='white', fg='black', font=('helvetica', 9, 'bold'))
#canvas1.create_window(300, 180, window=button2)

root.mainloop()
