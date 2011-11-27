import os.path
import _mmseg


DEFAULT_CHARACTERS_DICT = os.path.join(os.path.dirname(__file__), 'data', 'chars.dic')
DEFAULT_WORDS_DICT = os.path.join(os.path.dirname(__file__), 'data', 'words.dic')


class Algorithm(object):
    """
    The algorithm class holds the text to be segmented and returns the token iterier.
    """
    def __init__(self, text):
        self.text = text 
        self.algorithm = _mmseg.Algorithm(text)

    def __iter__(self):
        while True:
            token = self.algorithm.next_token()
            if not token:
                raise StopIteration
            yield token


class Segmenter(object):
    """
    The segmenter class manages the dict and segments text.
    """
    def __init__(self):
        self.dict_loaded = False

    def load_characters_dict(self, characters_dict):
        _mmseg.load_chars(characters_dict)

    def load_words_dict(self, words_dict):
        _mmseg.load_words(words_dict)

    def load_dict(self, characters_dict=DEFAULT_CHARACTERS_DICT, words_dict=DEFAULT_WORDS_DICT):
        self.load_characters_dict(characters_dict)
        self.load_words_dict(words_dict)
        self.dict_loaded = True

    def segment(self, text):
        if not self.dict_loaded:
            self.load_dict()
        return Algorithm(text)


def segment(text):
    """
    Helper function to segment text with the default segmenter.
    """
    return segmenter.segment(text)


segmenter = Segmenter()
