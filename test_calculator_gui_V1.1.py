from tkinter import Tk, Button, Text, PhotoImage, END, Frame

class Interfaz():
	def __init__(self, ventana, frame):
		self.ventana= ventana
		self.frame=frame
		self.ventana.title("TEST CALCULATOR V-FINAL 1.1")
		#Test this resolution
		self.ventana.geometry("413x233")
		self.ventana.resizable(False, False)
		#orchid value for background
		self.pantalla=Text(ventana,state="disabled",width=29,height=2,background="blue",foreground="white",font=("Helvetica",14))
		self.pantalla.grid(row=0, column=0, columnspan=4, padx=0, pady=10)
		"Operacion a llevar"
		self.operacion=""
		
		self.cont=1
		return

	def mostraryeliminar(self, valor):
		self.pantalla.configure(state="normal")
		self.pantalla.delete("1.0", END)
		self.pantalla.insert(END, valor)
		self.pantalla.configure(state="disabled")
		return

	def borrar(self):
		self.operacion=self.operacion[:len(self.operacion)-1]
		self.mostraryeliminar(self.operacion)
		return 

	def click(self, valor, escribir):
		try:
			if not escribir:
				if valor=="=" and self.operacion!="":
					#MAKING MATHS OPERATIONS
					resultado = str(eval(self.operacion))
					self.limpiarPantalla()
					self.operacion=str(resultado)
					self.mostrarEnPantalla(resultado)
			else:
				self.operacion+=str(valor)
				self.mostrarEnPantalla(valor)

		except SyntaxError:
			self.limpiarPantalla()
			self.mostrarEnPantalla("Something is Wrong in your Input !!!")

		return

	def crearBoton(self, valor, escribir=True, ancho=10, largo=2, fondo=None):                  
		
		if valor=="<--":
			return Button(self.ventana, text=str(valor), width=ancho, height=largo, command=self.limpiarPantalla )
		elif valor=="del":
			return Button(self.ventana, text=str(valor), width=ancho, height=largo, command=self.borrar)
		elif valor==")" or valor=="(":
			return Button(self.frame, text=str(valor), width=4, height=2, command=lambda: self.click(valor, escribir))
		else:
			return Button(self.ventana, text=str(valor), background=fondo, width=ancho, height=largo, command=lambda: self.click(valor, escribir))

	def limpiarPantalla(self):
		self.pantalla.configure(state="normal")
		self.pantalla.delete("1.0", END)
		self.pantalla.configure(state="disabled")
		self.operacion=""
		self.cont=1
		return

	def mostrarEnPantalla(self, valor):
		self.pantalla.configure(state="normal")
		self.pantalla.insert(END, valor)
		self.pantalla.configure(state="disabled")
		return

root = Tk()

#CREATE A NEW FRAME CONTAINER FOR "(" AND ")"
frame = Frame(root, width=10, height=2)
frame.grid(column=4, row=3)

ventana= Interfaz(root, frame)

#Creating Buttons
b1 = ventana.crearBoton(1)
b2 = ventana.crearBoton(2)
b3 = ventana.crearBoton(3)
b4 = ventana.crearBoton(4)
b5 = ventana.crearBoton(5)
b6 = ventana.crearBoton(6)
b7 = ventana.crearBoton(7)
b8 = ventana.crearBoton(8)
b9 = ventana.crearBoton(9)
b0 = ventana.crearBoton(0)
b10 = ventana.crearBoton("=", escribir=False)
b11 = ventana.crearBoton("+")
b12 = ventana.crearBoton("-")
b13 = ventana.crearBoton("*")
b14= ventana.crearBoton("**")
b15 = ventana.crearBoton("<--")
b18= ventana.crearBoton("%")
bpun = ventana.crearBoton(".")
b17 = ventana.crearBoton("del")
b16 = ventana.crearBoton("/")

b19 = ventana.crearBoton("(")
b20 = ventana.crearBoton(")")

cont=0
botones= [b1, b4, b7, b18, b2, b5, b8,b0, b3, b6, b9,bpun, b10, b11,b12, b13, b14, b15]
for bot in range(4):
	for row in range(1,5):
		botones[cont].grid(column=bot, row=row)
		cont+=1

b15.grid(column=4, row=0, padx= 10)
b17.grid(column=4, row=1, padx= 5)
b14.grid(column=4, row=4)
b16.grid(column=4, row=2)

#FRAME BUTTONS "(" AND ")"
b19.pack(side="left", fill="y", ipadx=1)
b20.pack(side="right", ipadx=1)

#Icon
#root.tk.call("wm", "iconphoto", root._w, PhotoImage(file="1916066.png"))
#root.iconbitmap("/index.ico")
root.mainloop()
