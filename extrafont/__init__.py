try:
    import Tkinter as tkinter
except ImportError:
    import tkinter

ExtrafontVersion = None


def enable(interpreter):
    """Imports extrafont module to the provided Tk/Tcl interpreter"""
    global ExtrafontVersion
    try:
        import os.path
        import platform

        supported = ["Darwin", "Linux", "Windows"]
        if platform.system() in supported: pass
        else: raise RuntimeError('Platform not supported.')
        
        module_path = os.path.join(os.path.dirname(__file__), 'extrafont')
        interpreter.tk.call('lappend', 'auto_path', module_path)
        ExtrafontVersion = interpreter.tk.call('package', 'require', 'extrafont')
    except tkinter.TclError:
        raise RuntimeError('Unable to load extrafont library.')
    return ExtrafontVersion

def availableFamilies(interpreter, fontFamilyPattern):
    """Returns the list of font-families matching the glob-style fontFamilyPattern"""
    interpreter.tk.call('extrafont::availableFamilies', fontFamilyPattern)

def cleanup(interpreter):
    """Unloads all the loaded extrafonts."""
    interpreter.tk.call('extrafont::cleanup')

def isAvaliable(interpreter, fontFamily):
    """Returns true if fontFamily is avaiable"""
    interpreter.tk.call('extrafont::isAvailable', fontFamily)

def load(interpreter, filename):
    """Loads all the fonts contained in filename"""
    interpreter.tk.call('extrafont::load', filename)

def loaded(interpreter):
    """Returns a list containing the names of all currently loaded extrafont font-files"""
    interpreter.tk.call('extrafont::loaded')

def nameinfo(interpreter, fontfile):
    """Returns a list of font-details"""
    interpreter.tk.call('extrafont::nameinfo', fontfile)

def nametable(interpreter):
    """Returns all the valid keys used for the font-details dictionary"""
    interpreter.tk.call('extrafont::nametable::nameIDs')

def query(interpreter, kind, selector_pattern=None):
    """Returns lists of different kinds (files, families, fullnames, details) about the loaded fonts, matching the optional selector_pattern"""
    if not selector_pattern: interpreter.tk.call('extrafont::query', kind)
    else: interpreter.tk.call('extrafont::query', kind, selector_pattern)

def unload(interpreter, filename):
    """Unloads all the fonts previously loaded with filename"""
    interpreter.tk.call('extrafont::unload', filename)
