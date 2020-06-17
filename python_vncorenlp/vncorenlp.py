import os
import sys
from typing import *

from . import protocols


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
CLASS_PATH = os.path.join(DATA_DIR, 'vncorenlp.jar')
MODEL_DIR = os.path.join(DATA_DIR, 'models')

VOCAB = 'vocab'
SEGMENTER = 'wordsegmenter.rdr'
TAGGER = 'postagger'
CLUSTER = 'clusters.xz'
EMBEDDING = 'embeddings.xz'
NER = 'ner.xz'
DEP = 'dep.xz'


def install(jar_path:str, *options):
    import jnius_config

    for option in options:
        jnius_config.add_options(option)

    jnius_config.set_classpath(jar_path)



class Package:
    Vocabulary:Optional[Type[protocols.Vocabulary]] = None
    LexicalInitializer:Optional[Type[protocols.LexicalInitializer]] = None
    WordSegmenter:Optional[Type[protocols.WordSegmenter]] = None
    PosTagger:Optional[Type[protocols.PosTagger]] = None
    NerRecognizer:Optional[Type[protocols.NerRecognizer]] = None
    DependencyParser:Optional[Type[protocols.DependencyParser]] = None
    VnCoreNLP:Optional[Type[protocols.VnCoreNLP]] = None

    @classmethod
    def load_class(cls):
        from jnius import autoclass

        cls.Vocabulary = autoclass('vn.corenlp.wordsegmenter.Vocabulary')
        cls.LexicalInitializer = autoclass('vn.pipeline.LexicalInitializer')

        cls.WordSegmenter = autoclass('vn.corenlp.wordsegmenter.WordSegmenter')
        cls.PosTagger = autoclass('vn.corenlp.postagger.PosTagger')
        cls.NerRecognizer = autoclass('vn.corenlp.ner.NerRecognizer')
        cls.DependencyParser = autoclass('vn.corenlp.parser.DependencyParser')

        cls.VnCoreNLP = autoclass('vn.pipeline.VnCoreNLP')


class Pipeline:

    def __init__(self):
        self.instance:Optional[protocols.VnCoreNLP] = None

    def load(self, model_dir:str=MODEL_DIR, 
            vocab:Optional[str]=None, segmenter:Optional[str]=None, 
            tagger:Optional[str]=None, 
            cluster:Optional[str]=None, embedding:Optional[str]=None, 
            ner:Optional[str]=None, dep:Optional[str]=None
        ):
        self.instance = Package.VnCoreNLP()

        if segmenter:
            assert vocab, 'Segmenter need vocab to work'
            vocabulary = Package.Vocabulary(os.path.join(model_dir, vocab))
            segmenter = Package.WordSegmenter(os.path.join(model_dir, segmenter), vocabulary)
            self.instance.setWordSegmenter(segmenter)

        if tagger:
            pos_tagger = Package.PosTagger(os.path.join(model_dir, tagger))
            self.instance.setPosTagger(pos_tagger)

        lexica = None
        if cluster and embedding:
            lexica = Package.LexicalInitializer(
                os.path.join(model_dir, cluster),
                os.path.join(model_dir, embedding)
            ).initializeLexica()

        if ner:
            assert lexica, 'Ner need cluster and embedding to work'
            ner_recognizer = Package.NerRecognizer(os.path.join(model_dir, ner), lexica)
            self.instance.setNerRecognizer(ner_recognizer)

        if dep:
            assert lexica, 'Ner need cluster and embedding to work'
            dep_parser = Package.DependencyParser(os.path.join(model_dir, dep), lexica)
            self.instance.setDependencyParser(dep_parser)

    def annotateText(self, text:str) -> List[List[Tuple[str, str, str, str]]]:
        annotations = self.instance.annotate(text)
        return [
            [
                (word.getForm(), word.getPosTag(), word.getNerLabel(), word.getDepLabel())
                for word in sentence
            ] for sentence in annotations
        ]