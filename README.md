#Word500
This is my attempt at creating a solver for [word500](https://www.word500.com/#), a wordle inspired game.

##The game
In 8 guesses or fewer, the player needs to find a 5-letter word. 
But the feedback on a guessed word is a bit different from wordle. 
Instead of knowing if a letter is green, yellow or grey (red in word500), 
the player only gets to know how many letters are green, yellow and red.

##Libraries needed
* Pandas
* tqdm

##Techniques used
* Having a file that known if we have 2 words, how many greens, yellows and reds we get
* Build a GUI with tkinter
* Solver using information theory video from 3B1B
  * Word frequency [TODO]
  * Entropy: E[information]=sum of all x (p(x) * information) [TODO]

##The lookup_table_part folder
Because github has a 100MB file limit, I provided a split lookup table in this folder.

##Sources
* 3Blue1Brown video on wordle: https://www.youtube.com/watch?v=v68zYyaEmEA
    * Corresponding GitHub: https://github.com/3b1b/videos/tree/master/_2022/wordle
* python unittest: https://docs.python.org/3/library/unittest.html
* Tkinter: https://realpython.com/python-gui-tkinter/
* tqdm: https://github.com/tqdm/tqdm