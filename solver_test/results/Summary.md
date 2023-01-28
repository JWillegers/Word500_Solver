This file contains some details about different runs.
All runs are done on hard mode
x_width and n_common are variables used in preparation/frequencies.py and are used for the sigmoid function. When changing these values, also run second_guess.py


| Filename    | Start word | Mean  | Fails | x_witdh | n_common | Formula give_n_suggestions                                                              | Notes                             |
|-------------|------------|-------|-------|---------|----------|-----------------------------------------------------------------------------------------|-----------------------------------|
| tares_1.txt | tares      | 5.054 | 7     | 50      | 3000     | score = turn * (1 - word frequency / max_value) + (current uncertainty - entropy)       |                                   |
| tares_2.txt | tares      | 4.999 | 7     | 50      | 3000     | score = 1/2 * turn * (1 - word frequency / max_value) + (current uncertainty - entropy) |                                   |
| tares_3.txt | tares      | 4.928 | 4     | 50      | 3000     | score = 1/4 * turn * (1 - word frequency / max_value) + (current uncertainty - entropy) |                                   |
| tares_4.txt | tares      | 4.916 | 4     | 50      | 3000     | score = turn * (1 - word sigmoid) + (current uncertainty - entropy)                     |                                   |
| tares_5.txt | tares      | 4.913 | 5     | 50      | 3000     | score = 1/2 * turn * (1 - word sigmoid) + (current uncertainty - entropy)               |                                   |                                   |
| entropy.txt | tares      | 5.179 | 5     | 50      | 3000     | score = entropy                                                                         | in score_sorted -> reverse = True |