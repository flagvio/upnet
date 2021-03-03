import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class DInserisciDestinatario(Gtk.Dialog):
	def __init__(self, parent):
		#self.dati=["pr1","pr2","pr3"]
		Gtk.Dialog.__init__(self, title="GIGINI", transient_for=parent, flags=0)
		self.add_buttons(
			Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
		)
		self.set_default_size(150, 100)
		
		grid=Gtk.Grid()
		#self.add(grid)
		grid.set_row_spacing(10)
		grid.set_column_spacing(5)
		
		lbNome = Gtk.Label(label="NOME PC ")
		self.enNome = Gtk.Entry()
		lbIP = Gtk.Label(label="IP ")
		self.enIP = Gtk.Entry()
		lbMAC = Gtk.Label(label="MAC ")
		self.enMAC = Gtk.Entry()
		label4 = Gtk.Label(label="lab4 ")
		
		grid.attach(lbNome,0,0,1,1)
		grid.attach(self.enNome,1,0,1,1)
		
		grid.attach(lbIP,0,1,1,1)
		grid.attach(self.enIP,1,1,1,1)
		
		grid.attach(lbMAC,0,2,1,1)
		grid.attach(self.enMAC,1,2,5,1)
		
		box = self.get_content_area()
		box.add(grid)
		self.show_all()

class DialogExample(Gtk.Dialog):
	def __init__(self, parent):
		Gtk.Dialog.__init__(self, title="My Dialog", transient_for=parent, flags=0)
		self.add_buttons(
			Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
		)
		self.set_default_size(150, 100)
		
		
		
		label = Gtk.Label(label="This is a dialog to display additional information")
	

		box = self.get_content_area()
		box.add(label)
		self.show_all()

class DialogWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Dialog Example")

        self.set_border_width(6)

        button = Gtk.Button(label="Open dialog")
        button.connect("clicked", self.on_button_clicked)

        self.add(button)

    def on_button_clicked(self, widget):
        #dialog = DialogExample(self)
        dialog = DInserisciDestinatario(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            #print(dialog.dati)
            print("Click OK")
        elif response == Gtk.ResponseType.CANCEL:
            print("The Cancel button was clicked")

        dialog.destroy()


#win = DialogWindow()
#win.connect("destroy", Gtk.main_quit)
#win.show_all()
#Gtk.main()
