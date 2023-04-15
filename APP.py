import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
#from PIL import ImageTk,Image

#Declarando lista de palavras proibidas:
Proibidas = [merda, caralho, coca, xuxa] 

#window 
window = ttk.Window(themename = 'darkly')
window.iconbitmap('C:/Users/Julio/Desktop/icone.ico')
window.title('Demo')
window.configure(bg ='#474446')
window.geometry('300x150')


#cometarios = []

#title
title_label = ttk.Label(master = window, text = 'Deixe um comentário', font = 'Calibri 24')
title_label.pack()


#função comentar
def comentar(Novo_elemento = [], MyLabel = [], comentarios = []):
    comentarios.append(string_entrada.get())
    #output_string.set(Novo_elemento)
    MyLabel.append(ttk.Label(
        master = window,
        text = comentarios[-1],
        background= '#f54260',
        font = 'Calibri 24'
       #textvariable= comentarios[i]
       ))
    MyLabel[-1].pack(pady = 10)
    print(len(comentarios))
    print(comentarios)

#input field
input_frame = ttk.Frame(master = window)
string_entrada = tk.StringVar()    
entry = ttk.Entry(master = input_frame, textvariable = string_entrada, width=50)
button =  ttk.Button(master = input_frame, text = 'Enviar', command = comentar)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack( pady = 10)


#output 
output_string = tk.StringVar()
 

#ComentLable
#MyLabel = []
#for i in range(len(comentarios)):
#    MyLabel.append(ttk.Label(
#      master = window,
#       text = comentarios[i],
 #      background= '#f54260',
#       font = 'Calibri 24',
#       #textvariable= output_string
 #      ))
#
#for i in range(len(comentarios)):
 #  MyLabel[i].pack(pady = 10)



#run 
window.mainloop()