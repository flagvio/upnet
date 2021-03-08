# by Ortu prof. Daniele - daniele.ortu@itisgrassi.edu.it
import socket
import os

NR=1400
PORTA=1300
class Server:
	def __init__(self,destinatario):
		self.HOST="localhost"
		self.d=destinatario
	
	def run(self):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((self.HOST, PORTA))
			s.listen(10)
			while True:
				print("attendo comessione")
				conn, addr = s.accept()
				with conn:
					print('Connected by', addr)
					with open(self.d,'wb') as fwb:
						i=0
						while True:
							data = conn.recv(NR)
							if not data:
								break
							conn.sendall(b'OK')
							fwb.write(data)						
							#i+=1
							#print(i)
class Client:
	def __init__(self,SERVER,sorgente):
		self.SERVER=SERVER
		self.s=sorgente
		self.perc=0.0
	def run(self):
		self.copiaNET(self.SERVER)	
	
	def copiaNET(self,IP):		
		#print("Entro in copiaNET")
		
		l=os.stat(self.s).st_size
		#print(l)
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as fwb:
			fwb.connect((IP, PORTA))
			#print("aperto destinatario")
			frb=open(self.s,'rb')
			#print("aperto sorgente")
			pos=0
			step=NR
			
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
				fwb.sendall(data)
				r=fwb.recv(NR)
				#print(r)
				if r!=b'OK':
					print("ERRORE NELLA COPIA. BYTE: "+str(pos))
					frb.close()
					return -1
				self.perc=(pos/l)

		frb.close()
		return 0

#srv=Server(1300)
#srv.run()

