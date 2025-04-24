from tkinter import Tk
from gui import show_gui

def main():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    show_gui()

if __name__ == "__main__":
    main()
