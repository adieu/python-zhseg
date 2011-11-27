%module mmseg
%{
#include "algor.h"
%}

%typemap(in) (const char *text, int length) {
    $1 = PyString_AsString($input);
    $2 = PyString_Size($input);
};

namespace rmmseg
{
    namespace dict
    {
        bool  load_chars(const char *filename);
        bool  load_words(const char *filename);
    }

    class Algorithm
    {
    public:
        Algorithm(const char *text, int length);
        %extend {
            PyObject *next_token() {
                PyObject *resultobj = 0;
                rmmseg::Token token = $self->next_token();
                resultobj = PyString_FromStringAndSize((&token)->text, (&token)->length);
                return resultobj;
            }
        }
    };
}
