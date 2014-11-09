# Valley of Fear - 20

## Problem

The hard drive may be corrupted, but you were able to recover [a small chunk of text](book.txt). Scribbled on the back of the hard drive is a set of mysterious numbers. Can you discover the meaning behind these numbers? (1, 9, 4) (4, 2, 8) (4, 8, 3) (7, 1, 5) (8, 10, 1)

## Hint

Might each set of three numbers represent a word in a message?

## Writeup

Upon close inspection of the `book.txt` and of the hint, it can be concluded that for each ordered triple, the first number represents the paragraph number, the second number represents the line number, and the third number represents the word. The message is:

    the flag is ceremonial plates

## Flag

ceremonial plates