#Word500
This is my attempt at creating a solver for [word500](C:\Users\jonat\PycharmProjects\AdventOfCode2022), a wordle inspired game.

##The game
In 8 guesses or fewer, the player needs to find a 5-letter word. 
But the feedback on a guessed word is a bit different from wordle. 
Instead of knowing if a letter is green, yellow or grey (red in word500), 
the player only gets to know how many letters are green, yellow and red.

##Techniques used
* I started off by reducing the word list based on the amount of greens and yellows I got




##Sources
* 3Blue1Brown video on wordle: https://www.youtube.com/watch?v=v68zYyaEmEA
    * Corresponding GitHub: https://github.com/3b1b/videos/tree/master/_2022/wordle
* python unittest: https://docs.python.org/3/library/unittest.html