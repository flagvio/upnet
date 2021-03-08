## finestra di dialogo per visualizzare copia file
# by Ortu prof. Daniele - daniele.ortu@itisgrassi.edu.it
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk,GLib

from FGestione import FGest
from ClientServer import Client

import threading
import time
class CPNet(Gtk.Window):
	def __init__(self,listaPC,fileSorgente,fileDestinatario=None):
		Gtk.Window.__init__(self, title="Copie in corso",)

		self.set_border_width(6)
		self.set_default_size(800, 500)
		
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(vbox)
		
		label = Gtk.Label()
		label.set_markup("<b>FILE DA TRASFERIRE</b>")
		label.set_justify(Gtk.Justification.LEFT)
		vbox.pack_start(label, False, True, 0)
		
		print("FILE S: "+fileSorgente)
		
		for lspc in listaPC:
			if lspc[3]==1:
				cpn=CPNet_one(lspc,fileSorgente);
				#print(cpn.hbox)
				vbox.pack_start(cpn.hbox, False, True, 0)
		
		#cpn=CPNet_one("localhost",fileSorgente);
		#print(cpn.hbox)
		#vbox.pack_start(cpn.hbox, False, True, 0)
		
		

class CPNet_one():
	def __init__(self,pc,fileSorgente,fileDestinatario=None):
		
		self.NOME=0
		self.IP=1
		self.MAC=2
		self.STATO=3
		self.lspc=pc
		
		self.fs=fileSorgente
		
		self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		self.lbNome=Gtk.Label(label=pc[self.NOME])
		self.progressbar=Gtk.ProgressBar()
		
		self.button = Gtk.Button(label="stop")
		self.button.connect("clicked", self.on_button_clicked)
		#print("---"+self.fs)
		if fileDestinatario is None:	
			self.fs=fileSorgente
			self.client=Client(self.lspc[self.IP],fileSorgente)
			
			
			self.hbox.pack_start(self.lbNome, False, True, 0)
			self.hbox.pack_start(self.progressbar, True, True, 0)
			self.hbox.pack_start(self.button, False, True, 0)
			#print("CREATO HBOX")
			x = threading.Thread(target=self.thCopiaNET, args=(self.lspc[self.IP],fileSorgente))
			x.start()
			
		self.timeoutNET_id = GLib.timeout_add(50, self.on_timeoutNET,None)
		self.activity_mode = False	


		
	
	def OLD__init__OLD(self,listaPC,fileSorgente,fileDestinatario,tipo):
		Gtk.Window.__init__(self, title="Copie in corso",)

		self.set_border_width(6)
		self.set_default_size(800, 500)
		
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(vbox)
		
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		vbox.add(hbox)
		
		self.progressbar = Gtk.ProgressBar()
		hbox.pack_start(self.progressbar, True, True, 0)
		
		button = Gtk.Button(label="stop")
		button.connect("clicked", self.on_button_clicked)
		hbox.pack_start(button, True, True, 0)
		
		
		
		if tipo=="NET":
			self.timeoutNET_id = GLib.timeout_add(50, self.on_timeoutNET, None)
		else:
			self.timeout_id = GLib.timeout_add(50, self.on_timeout, None)
		self.activity_mode = False

		
		self.fs=fileSorgente
		x = threading.Thread(target=self.thCopiaNET, args=("localhost"))
		x.start()

		
	def thCopiaNET(self,IP,fileSorgente):
		
		
		#print("F: "+fileSorgente+" "+fileDestinatario)
		print("TREAHD-SART"+IP)
		
		self.client.run()
		#time.sleep(2)
		print("TREAHD-STOP")
	
	
	def thCopia(self,fileSorgente,fileDestinatario):
		self.f=FGest()
		#print("F: "+fileSorgente+" "+fileDestinatario)
		print("TREAHD-SART")
		self.f.copia(fileSorgente,fileDestinatario)
		#time.sleep(2)
		print("TREAHD-STOP")

	def on_timeoutNET(self, user_data):
		"""
		Update value on the progress bar
		"""
		if self.activity_mode:
			self.progressbar.pulse()
		else:
			
			new_value=self.client.perc
			
			self.progressbar.set_fraction(new_value)

		# As this is a timeout function, return True so that it
		# continues to get called
		return True
		
	def on_timeout(self, user_data):
		"""
		Update value on the progress bar
		"""
		if self.activity_mode:
			self.progressbar.pulse()
		else:
			#new_value = self.progressbar.get_fraction() + 0.01
			
			new_value=self.f.perc
			
			#if new_value > 1:
			#	new_value = 0

			self.progressbar.set_fraction(new_value)

		# As this is a timeout function, return True so that it
		# continues to get called
		return True
       
	def on_button_clicked(self, widget):
		dialog = DialogExample(self)
		response = dialog.run()

		if response == Gtk.ResponseType.OK:
			print("The OK button was clicked")
		elif response == Gtk.ResponseType.CANCEL:
			print("The Cancel button was clicked")

		dialog.destroy()

#win = CPNet([['PC1','192.168.1.240','FFFFFF',1],['PC2','localhost','FFFFFF',1]],'/home/neo/Immagini/tcp.png')
#win = CPNet_one("192.168.1.240",'/media/neo/77CC8C747666395A/virtualBox/zeroshell2.vdi')
#win = CPNet([('PC1','192.168.1.240','FFFFFF'),('PC2','localhost','FFFFFF')],'/media/neo/77CC8C747666395A/virtualBox/zeroshell2.vdi')
#win.connect("destroy", Gtk.main_quit)
#win.show_all()
#Gtk.main()
