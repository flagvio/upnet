import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class FMain(Gtk.Window):
	def __init__(self):
		super(FMain, self).__init__()
		#self = Gtk.Window()
		self.set_default_size(800, 500)
		self.set_position(Gtk.WindowPosition.CENTER)
		self.connect("destroy", Gtk.main_quit)
		#icona
		self.set_icon_from_file("rete.png")
		
		label = Gtk.Label()
		label.set_text("This is a left-justified label.\nWith multiple lines.")
        #label.set_justify(Gtk.Justification.LEFT)
        #self.add(label)
	
	#def corpo(self):
		
		
	def main(self):
		self.show()
		Gtk.main()
#if __name__ == "__main__":
upnet = FMain()
upnet.main()
