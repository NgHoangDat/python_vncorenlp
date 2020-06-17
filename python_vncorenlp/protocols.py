from typing import *

from typing_extensions import Protocol


class Vocabulary(Protocol):

    def __init__(self, path:str):
        ...


class WordSegmenter(Protocol):

    def __init__(self, path:str, vocab:Vocabulary):
        ...



class PosTagger(Protocol):

    def __init__(self, path:str):
        ...


class GlobalLexica(Protocol):
    ...


class LexicalInitializer(Protocol):

    def __init__(self, cluster:str, embedding:str):
        ...

    def initializeLexica(self) -> GlobalLexica:
        ...


class NerRecognizer(Protocol):

    def __init__(self, path:str, lexica:GlobalLexica):
        ...



class DependencyParser(Protocol):

    def __init__(self, path:str, lexica:GlobalLexica):
        ...


class VnCoreNLP(Protocol):

    def __init__(self):
        ...

    def setWordSegmenter(segmenter:WordSegmenter):
        ...

    def setPosTagger(postagger:PosTagger):
        ...

    def setNerRecognizer(recognizer:NerRecognizer):
        ...

    def setDependencyParser(parser:DependencyParser):
        ...
