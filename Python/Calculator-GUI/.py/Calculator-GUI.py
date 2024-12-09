import tkinter as tk

def calculate():
    operacao = 0
    operacao = visor.get()
    try:
        answer = eval(operacao) 
    except:
        answer = 'ERROR'
    clear()
    visor.insert(0,answer)

def write(text):
    currentText = visor.get()
    clear()
    visor.insert(tk.END, currentText + text)

def clear():
    visor.delete(0,tk.END)
    
app = tk.Tk()
app.title('Calculator')
app.geometry('300x600')
app.config(bg = '#14757F')

labelForvisor = tk.Label(app, text = 'Calculator' )
labelForvisor.config(bg='lightgray')

visor = tk.Entry(app,font=('',15), width=25, bg='#FFF6BD')
visor.grid(row=0,column=0, columnspan=4,padx=10, pady=10 )


Buttons = [
    ['1','2','3','C'],
    ['4','5','6','+'],
    ['7','8','9','-'],
    ['*','0','/','.'],
    ['','**','%','=']
]


for i, row in enumerate(Buttons):
    for j, txt in enumerate(row):
        if(txt == 'C'):
            btn = tk.Button(bg='#FFF6BD',width=5,height=5,text= txt, command = clear)
            btn.grid(row=i+1,column=j,padx=10,pady=10)
        elif(txt == '='):
            btn = tk.Button(bg='#FFF6BD',width=5,height=5,text= txt, command = calculate)
            btn.grid(row=i+1,column=j,padx=10,pady=10)
        else:
            btn = tk.Button(bg='#FFF6BD',width=5,height=5,text= txt, command  = lambda txt=txt: write(txt) )
            btn.grid(row=i+1,column=j,padx=10,pady=10)

app.mainloop()
