from tkinter import *
from PIL import ImageTk

class HOver_Effect:
    def __init__(self, root):
        self.root = root
        self.root.title("IMAGE HOVER EFFECT")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#262626")

        title=Label(self.root,text="IMAGE HOVER EFFECT IN PYTHON TKINTER",font=("times new roman",40,"bold")).place(x=0,y=50,relwidth=1)
        self.image_=ImageTk.PhotoImage(file="C:\\Users\\Adarsh kumar\\Documents\\Image-Hover-Effect\\1.jpg")

        self.y=0
        self.c=0
        self.lbl_img=Label(self.root,image=self.image_,bd=0,cursor="hand2")
        self.lbl_img.place(x=550,y=220)
        self.lbl_img.bind("<Enter>",self.hover_in)
        self.lbl_img.bind("<Leave>",self.hover_out)
        self.hover_function()

    def hover_in(self,ev):   
        self.c=1
        

    def hover_out(self,ev):
        self.c=0
          

    def hover_function(self):
       
        if self.c==1:
            if self.y!=-30:
                self.y-=1
            self.lbl_img.place(y=220+self.y)
        if self.c==0:
            if self.y!=0:
                self.y+=1
            self.lbl_img.place(y=220+self.y)

        self.lbl_img.after(15,self.hover_function)                

root=Tk()
obj = HOver_Effect(root)
root.mainloop()        