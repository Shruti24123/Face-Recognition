from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class ChatBot:
    def __init__(self,root):
       self.root=root
       self.root.title("ChatBot")
       self.root.geometry("600x550+0+0")
       self.root.bind('<Return>',self.enter_func)

       main_frame=Frame(self.root,bd=4,bg='powder blue',width=600)
       main_frame.pack()

       img_chat=Image.open(r"New folder\chatbot.png")
       img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
       self.photoimg=ImageTk.PhotoImage(img_chat)

       Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=620,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='green',bg='white')
       Title_label.pack(side=TOP)

       self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
       self.text=Text(main_frame,width=55,height=17,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y)
       self.scroll_y.pack(side=RIGHT,fill=Y)
       self.text.pack()

       btn_frame=Frame(self.root,bd=4,bg='white',width=600)
       btn_frame.pack()

       label=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
       label.grid(row=0,column=0,padx=3,sticky=W)
       
       self.entry=StringVar()
       self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=35,font=('arial',13,'bold'))
       self.entry1.grid(row=0,column=1,padx=5,sticky=W)

       self.send=Button(btn_frame,text='Send>>',command=self.send,font=('arial',12,'bold'),width=8,bg='green',)
       self.send.grid(row=0,column=2,padx=5,sticky=W)

       self.clear=Button(btn_frame,text='Clear Data',command=self.clear,font=('arial',10,'bold'),width=8,bg='red',fg='white')
       self.clear.grid(row=1,column=0,padx=5,sticky=W)


       self.msg=''
       self.label1=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
       self.label1.grid(row=0,column=0,padx=3,sticky=W)


       # ====== function declaration=======

    def enter_func(self,event):
        self.send.invoke()
      #  self.entry.set('') 


    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')   

    def send(self):
        send='\t\t\t'+'You: '+self.entry.get() 
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg='Please enter some input'  
            self.label1.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.label1.config(text=self.msg,fg='red')

        if(self.entry.get()=='hello'):
            self.text.insert(END,"\n\n"+"BOT: Hi")

        elif(self.entry.get()=="hi"):
            self.text.insert(END,"\n\n"+"BOT: Hello")

        elif(self.entry.get()=="how are you?"):
            self.text.insert(END,"\n\n"+"BOT: fine and you")

        elif(self.entry.get()=="fantastic"):
            self.text.insert(END,"\n\n"+"BOT: Nice to hear")   


        elif(self.entry.get()=="who created you"):
            self.text.insert(END,"\n\n"+"BOT: Ankita did using python")   

        elif(self.entry.get()=="what is your name"):
            self.text.insert(END,"\n\n"+"BOT: My name is Ankita dubey")   

        elif(self.entry.get()=="can you speak marathi"):
            self.text.insert(END,"\n\n"+"BOT: I am still learning it...")   


        elif(self.entry.get()=="what is machine learning"):
            self.text.insert(END,"\n\n"+"BOT: Machine learning (ML) is a type of artificial intelligence (AI)\n that allows software applications to become more accurate\n at predicting outcomes without being explicitly programmed to do\n so. Machine learning algorithms use historical data as input to predict\n new output values.")   
        
        elif(self.entry.get()=="how does face recognition work"):
            self.text.insert(END,"\n\n"+"BOT: A facial recognition system uses biometrics to map facial\n features from a photograph or video. It compares the information\n with a database of known faces to find a match. Facial recognition can help\n verify a person's identity, but it also raises privacy issues.") 

        elif(self.entry.get()=="can you speak marathi"):
            self.text.insert(END,"\n\n"+"BOT: I am still learning it...")  

        elif(self.entry.get()=="what is chatbot"):
            self.text.insert(END,"\n\n"+"BOT: A chatbot is a software or computer program that simulates\n human conversation or chatter through text or voice interactions.")   

        elif(self.entry.get()=="what is python programming"):
            self.text.insert(END,"\n\n"+"BOT: Python is a powerful general-purpose programming language.\n It is used in web development, data science, creating software\n prototypes, and so on. Fortunately for beginners, Python has simple easy-to-use\n syntax. This makes Python an excellent language to learn to program for beginners.")   

        elif(self.entry.get()=="how many countries use facial recognition"):
            self.text.insert(END,"\n\n"+"BOT: There are 109 countries today that are either using or have\n approved the use of facial recognition technology for\n surveillance purposes.")   

        elif(self.entry.get()=="bye"):
            self.text.insert(END,"\n\n"+"BOT: ThankYou for chatting")     
                                               

        else:
            self.text.insert(END,"\n\n"+"BOT: Sorry I didn't get it...")


                   







if __name__ == '__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()



