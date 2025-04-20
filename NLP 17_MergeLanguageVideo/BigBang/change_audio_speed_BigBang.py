# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 11:46:37 2025

@author: Norat
"""
import video_toolkit as vt
from pathlib import Path
from beartype import beartype

# vt.change_audio_speed_1file(audio_path, speedx, output_name)

# /change_audio_speed_1file still have some errors
def test_change_audio_speed_1file():
    audio_path01 = r"C:\C_Video_Python\video_toolkit_test\change_audio_speed_1file\BigBang season1 French\BigBang FR S01E01_FR.mp3"
    # SPEEDX = 0.9612
    SPEEDX = 0.5
    vt.change_audio_speed_1file(audio_path01,SPEEDX,"BigBang FR S01E01_FR_cs.mp3",print_errors=True)



@beartype
def change_audio_speed_1file(
        audio_path: str | Path,
        speedx: int | float,
        output_name: str | Path,
        output_folder: str | Path = "") -> None:
    
    """
    Adjust audio playback speed and export to specified format.

    This function modifies the playback speed of an input audio file and saves it
    with the specified output extension (e.g., .wav, .mp3). The output format is
    automatically determined from the output file extension.

    Parameters
    ----------
    audio_path : str or Path
        Path to the input audio file. Supports all formats recognized by pydub
        (MP3, WAV, OGG, FLAC, etc.).
    speedx : int or float
        Speed multiplier for audio playback:
        - Values < 1.0 will slow down the audio (e.g., 0.5 for half speed)
        - Values > 1.0 will speed up the audio (e.g., 2.0 for double speed)
        - Value of 1.0 maintains original speed
    output_name : str or Path
        Output filename including extension (determines output format).
        Example: "output.wav" for WAV format, "fast.mp3" for MP3 format.
    output_folder : str or Path, optional
        Destination directory for output file. If not specified, uses the same
        directory as the input file.

    Returns
    -------
    None
        Output file is saved to the specified location.

    Raises
    ------
    FileNotFoundError
        If the input audio file does not exist.
    ValueError
        If speedx is zero or negative.
    Exception
        For pydub-related processing errors (e.g., unsupported formats).

    See Also
    --------
    pydub.AudioSegment : Base class used for audio manipulation.

    Notes
    -----
    1. Requires ffmpeg to be installed for handling non-WAV formats.
    2. For batch processing, consider wrapping this function in a loop.

    Examples
    --------
    Slow down audio by 25% and save as WAV:

    >>> change_audio_speed_1file("input.mp3", 0.75, "slow.wav", "output_dir")

    Speed up audio 2x and save as MP3 in same directory:

    >>> change_audio_speed_1file("sound.wav", 2.0, "fast.mp3")
    """
    # medium tested
    
    from pydub import AudioSegment
    from pathlib import Path
    
    # Load audio file (supports MP3, WAV, etc.)
    audio = AudioSegment.from_file(audio_path)

    # Adjust speed (e.g., 0.9764x slower)
    slowed_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * speedx)
    }).set_frame_rate(audio.frame_rate)

    # Determine output folder
    filepath = Path(audio_path)
    folder_path = filepath.parent
    output_folder_in = Path(output_folder) if output_folder else folder_path

    # Ensure the output folder exists
    output_folder_in.mkdir(parents=True, exist_ok=True)

    # Get the output format from the file extension
    output_path = output_folder_in / f"{output_name}"
    output_format = output_path.suffix[1:].lower()  # Remove the dot and convert to lowercase

    # Export slowed audio with the correct format
    slowed_audio.export(output_path, format=output_format)

def test_change_audio_speed_1file_v2():
    # I use this function to create 1 audio per episode
    audio_path01 = r"C:\C_Video_Python\video_toolkit_test\change_audio_speed_1file\BigBang season1 French\BigBang FR S01E13_FR.mp3"
    output_folder = r"C:\C_Video_Python\The Big Bang Theory\BigBang Theory Season 01\Season 01 Audio\French_adj_speed"
    SPEEDX = 0.95903619926980600
    vt.change_audio_speed_1file(audio_path01,SPEEDX,"BigBang FR S01E13_FR_cs_v2.mp3",output_folder = output_folder)
    
test_change_audio_speed_1file_v2()
# test_change_audio_speed_1file()