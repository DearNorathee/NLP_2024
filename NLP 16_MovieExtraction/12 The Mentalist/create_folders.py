# create Polish folder


#%%
# create working folder
subtitle_folders = [
    'Amazon_temp',
    "Korean",
    "Chinese_Traditional",
    "Arabic",
    "Hebrew",
    "Russian",
    "Greek",
    "Czech",
    "Turkish",
    "Swedish",
    "Finnish",
    "Romanian",
    "Portuguese_EU",
    "Portuguese_Brazil",
    "Polish",
    "Norwegian",
    "Dutch",
    "Hungarian",
    "Italian",
    "French",
    "Spanish_Latin America",
    "Spanish_Spain",
    "German",
    "Danish",
    "English",
]

audio_folders =  [
    'Amazon_temp',
    "German",
    "English",
    "Spanish (Latin America)",
    "Spanish (Spain)",
    "French",
    "Italian",
    "Japanese",
    "Portuguese_Brazil"]


vt.create_series_working_folder(
    series_name = "The Mentalist"
    , create_structure_at = r"C:\C_Video_Python"
    , audio_folders = audio_folders
    , subtitle_folders = subtitle_folders
    , end_seasons = 7)