import re

import pandas as pd

# Sample DataFrame
data = {
    'text_column': [
        '12-ABC-1234567-00000-1234-12-34',
        '34-DEF-7654321-00000-5678-34-56',
        '56-GHI-9876543-00000-6789-56-78',
        '12-ABC-1234567-00000-1234-12-34',
        '34-DEF-7654321-00000-5678-34-56',
        '56-GHI-9876543-00000-6789-56-78',
    ],
    'policy_no':["29-SAU-0000084-2024-03 (นางสาว อริสา ชุมพลพันธ์)", 
                 "00-SAU-0001814-2023-07/01, 00-SPU-0001918-2023-07/01 นาย ธเนศ พันธ์หงษ์ #00 Log no.1022,1023", 
                 "00-SAU-0000944-2024-03, 00-SPU-0000607-2024-03 (ห้างหุ้นส่วนจำกัด สาลี่รัช)", 
                 "00-SAB-0000558-2024-03, 00-SPU-0000604-2024-03 นิติบุคคลอาคารชุด ราม 12 คอนโดมิเนียม #00 Log no.1055,1056", 
                 "FW: 00-SAU-0000943-2024-03 คุณ บุญตา แซ่ฉั่ว #00 Log no.1050", 
                 "FW: 00-SAU-0000945-2024-03 00-SPU-0000608-2024-03 บริษัท โฮมชีวิน จำกัด"]
}





def extract_with_regex(df:pd.DataFrame, col:str, pattern:str) -> pd.DataFrame:
    import pandas as pd
    import re
    """
    { {col_1, col_2, col_3} }
    Extracts multiple occurrences of text from a specified column in a DataFrame 
    using a regular expression pattern and splits each extraction into a new column.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the data.
    column : str
        The name of the column from which to extract text.
    pattern : str
        The regular expression pattern to use for extraction.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with each occurrence of the extracted text as a new column.
    """
    # Function to find all matches of the pattern in a string
    def find_all_matches(text, pattern):
        return re.findall(pattern, text)
    out_df = df.copy()
    # Apply the function to each row in the specified column
    out_df['matches'] = out_df[column].apply(lambda x: find_all_matches(x, pattern))
    
    # Determine the maximum number of matches in any row
    max_matches = out_df['matches'].apply(len).max()
    
    # Create new columns for each possible match
    out_cols = [f'{column}_{i+1}' for i in range(max_matches)]
    for i in range(max_matches):
        out_df[f'{column}_{i+1}'] = out_df['matches'].apply(lambda x: x[i] if i < len(x) else None)
    
    # Drop the intermediate 'matches' column
    out_df = out_df[out_cols]
    
    return out_df



df = pd.DataFrame(data)
column = 'policy_no'
# Define the regex pattern
pattern = r'(\d{2}-[A-Z0-9]{3}-\d{7}(?:-00000)?-\d{4}-\d{2}(?:[-\/]\d{2})?)'

# Extract text using the defined function
actual01 = df[column].str.extract(pattern)
actual02 = extract_with_regex(df, column, pattern)
print(actual01)
