from tkinter import*
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest

    trans=Translator()
    trans1=trans.translate(text,src = src1,dest = dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0,END)
    textget = change(text = masg,src = s,dest = d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)

root = Tk()
root.title("Google Translator")
root.geometry("500x1000")
root.config(bg="Red")

lab_txt=Label(root,text="Translator",font=("Times New Roman",40,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

frame=Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text",font=("Times New Roman",20,"bold"),fg="black",bg="red")
lab_txt.place(x=100,y=100,height=30,width=300)
Sor_txt=Text(frame,font=("Times New Roman",20,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=140,height=150,width=480)

list_text=list(LANGUAGES.values())

comb_sor=ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=40,width=100)
comb_sor.set("english")

button_change=Button(frame,text="Translate",relief=RAISED)
button_change.place(x=130,y=300,height=40,width=100)

comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=390,y=300,height=40,width=100)
comb_dest.set("english")

lab_txt=Label(root,text="Dest Text",font=("Times New Roman",20,"bold"),fg="black",bg="red")
lab_txt.place(x=100,y=360,height=30,width=300)

dest_txt=Text(frame,font=("Times New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)

root.mainloop()
