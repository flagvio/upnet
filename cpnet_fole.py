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
		
		#hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		#vbox.add(hbox)
		
		self.client=[]
		self.progressbar=[]
		
		if fileDestinatario is None:	
			self.fs=fileSorgente
			
			i=0
			for rec in listaPC:
				hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
				self.progressbar.append ( Gtk.ProgressBar())
				hbox.pack_start(self.progressbar[i], True, True, 0)
				button = Gtk.Button(label="stop")
				button.connect("clicked", self.on_button_clicked)
				hbox.pack_start(button, False, True, 0)
					
				
				x = threading.Thread(target=self.thCopiaNET, args=(i,rec[2],fileSorgente))
				x.start()
				
				vbox.pack_start(hbox,False,True,0)
				self.timeoutNET_id = GLib.timeout_add(50, self.on_timeoutNET, i)
				self.activity_mode = False	
				i+=1	

		
	
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

		
	def thCopiaNET(self,nrClient,IP,fileSorgente):
		
		client.Client(IP,fileSorgente)
		#print("F: "+fileSorgente+" "+fileDestinatario)
		print("TREAHD-SART"+str(nrTH))
		
		#client.run()
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
			
			new_value=self.client[user_data].perc
			
			self.progressbar[user_data].set_fraction(new_value)

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

#win = CPNet([('PC1','192.168.1.1','FFFFFF')],'/media/neo/77CC8C747666395A/virtualBox/debian-9.2.1-amd64-netinst.iso','/home/neo/Scrivania/tmp/cancellao')
win = CPNet([('PC1','192.168.1.240','FFFFFF'),('PC2','localhost','FFFFFF')],
			'/media/neo/77CC8C747666395A/virtualBox/zeroshell2.vdi')
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
