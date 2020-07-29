#!/usr/bin/env python
# -*- conding: utf-8 -*-
import os
import tkinter as tk
import tkinter.ttk as ttk

import cv2
import wx


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


def main():
    pass


if __name__ == "__main__":
    main()
