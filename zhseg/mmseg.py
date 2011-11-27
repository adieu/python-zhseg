import os.path
import _mmseg


DEFAULT_CHARACTERS_DICT = os.path.join(os.path.dirname(__file__), 'data', 'chars.dic')
DEFAULT_WORDS_DICT = os.path.join(os.path.dirname(__file__), 'data', 'words.dic')


class Algorithm(object):
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
    """docstring for Segmenter"""
    def __init__(self):
        self.dict_loaded = False

    def load_characters_dict(self, characters_dict):
        """docstring for load_character_dict"""
        _mmseg.load_chars(characters_dict)

    def load_words_dict(self, words_dict):
        """docstring for load_word_dict"""
        _mmseg.load_words(words_dict)

    def load_dict(self, characters_dict=DEFAULT_CHARACTERS_DICT, words_dict=DEFAULT_WORDS_DICT):
        """docstring for load_dict"""
        self.load_characters_dict(characters_dict)
        self.load_words_dict(words_dict)
        self.dict_loaded = True

    def segment(self, text):
        """docstring for segment"""
        if not self.dict_loaded:
            self.load_dict()
        return Algorithm(text)


def segment(text):
    """docstring for segment"""
    return segmenter.segment(text)


segmenter = Segmenter()
