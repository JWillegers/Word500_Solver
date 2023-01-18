This file contains some details about different runs.
All runs are done on hard mode
All test are run with x_width = 50 and n_common = 3000 in line 21 and 22 in preparation/frequencies.py

| Filename    | Start word | Mean  | Fails | Formula give_n_suggestions                                                              | Notes                             |
|-------------|------------|-------|-------|-----------------------------------------------------------------------------------------|-----------------------------------|
| tares_1.txt | tares      | 5.054 | 7     | score = turn * (1 - word frequency / max_value) + (current uncertainty - entropy)       |                                   |
| tares_2.txt | tares      | 4.999 | 7     | score = 1/2 * turn * (1 - word frequency / max_value) + (current uncertainty - entropy) |                                   |
| tares_3.txt | tares      | 4.928 | 4     | score = 1/4 * turn * (1 - word frequency / max_value) + (current uncertainty - entropy) |                                   |
| tares_4.txt | tares      | 4.916 | 4     | score = turn * (1 - word sigmoid) + (current uncertainty - entropy)                     |                                   |
| entropy.txt | tares      | 5.179 | 5     | score = entropy                                                                         | in score_sorted -> reverse = True |