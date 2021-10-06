import tkinter as tk
from tkinter import *
from tkinter import ttk
import math as m

class DecimalToBinary:

	def __init__(self, root):
		#initial application
		root.title("Decimal to Binary conversion")

		#setting up main frame
		mainframe = ttk.Frame(root, padding="3 3 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		root.columnconfigure(0, weight=1)
		root.rowconfigure(0, weight=1)

		#creating the decimal entry widget
		self.decimal = StringVar()
		decimal_entry = ttk.Entry(mainframe, width=7, textvariable=self.decimal)
		decimal_entry.grid(column=2, row=1, sticky=(W, E))

		#creating the binary output widget
		self.binary = StringVar()
		ttk.Label(mainframe, textvariable=self.binary).grid(column=2, row=2, sticky=(W, E))
		ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

		ttk.Label(mainframe, text="in decimal").grid(column=3, row=1, sticky=W)
		ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
		ttk.Label(mainframe, text="in binary").grid(column=3, row=2, sticky=W)

		#polish
		for child in mainframe.winfo_children(): 
		    child.grid_configure(padx=5, pady=5)
		decimal_entry.focus()
		root.bind("<Return>", self.calculate)

		
	def calculate(self, *args):
		input = int(self.decimal.get())
		try:
			if (input >= 0):
			  x = 0
			  output = ''
			  if input > 0:
				  while (m.pow(2,x) < input):
					  x = x + 1
				  for i in reversed(range(x + 1)):
					  if (input >= m.pow(2, i)):
						  input -= m.pow(2, i)
						  output = output + '1'
					  else:
						  output = output + '0'
			#gets rid of leading zero
			if output[0:1] == '0':
				output = output[1:]
				
			self.binary.set(output)
		except ValueError:
			pass

root = Tk()
DecimalToBinary(root)
root.mainloop()

