import os.path
import _mmseg


DEFAULT_CHARACTER_DICT = os.path.join(os.path.dirname(__file__), 'data', 'chars.dic')
DEFAULT_WORD_DICT = os.path.join(os.path.dirname(__file__), 'data', 'words.dic')


class Algorithm(object):
    def __init__(self, text):
        """\
        Create an Algorithm instance to segment text.
        """
        self.text      = text # add a reference to prevent the string buffer from 
                              # being GC-ed
        self.algor     = _mmseg.mmseg_algor_create(text, len(text))
        self.destroied = False

    def __iter__(self):
        """\
        Iterate through all tokens. Note the iteration has
        side-effect: an Algorithm object can only be iterated
        once.
        """
        while True:
            tk = self.next_token()
            if tk is None:
                raise StopIteration
            yield tk
    
    def next_token(self):
        """\
        Get next token. When no token available, return None.
        """
        if self.destroied:
            return None
        
        tk = _mmseg.mmseg_next_token(self.algor)
        if len(tk) == 0:
            # no token available, the algorithm object
            # can be destroied
            self._destroy()
            return None
        else:
            return tk

    def _destroy(self):
        
        if not self.destroied:
            _mmseg.mmseg_algor_destroy(self.algor)
            self.destroied = True

    def __del__(self):
        self._destroy()


class Segmenter(object):
    """docstring for Segmenter"""
    def __init__(self):
        self.dict_loaded = False

    def load_character_dict(self, character_dict):
        """docstring for load_character_dict"""
        _mmseg.mmseg_load_chars(character_dict)

    def load_word_dict(self, word_dict):
        """docstring for load_word_dict"""
        _mmseg.mmseg_load_words(word_dict)

    def load_dict(self, character_dict=DEFAULT_CHARACTER_DICT, word_dict=DEFAULT_WORD_DICT):
        """docstring for load_dict"""
        self.load_character_dict(character_dict)
        self.load_word_dict(word_dict)
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
