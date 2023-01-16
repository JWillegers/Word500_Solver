# Word500
This is my attempt at creating a solver for [word500](https://www.word500.com/#), a wordle inspired game.

## The game
In 8 guesses or fewer, the player needs to find a 5-letter word. 
But the feedback on a guessed word is a bit different from wordle. 
Instead of knowing if a letter is green, yellow or grey (red in word500), 
the player only gets to know how many letters are green, yellow and red.

## Libraries needed
* Pandas
* tqdm
  * Only for running scripts in /preperation and /solver_test
* Matplotlib
  * Only used in /solver_test

## Techniques used
* Having a file that known if we have 2 words, how many greens, yellows and reds we get
* Build a GUI with tkinter
* Solver using information theory video from 3B1B
  * Word frequency
  * Entropy: E[information]=sum of all x (p(x) * information)
  * Score based on word frequency and entropy
    * I'm in no means an expert in choosing a fitting function to calculate the score, so it is heavily inspired by the 3B1B video.

## How well does it perform?
TODO

## The files
 - ### main.py
   From this file you can run the solver. In this file is all the code that makes the GUI work.
 - ### solver.py
    Processing the guess, finding out which words can still be the answer, 
 - calculating their entropy and giving new guess suggestions.
 - ### /lookup_table_part
    Because github has a 100MB file limit, I provided a split lookup table in this folder.
 - ### /unittests
   In this folder where my unittests. Some are deprecated, others are never made. 
They are never made because at some point I switched over to seeing if it works within the GUI, something that I need to work on.
 - ### /solver_test
    Testing solver.py <br>
    In this folder you will find a folder called /results in which you can find a summary of the tests and the corresponding data
 - ### /preparation
    This folder contains data and script to create and load that data. This data is used in the game.


##Sources
* 3Blue1Brown video on wordle: https://www.youtube.com/watch?v=v68zYyaEmEA
    * Corresponding GitHub: https://github.com/3b1b/videos/tree/master/_2022/wordle
* Python unittest: https://docs.python.org/3/library/unittest.html
* Tkinter: https://realpython.com/python-gui-tkinter/
* tqdm: https://github.com/tqdm/tqdm
* Managing Entries: https://stackoverflow.com/questions/44638007/tkinter-when-press-enter-then-it-goes-to-the-next-text-box