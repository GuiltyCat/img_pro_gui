#!/usr/bin/env python
# -*- conding: utf-8 -*-
import os
import tkinter as tk
import tkinter.ttk as ttk

import cv2
from PIL import Image, ImageTk


class Param:
    def __init__(self, name, default, limit, odd=False):
        self.name = name
        self.limit = limit
        self.default = default
        self.value = self.default
        self.odd = odd

    def min(self):
        return self.limit[0]

    def max(self):
        return self.limit[1]

    def restrict(self, value):
        if self.odd and value % 2 == 0:
            value += 1

        value = max(value, self.min())
        value = min(value, self.max())
        return value

    def __call__(self, value=None):
        if value is None:
            return value
        self.value = value
        return None


class Params:
    def __init__(self, **params):
        self.params = params


class ParamsGUI:
    def __init__(self, params):
        self.params = params


class ImageProcessing:
    def __init__(self):
        pass

    def __call__(self, img):

        return img

    def change_params(self):
        return


class ProcessList(ttk.Treeview):
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)


GRID_EXPAND_ALL = (tk.N, tk.S, tk.E, tk.W)


class ImageProcessList(ttk.Frame):
    def __init__(self, master, **kw):
        ttk.Frame.__init__(self, master, **kw)
        names = ["二値化", "適応二値化", "ガウシアンブラー"]

        for i, n in enumerate(names):
            ttk.Button(self, text=n).grid(row=i, column=0, sticky=tk.W)


class ProcessListWithScrollBar(ttk.Frame):
    def __init__(self, master, **kw):
        ttk.Frame.__init__(self, master, **kw)
        self.process_list = ProcessList(self)
        self.scroll = ttk.Scrollbar(
            self, orient="vertical", command=self.process_list.yview
        )

        self.process_list.grid(row=0, column=0, sticky=GRID_EXPAND_ALL)
        self.scroll.grid(row=0, column=1, sticky=tk.N + tk.S)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


class ImageCanvas(ttk.Label):
    def __init__(self, master, **kw):
        ttk.Label.__init__(self, master, **kw)

    def change(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)
        self.configure(image=img_tk)
        self.image = img_tk


class ImgProApp(ttk.Frame):
    def __init__(self, master, **kw):
        tk.Frame.__init__(self, master, **kw)
        self.master = master

        self.image_process_list = ImageProcessList(self)
        # self.process_list = ProcessList(self)
        self.process_list = ProcessListWithScrollBar(self)
        self.image_canvas = ImageCanvas(self)

        self.image_process_list.grid(row=0, column=0, sticky=GRID_EXPAND_ALL)
        self.process_list.grid(row=0, column=1, sticky=GRID_EXPAND_ALL)
        self.image_canvas.grid(row=0, column=2, sticky=GRID_EXPAND_ALL)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # self.image_canvas.change(cv2.imread("/home/miyamoto/download/hVtUVi0.jpg"))


def main():

    root = tk.Tk()
    ImgProApp(root).grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()
    pass


if __name__ == "__main__":
    main()
