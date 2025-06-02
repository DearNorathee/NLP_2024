# -*- coding: utf-8 -*-
"""
Created on Sun May 18 10:18:21 2025

@author: Norat
"""

import video_toolkit as vt
import os_toolkit as ost
from pathlib import Path
import pandas as pd

portuguese_sub_root_folder = r"C:\C_Video_Python\Portuguese\The 100\Subtitle Ori"

portuguese_sub_folders = []
for i in range(1,8):
    portuguese_sub_folders.append(f"Portuguese Season {str(i).zfill(2)}")
    
ost.create_folders(portuguese_sub_root_folder, portuguese_sub_folders)


vt.srt_to_Excel(srt_path = r"C:\C_Video_Python\Portuguese\The 100\Subtitle Ori\Portuguese Season 01", 
                output_path = r"C:\C_Video_Python\Portuguese\The 100\Subtitle Ori\Portuguese Season 01" )

sub_s1 = vt.sub_to_df(r"C:\C_Video_Python\Portuguese\The 100\Subtitle Ori\Portuguese Season 01")





def df_to_pdf(
    pd_series: pd.Series,
    output_name: str | Path,
    output_folder: str | Path = "",
    font_size: int = 12,
    font: str = "Arial"
    ) -> None:
    # hard to ChatGPT
    from fpdf import FPDF
    
    """
    Export a pandas Series to a PDF file, each entry on a new line.

    Parameters
    ----------
    pd_series : pd.Series
        The series containing text (sentences) to write to the PDF.
    output_name : str | Path
        Filename for the output PDF (e.g., 'result.pdf').
    output_folder : str | Path, optional
        Folder to save the PDF in. Default is current directory.
    font_size : int, optional
        Font size to use. Default is 12.
    font : str, optional
        Font family to use (e.g., 'Arial'). Default is 'Arial'.
    
    Returns
    -------
    None
    """

    # Resolve full output path
    output_path = Path(output_folder) / output_name

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font(family=font, size=font_size)

    for text in pd_series.astype(str):
        pdf.multi_cell(w=20, h=10, text = text)

    pdf.output(str(output_path))

df_to_pdf(sub_s1[0]['sentence'],"The 100 PT_S01E01.pdf",font_size=5,output_folder = r"C:\C_Video_Python\Portuguese\The 100\Subtitle Ori\Portuguese Season 01")



