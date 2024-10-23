import tkinter as tk
app = tk.Tk()
app.title("Calculadora")
app.geometry("200x410")
app.config(bg="cyan")

visor = tk.Entry(app,font=("Arial",12))
visor.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def calcular():
    conta = visor.get()
    try:
        resultado = eval(conta)
        visor.delete(0,tk.END)
        visor.insert(0,resultado)
    except Exception as e:
        visor.delete(0,tk.END)
        visor.insert(0,"Error")

button_params = {"width":2,"height":2}

C = tk.Button(app, text="C", command=lambda: visor.delete(0,tk.END),**button_params) 
plus = tk.Button(app, text="+", command=lambda: visor.insert(tk.END,"+"),**button_params )
menos = tk.Button(app, text="-", command=lambda: visor.insert(tk.END,"-"),**button_params )
um = tk.Button(app, text="1", command=lambda: visor.insert(tk.END,"1"),**button_params )
dois = tk.Button(app, text="2", command=lambda: visor.insert(tk.END,"2"),**button_params )
tres = tk.Button(app, text="3", command=lambda: visor.insert(tk.END,"3"),**button_params )
quatro = tk.Button(app, text="4", command=lambda: visor.insert(tk.END,"4"),**button_params )
cinco = tk.Button(app, text="5", command=lambda: visor.insert(tk.END,"5"),**button_params )
seis = tk.Button(app, text="6", command=lambda: visor.insert(tk.END,"6"),**button_params )
sete = tk.Button(app, text="7", command=lambda: visor.insert(tk.END,"7"),**button_params )
oito = tk.Button(app, text="8", command=lambda: visor.insert(tk.END,"8"),**button_params )
nove = tk.Button(app, text="9", command=lambda: visor.insert(tk.END,"9"),**button_params )
zero = tk.Button(app, text="0", command=lambda: visor.insert(tk.END,"0"),**button_params )
multi = tk.Button(app, text="*", command=lambda: visor.insert(tk.END,"*"),**button_params )
div = tk.Button(app, text="/", command=lambda: visor.insert(tk.END,"/"),**button_params )
igual = tk.Button(app, text="=",command=calcular,**button_params)
ponto = tk.Button(app, text=".", command=lambda: visor.insert(tk.END,"."),**button_params )
nd = tk.Button(app,text="",**button_params)

C.grid(row=1, column=0, padx=10, pady=10)
plus.grid(row=1, column=1, padx=10, pady=10)
menos.grid(row=1, column=2, padx=10, pady=10)

um.grid(row=2, column=0, padx=10, pady=10)
dois.grid(row=2, column=1, padx=10, pady=10)
tres.grid(row=2, column=2, padx=10, pady=10)

quatro.grid(row=3, column=0, padx=10, pady=10)
cinco.grid(row=3, column=1, padx=10, pady=10)
seis.grid(row=3, column=2, padx=10, pady=10)

sete.grid(row=4, column=0, padx=10, pady=10)
oito.grid(row=4, column=1, padx=10, pady=10)
nove.grid(row=4, column=2, padx=10, pady=10)

multi.grid(row=5, column=0, padx=10, pady=10)
zero.grid(row=5, column=1, padx=10, pady=10)
div.grid(row=5, column=2, padx=10, pady=10)

nd.grid(row=6, column=0, padx=10, pady=10)
ponto.grid(row=6, column=1, padx=10, pady=10)
igual.grid(row=6, column=2, padx=10, pady=10)

app.mainloop()