# sub for moving title
import pandas as pd

import excel_tool as xt
import excel_tool.range as rg
import excel_tool.workbook as wb
import excel_tool.worksheet as ws

import xlwings as xw
from tqdm import tqdm

def main():
    excel_path = r"C:\Users\Heng2020\OneDrive\D_Documents\_Learn Languages\_LearnLanguages 02 Main\Duolingo\Duolingo French 02.xlsm"
    wb01 = wb.returnAsWB(excel_path)
    sheet_name = "formated"
    ws01 = ws.ws_at_WB(sheet_name, wb01)
    to_replace_rng: xw.main.Range

    orange = hex_to_rgb("#FFC000")
    
    # for i in tqdm(range(1,4000)):
    #     title_adr = "J" + str(i)
    #     boolean_adr = "F" + str(i)
    #     to_replace_adr = "B" + str(i)

    #     to_replace_rng = ws01.range(to_replace_adr)

    #     title = ws01.range(title_adr).value
    #     is_replaced = ws01.range(boolean_adr).value

    #     if title not in [None,""]:
    #         to_replace_rng.value = title
    #         to_replace_rng.api.Interior.Color = xw.utils.rgb_to_int(orange)
    
    clear_empty_cell_run()
    print("Done")

def clear_empty_cell_run():
    excel_path = r"C:\Users\Heng2020\OneDrive\D_Documents\_Learn Languages\_LearnLanguages 02 Main\Duolingo\Duolingo French 02.xlsm"
    wb01 = wb.returnAsWB(excel_path)
    sheet_name = "formated"
    ws01 = ws.ws_at_WB(sheet_name, wb01)
    
    rng: xw.main.Range
    curr_rng: xw.main.Range

    rng = ws01.range("A1:A3500")

    clear_empty_cell(rng)
    print("Done from clear_empty_cell_run")
    


def clear_empty_cell(rng):
    # it would clear the cell with ""(empty string)
    # to make sure that it would be seen in Excel as truely empty

    # works not
    
    # .clear doesn't work
    # I need to use .value = None instead
    from tqdm import tqdm
    for curr_rng in tqdm(rng):
        if curr_rng.value in [None,""]:
            curr_rng.value = None

def hex_to_rgb(hex_color):
    """ Convert hex color to an RGB tuple. """
    hex_color = hex_color.lstrip('#')  # Remove the '#' symbol if it exists
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))  # Convert to RGB tuple

if __name__ == "__main__":
    main()