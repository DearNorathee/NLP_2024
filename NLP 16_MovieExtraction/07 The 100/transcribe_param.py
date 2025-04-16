transcribe(
    audio: Union[str, BinaryIO, np.ndarray]
    , language: Optional[str]=None
    , task: str="transcribe"
    , log_progress: bool=False
    , beam_size: int=5
    , best_of: int=5
    , patience: float=1
    , length_penalty: float=1
    , repetition_penalty: float=1
    , no_repeat_ngram_size: int=0, temperature: Union[float, List[float], Tuple[float, ...]]=[ 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, ], compression_ratio_threshold: Optional[float]=2.4, log_prob_threshold: Optional[float]=-1.0, no_speech_threshold: Optional[float]=0.6, condition_on_previous_text: bool=True, prompt_reset_on_temperature: float=0.5, initial_prompt: Optional[Union[str, Iterable[int]]]=None, prefix: Optional[str]=None, suppress_blank: bool=True, suppress_tokens: Optional[List[int]]=[-1], without_timestamps: bool=False, max_initial_timestamp: float=1.0, word_timestamps: bool=False, prepend_punctuations: str="\"'“¿([{-", append_punctuations: str="\"'.。,,!!??::”)]}、", multilingual: bool=False, vad_filter: bool=False, vad_parameters: Optional[Union[dict, VadOptions]]=None, max_new_tokens: Optional[int]=None, chunk_length: Optional[int]=None, clip_timestamps: Union[str, List[float]]="0", hallucination_silence_threshold: Optional[float]=None, hotwords: Optional[str]=None, language_detection_threshold: Optional[float]=0.5, language_detection_segments: int=1) -> Tuple[Iterable[Segment], TranscriptionInfo]