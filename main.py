#!/usr/bin/env python
# -*- coding: utf8 -*-

import cups
from fpdf import FPDF

class Blank:
    """Class for creating pdf document for printing."""

    def __init__(self):
        self.filename = "./temprorary/file2print.pdf"
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font('DejaVu', '', 10)

        name = input("Name: ")
        surname = input("Surname: ")
        date = input("Date of birthday: ")

        self.text = "   Україна\n"
        self.text += "  Київська область, м. Буча\n"
        self.text += "  КНП 'Бучанський консультативно-діагностичний\n"
        self.text += "  центр' Бучанської міської ради\n"
        self.text += "  ідентифікаційний номер 42081679\n"
        self.text += "\n      " + name
        self.text += "\n      " + surname
        self.text += "\n      " + date

        for txt in self.text.split("\n"):
            pdf.write(5, txt)
            pdf.ln(5)

        pdf.output(self.filename, 'F')

nice = Blank()
