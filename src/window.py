#contains the definition class for the gui window
#and its associated functions
import tkinter as tk
from tkinter import messagebox
import color

class window:
    def __init__(self, col):
        self.root = tk.Tk()
        self.root.title("HSV")
        self.root.resizable(False, False)
        self.label_h = tk.Label(self.root, text="Enter Hue:")
        self.label_h.grid(column=0, row=0, padx=10, pady=10)
        self.entry_h = tk.Entry(self.root)
        self.entry_h.grid(column=1, row=0, padx=10, pady=10)
        self.label_s = tk.Label(self.root, text="Enter Saturation:")
        self.label_s.grid(column=0, row=1, padx=10, pady=10)
        self.entry_s = tk.Entry(self.root)
        self.entry_s.grid(column=1, row=1, padx=10, pady=10)
        self.label_v = tk.Label(self.root, text="Enter Value:")
        self.label_v.grid(column=0, row=2, padx=10, pady=10)
        self.entry_v = tk.Entry(self.root)
        self.entry_v.grid(column=1, row=2, padx=10, pady=10)
        self.but = tk.Button(self.root, text="Apply Color", command=self.button_press).grid(column=0, row=3, padx=10, pady=10, columnspan=2)
        self.color_bg = col
        self.color_fg = col.find_complement()
        self.update_color()
        self.root.mainloop()

    def button_press(self):
        hue = float(self.entry_h.get())
        if hue > 360 or hue < 0:
            messagebox.showerror("Out of bounds", "Hue can only assume a value in the range [0, 360]")
            return 0
        sat = float(self.entry_s.get())
        if sat < 0 or sat > 1:
            messagebox.showerror("Out of bounds", "Saturation can only assume values in the range [0, 1]")
            return 0
        val = float(self.entry_v.get())
        if val < 0 or val > 1:
            messagebox.showerror("Out of bounds", "Value can only assume values in the range [0, 1]")
            return 0
        self.color_bg = color.hsv(hue, sat, val)
        self.color_fg = self.color_bg.find_complement()
        self.update_color()
    #update the window whenever color is updated
    #TODO
    def update_color(self):
        bg = self.color_bg.to_rgb()
        fg = self.color_fg.to_rgb()
        labels = [self.label_h, self.label_s, self.label_v]
        entries = [self.entry_h, self.entry_s, self.entry_v]
        self.root["bg"] = bg
        for i in labels:
            i["fg"] = fg
            i["bg"] = bg
        for i in entries:
            i["fg"] = fg
            i["bg"] = bg
            i["selectborderwidth"] = 1