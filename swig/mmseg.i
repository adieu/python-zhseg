%module mmseg
%{
#include "mmseg.h"
%}

%typemap(out) Token {
    $result = PyString_FromStringAndSize($1.text, $1.length);
}

extern int mmseg_load_chars(const char *path);
extern int mmseg_load_words(const char *path);
extern void mmseg_dic_add(const char *word, int len, int freq);
extern rmmseg::Algorithm *mmseg_algor_create(const char *text, int len);
extern void mmseg_algor_destroy(rmmseg::Algorithm *algor);
extern Token mmseg_next_token(rmmseg::Algorithm *algor);
