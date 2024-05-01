# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 15:21:45 2023

@author: Heng2020
"""
import os
import comtypes.client


def docx_to_pdf(docx_path, pdf_path):
    # Load the required Word application
    word = comtypes.client.CreateObject('Word.Application')
    word.Visible = False
    
    # Ensure the output directory exists
    if not os.path.isdir(os.path.dirname(pdf_path)):
        os.makedirs(os.path.dirname(pdf_path))

    # Open the .docx file
    doc = word.Documents.Open(docx_path)
    doc.SaveAs(pdf_path, FileFormat=17)  # 17 represents the wdFormatPDF enumeration
    
    # Close the Word application
    doc.Close()
    word.Quit()
    

docx_path = 'path/to/your/document.docx'
pdf_path = 'path/to/your/document.pdf'
docx_to_pdf(docx_path, pdf_path)