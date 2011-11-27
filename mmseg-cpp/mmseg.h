/**
 * A C interface to mmseg-cpp. Will be compiled to a
 * shared library.
 */

#include "token.h"
#include "dict.h"
#include "algor.h"

#if defined(_MSC_VER) // Microsoft compiler
#    define DLLEXPORT __declspec(dllexport)
#elif defined(__GNUC__) // GNU compiler
#    define DLLEXPORT
#else
#    error Unknown compiler, donot know how to process dllexport
#endif


extern "C" {
    
    struct Token
    {
        const char *text;
        int offset;
        int length;
    };

    /*
     * Load a character dictionary.
     */
    DLLEXPORT
	int mmseg_load_chars(const char *path);

    /*
     * Load a word dictionary.
     */ 
    DLLEXPORT
	int mmseg_load_words(const char *path);
    
    /*
     * Add a word to the in-memory dictionary.
     *
     * - word is a String.
     * - length is number of characters (not number of bytes) of the
     *   word to be added.
     * - freq is the frequency of the word. This is only used when
     *   it is a one-character word.
     */
    DLLEXPORT
	void mmseg_dic_add(const char *word, int len, int freq);

    /*
     * Create an Algorithm object.
     *
     * - text is the text to process. It is OK to contain NUL
     *   character.
     * - len is the length (number of bytes) of the text.
     */
    DLLEXPORT
	rmmseg::Algorithm *mmseg_algor_create(const char *text, int len);

    DLLEXPORT
	void mmseg_algor_destroy(rmmseg::Algorithm *algor);

    DLLEXPORT
	Token mmseg_next_token(rmmseg::Algorithm *algor);
}
