from tkinter import *


#Put it in English


class Interfaz():
	def __init__(self, ventana):
		self.ventana= ventana

		self.ventana.title("TEST CALCULATOR BY ELDANYGA GITHUB V1.0")
		#Test this resolution
		self.ventana.geometry("600x250")
		self.ventana.resizable(width=0, height=0)

		

		self.pantalla=Text(ventana,state="disabled",width=40,height=3,background="orchid",foreground="white",font=("Helvetica",15))
		self.pantalla.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

		"Operacion a llevar"
		self.operacion=""

		return


	def click(self, valor, escribir):
		try:
			if not escribir:
				if valor=="=" and self.operacion!="":
					resultado = str(eval(self.operacion))
					#self.operacion=""
					self.limpiarPantalla()
					self.mostrarEnPantalla(resultado)

				#self.operacion+=str(valor)
			else:

				self.operacion+=str(valor)
				self.mostrarEnPantalla(valor)
		except SyntaxError:
			self.limpiarPantalla()
			self.mostrarEnPantalla("Está colocando mal un número")

		return

		
	def crearBoton(self, valor, escribir=True, ancho=19, largo=1):                     #lambda permite pasarle parametros al metodo click
		if valor=="<--":
			return Button(self.ventana, text=str(valor), width=ancho, height=largo, command=self.limpiarPantalla)
		else:
			return Button(self.ventana, text=str(valor), width=ancho, height=largo, command=lambda: self.click(valor, escribir))


	def limpiarPantalla(self):
		self.pantalla.configure(state="normal")
		self.pantalla.delete("1.0", END)
		self.pantalla.configure(state="disabled")
		self.operacion=""
		return

	def mostrarEnPantalla(self, valor):
		self.pantalla.configure(state="normal")
		self.pantalla.insert(END, valor)
		self.pantalla.configure(state="disabled")
		return



root = Tk()
ventana= Interfaz(root)


#Creando Botones

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


cont=0
botones= [b1, b4, b7, b2, b5, b8, b3, b6, b9]
for bot in range(3):
	for row in range(1,4):
		botones[cont].grid(column=bot, row=row)
		cont+=1

b0.grid(column=1, row=4)

b10 = ventana.crearBoton("=", escribir=False)
b10.grid(column=6, row=6)

b11 = ventana.crearBoton("+")
b11.grid(column=6, row=5)

b12 = ventana.crearBoton("-")
b12.grid(column=6, row=4)

b13 = ventana.crearBoton("*")
b13.grid(column=6, row=3)

b14= ventana.crearBoton("**")
b14.grid(column=6, row=2)

#Crear el ultimo boton que necesita una funcion dentro de la clase
b15 = ventana.crearBoton("<--")
b15.grid(column=6, row=0)

b16 = ventana.crearBoton("/")
b16.grid(column=6, row=1)





#Icono
root.tk.call("wm", "iconphoto", root._w, PhotoImage(file="1916066.png"))

#root.iconbitmap("/index.ico")
root.mainloop()
