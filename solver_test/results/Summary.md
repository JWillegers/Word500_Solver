This file contains some details about different runs

| Filename    | Start word | Mean  | Fails | Formula give_n_suggestions                                                              |
|-------------|------------|-------|-------|-----------------------------------------------------------------------------------------|
| tares_1.txt | tares      | 5.054 | 7     | score = turn * (1 - word frequency / max_value) + (current uncertainty - entropy)       |  
| tares_2.txt | tares      | 4.999 | 7     | score = 1/2 * turn * (1 - word frequency / max_value) + (current uncertainty - entropy) |
| tares_3.txt | tares      | 4.928 | 4     | score = 1/4 * turn * (1 - word frequency / max_value) + (current uncertainty - entropy) |