# Hangman
Hangman Game

  In this game, the computer selects a word in random from a list of words. The computer prints a blank ('_') for each letter in word. The user guesses a letter in the word. If the letter is present in the word, the computer fills the
blank with the letter. If the letter is not present, the miss count is incremented. The computer displays a hangman diagram corresponding to the miss count. If the user is able to find the word, before 8 misses, the user wins the game. Else the hangman diagram gets completed and the user looses the game. The different stages of the hangman for each miss count is shown below.
```
 Stage 1




-+-

Stage 2

 |
 |
 |
-+-

Stage 3

 +---
 |
 |
 |
-+-

Stage 4

 +--+
 |  O
 |
 |
-+-

Stage 5

 +--+
 |  O
 |  |
 |
-+-

Stage 6

 +--+
 |  O
 | /|\
 |
-+-

Stage 7

 +--+
 |  O
 | /|\
 | / \
-+-

A sample run of the game is shown below, for the word INDIA.

_ _ _ _ _

Enter a letter: A

        A
_ _ _ _ _

Enter a letter: I

I     I A
_ _ _ _ _

Enter a letter: E





-+-

I     I A
_ _ _ _ _

Enter a letter: M


 |
 |
 |
-+-

I     I A
_ _ _ _ _

Enter a letter: F

 +---
 |
 |
 |
-+-

I     I A
_ _ _ _ _
```
