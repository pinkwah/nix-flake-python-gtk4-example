import sys

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import GLib, Gtk, Adw

class MyApplication(Adw.Application):
    def __init__(self) -> None:
        super().__init__(application_id="com.example.MyGtkApplication")
        GLib.set_application_name("My Gtk Application")

    def do_activate(self) -> None:
        window = Adw.ApplicationWindow(application=self, title="Hello World")
        window.present()


app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
