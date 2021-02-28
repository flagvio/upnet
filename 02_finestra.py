import pygtk
pygtk.require('2.0')
import gtk
class FirstWin:
	def __init__(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.button = gtk.Button("Hello, World!")
		self.win.add(self.button) 
		self.win.show()
	
	def main(self):
		gtk.main()

if __name__ == "__main__":
	first = FirstWin()
	first.main()
