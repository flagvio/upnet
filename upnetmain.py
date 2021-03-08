# by Ortu prof. Daniele - daniele.ortu@itisgrassi.edu.it
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from FGestione import FGest
from INDest import apriDialogo
from cpnet import CPNet

class FMain(Gtk.Window):
	def __init__(self):
		super(FMain, self).__init__(title="Aggiorna in rete")
		self.f=FGest()
		self.f.leggiCSV("pc.csv")
		#self = Gtk.Window()
		self.set_default_size(800, 500)
		self.set_position(Gtk.WindowPosition.CENTER)
		self.connect("destroy", Gtk.main_quit)
		#icona
		self.set_icon_from_file("rete.png")
		
		hbox = Gtk.Box(spacing=1)
		hbox.set_homogeneous(False)
		vbox=self.corpo_sx()
		hbox.pack_start(vbox, True, True, 20)
		vbox=self.corpo_dx()
		hbox.pack_start(vbox, True, True, 20)
		
		
		self.add(hbox)        
	def corpo_dx(self):
		hbox= Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=1)
		hbox.set_homogeneous(False)
		vbox= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
		vbox.set_homogeneous(False)
		
		label = Gtk.Label()
		label.set_markup("<b>FILE DA TRASFERIRE</b>")
		label.set_justify(Gtk.Justification.LEFT)
		vbox.pack_start(label, False, True, 0)
		
		self.enFSource = Gtk.Entry()
		#entry.set_text("                  ")
		self.enFSource.set_editable(False)		
		hbox.pack_start(self.enFSource, False, True, 0)
		bt = Gtk.Button.new_with_label("....")
		bt.connect("clicked", self.btClickScegli)
		hbox.pack_start(bt, False, True, 0)
		vbox.pack_start(hbox, False, True, 0)

		bt = Gtk.Button.new_with_label("avvia")
		bt.connect("clicked", self.btClickAvvia)
		vbox.pack_start(bt, False, False, 10)
		
		return vbox
		
	def corpo_sx(self):
		vbox= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
		vbox.set_homogeneous(False)
		
		label = Gtk.Label()
		label.set_markup("<b>COMPUTER DA AGGIORNARE</b>")
		label.set_justify(Gtk.Justification.LEFT)
		vbox.pack_start(label, False, True, 0)
		
		
		lstPC=self.listaPC()
		vbox.pack_start(lstPC, True, True, 0)
		
		btAggiungi = Gtk.Button.new_with_label("AGGIUNGI")
		btAggiungi.connect("clicked", self.btClickAggiungi)
		vbox.pack_start(btAggiungi, False, False, 10)

		return vbox
	def listaPC(self):
		listbox = Gtk.ListBox()
			
		#print(self.f.dati)
		i=0
		for riga in self.f.dati:
			hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
			row = Gtk.ListBoxRow()
			label1 = Gtk.Label(label=riga[0], xalign=0)
			label2 = Gtk.Label(label=riga[1], xalign=0)
			label3 = Gtk.Label(label=riga[2], xalign=0)
			ck=Gtk.CheckButton()
			ck.set_active(False)
			self.f.dati[i].append(0)
			ck.connect("toggled", self.on_button_toggled, i)
			hbox.pack_start(label1, True, True, 0)
			hbox.pack_start(label2, True, True, 0)
			hbox.pack_start(label3, True, True, 0)
			hbox.pack_start(ck, False, True, 0)
			row.add(hbox)
			listbox.add(row)
			i+=1
			
		return listbox
	def on_button_toggled(self,ck,nr):
		if ck.get_active():
			self.f.dati[nr][3]=1
		else:
			self.f.dati[nr][3]=0
		print(ck)
		print(self.f.dati[nr])
	def btClickScegli(self,button):
		#print("Hai cliccato ...")
		dialog = Gtk.FileChooserDialog(
			title="Please choose a file", parent=self, action=Gtk.FileChooserAction.OPEN
		)
		dialog.add_buttons(
			Gtk.STOCK_CANCEL,
			Gtk.ResponseType.CANCEL,
			Gtk.STOCK_OPEN,
			Gtk.ResponseType.OK,
		)

		self.add_filters(dialog)

		response = dialog.run()
		if response == Gtk.ResponseType.OK:
			#print("Open clicked")
			#print("File selected: " + dialog.get_filename())
			self.enFSource.set_text(dialog.get_filename())
		#elif response == Gtk.ResponseType.CANCEL:
		#	print("Cancel clicked")
		
		dialog.destroy()
	
	def add_filters(self, dialog):
		  filter_text = Gtk.FileFilter()
		  filter_text.set_name("Text files")
		  filter_text.add_mime_type("text/plain")
		  dialog.add_filter(filter_text)
		  filter_py = Gtk.FileFilter()
		  filter_py.set_name("Python files")
		  filter_py.add_mime_type("text/x-python")
		  dialog.add_filter(filter_py)
		  filter_any = Gtk.FileFilter()
		  filter_any.set_name("Any files")
		  filter_any.add_pattern("*")
		  dialog.add_filter(filter_any)

	def btClickAggiungi(self,button):		
		dialog = apriDialogo()
	def controlla(self):
		if self.enFSource.get_text()=="":
			msg= Gtk.MessageDialog(
				transient_for=self,
				flags=0,
				message_type=Gtk.MessageType.INFO,
				buttons=Gtk.ButtonsType.OK,
				text="Inserisci il file da copiare",
			)
			msg.run()
			msg.destroy()

			return False		
	def btClickAvvia(self,button):
		print("Hai cliccato AVVIA")
		if self.controlla()==False:
			return
		cccp=CPNet(self.f.dati,self.enFSource.get_text())
		cccp.connect("destroy", Gtk.main_quit)
		cccp.show_all()
		Gtk.main()

	def main(self):
		self.show_all()
		Gtk.main()
#if __name__ == "__main__":
upnet = FMain()
upnet.main()
