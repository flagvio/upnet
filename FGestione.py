# by Ortu prof. Daniele - daniele.ortu@itisgrassi.edu.it
import csv
import os

import socket

M=1048576
G=1073741824
ST=1400
class FGest():
	def __init__(self):
		print("FGestione creato")
		self.perc=0.0
	
	def copia2(self):
			while False:
				if pos>=l:
					break
				
				frb.seek(pos,0)
				#fwb.seek(pos,0)
				if (pos+step)>l:
					step=l-pos
					pos=l
					#print('IF '+str(step))
				else:
					pos+=step
					#print('ELSE '+str(pos))
				data=frb.read(step)
				#print(data)			
				fwb.write(data)
				self.perc=(pos/l)
				print(self.perc)
		
	def copia(self,s,d):		
		print("Entro in copia")
		
		l=os.stat(s).st_size
		print(l)
		with open(d,'wb') as fwb:
			print("aperto destinatario")
			frb=open(s,'rb')
			print("aperto sorgente")
			pos=0
			step=ST
			while True:
				if pos>=l:
					break
				
				frb.seek(pos,0)
				#fwb.seek(pos,0)
				if (pos+step)>l:
					step=l-pos
					pos=l
					#print('IF '+str(step))
				else:
					pos+=step
					#print('ELSE '+str(pos))
				data=frb.read(step)
				#print(data)			
				fwb.write(data)
				self.perc=(pos/l)
				#print(self.perc)
		frb.close()
		
		
		
	def leggiCSV(self,f):
		self.dati=""
		try:
			with open("./"+f, newline="", encoding="ISO-8859-1") as filecsv:
				lettore = csv.reader(filecsv,delimiter=";")
				#print(lettore)			
				#header = next(lettore)
				#header = next(lettore)
				#print(header)	
				self.dati = [[linea[0],linea[1],linea[2]] for linea in lettore ]
				#print(self.filecompleto) 		
				return ""
		except FileNotFoundError:
			return "Errore apertura file"
		
#g = FGest().copia('testFile.py','tmp.png')
