import csv

class FGets():
	def __init__(self,f):
		self.dati=""
		try:
			with open("./"+f, newline="", encoding="ISO-8859-1") as filecsv:
				lettore = csv.reader(filecsv,delimiter=";")
				#print(lettore)			
				#header = next(lettore)
				#header = next(lettore)
				#print(header)	
				self.dati = [(linea[0],linea[1],linea[2]) for linea in lettore ]
				#print(self.filecompleto) 		
		except FileNotFoundError:
			print("Errore apertura file")

#upnet = FGets("pc.csv")
