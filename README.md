# Wordmaggedon

Wordmaggedon is a project mainly used to beat everyone else at games like skribble.io

## Usage

### To find a word when you only know its length / pattern

use the `findWordsByPattern` using a pattern similar to "p_tte_n"; the program will check all letters that can be replaced on the _ character.

### To find a word when you know its (possible) letters and its length

use the `findWordsByLetters`; if the number of letters is less than the length of the word searched, then the search will include all other letters.