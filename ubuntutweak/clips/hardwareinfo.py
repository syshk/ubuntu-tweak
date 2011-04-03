import os
from gi.repository import Gtk, GLib

from ubuntutweak import system
from ubuntutweak.clips import Clip
from ubuntutweak.utils import icon
from ubuntutweak.gui.containers import EasyTable

class HardwareInfo(Clip):
    def __init__(self):
        Clip.__init__(self)

        self.set_image_from_pixbuf(icon.get_from_name('computer', size=48))
        self.set_title(_('Hardware Information'))

        cpumodel = _('Unknown')

        if os.uname()[4][0:3] == "ppc":
            for element in file("/proc/cpuinfo"):
                if element.split(":")[0][0:3] == "cpu":
                    cpumodel = element.split(":")[1].strip()
        else:
            for element in file("/proc/cpuinfo"):
                if element.split(":")[0] == "model name\t":
                    cpumodel = element.split(":")[1].strip()

        for element in file("/proc/meminfo"):
            if element.split(" ")[0] == "MemTotal:":
                raminfo = element.split(" ")[-2]

        self.table = EasyTable(items=(
                        (Gtk.Label(label=_('CPU:')),
                         Gtk.Label(label=cpumodel)),
                        (Gtk.Label(label=_('Memory:')),
                         Gtk.Label(label=GLib.format_size_for_display(int(raminfo) * 1024))),
                        ),
                        xpadding=12, ypadding=2)
        self.set_content(self.table)