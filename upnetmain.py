import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class FMain(Gtk.Window):
	def __init__(self):
		super(FMain, self).__init__(title="Aggiorna in rete")
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
		vbox= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
		vbox.set_homogeneous(False)
		
		label = Gtk.Label()
		label.set_markup("<b>FILE DA TRASFERIRE</b>")
		label.set_justify(Gtk.Justification.LEFT)
		vbox.pack_start(label, False, True, 0)
		
		entry = Gtk.Entry()
		entry.set_text("                  ")
		entry.set_editable(False)
		vbox.pack_start(entry, False, True, 0)

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
		
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		label1 = Gtk.Label(label="Automatic Date & Time", xalign=0)
		label2 = Gtk.Label(label="Requires internet access", xalign=0)
		hbox.pack_start(label1, True, True, 0)
		hbox.pack_start(label2, True, True, 0)
		row.add(hbox)
		listbox.add(row)

		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		label1 = Gtk.Label(label="bau", xalign=0)
		label2 = Gtk.Label(label="miao", xalign=0)
		hbox.pack_start(label1, True, True, 0)
		hbox.pack_start(label2, True, True, 0)
		row.add(hbox)
		listbox.add(row)
		
		
		return listbox
	def btClickAggiungi(self,button):
		print("Hai cliccato AGGIUNGI")
	def btClickAvvia(self,button):
		print("Hai cliccato AVVIA")
	def main(self):
		self.show_all()
		Gtk.main()
#if __name__ == "__main__":
upnet = FMain()
upnet.main()
