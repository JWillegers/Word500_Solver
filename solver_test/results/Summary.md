This file contains some details about different runs. <br>
All runs are done on hard mode <br>
x_width and n_common are variables used in preparation/frequencies.py and are used for the sigmoid function. When changing these values, also run second_guess.py <br>


| Filename       | Start word | Mean  | Fails | x_witdh | n_common | Formula give_n_suggestions                                                              | Notes                             |
|----------------|------------|-------|-------|---------|----------|-----------------------------------------------------------------------------------------|-----------------------------------|
| tares_50_1.txt | tares      |       |       | 50      | 3000     | score = turn * (1 - word frequency / max_value) + (current uncertainty - entropy)       |                                   |
| tares_50_2.txt | tares      |       |       | 50      | 3000     | score = 1/2 * turn * (1 - word frequency / max_value) + (current uncertainty - entropy) |                                   |
| tares_50_3.txt | tares      |       |       | 50      | 3000     | score = 1/4 * turn * (1 - word frequency / max_value) + (current uncertainty - entropy) |                                   |
| tares_50_4.txt | tares      |       |       | 50      | 3000     | score = turn * (1 - word sigmoid / total_value) + (current uncertainty - entropy)       |                                   |
| tares_50_5.txt | tares      |       |       | 50      | 3000     | score = 1/2 * turn * (1 - word sigmoid / total_value) + (current uncertainty - entropy) |                                   |  
| entropy_50.txt | tares      |       |       | 50      | 3000     | score = entropy                                                                         | in score_sorted -> reverse = True |
| tares_25_1.txt | tares      | 4.890 | 1     | 25      | 3000     | score = 1/2 * turn * (1 - word sigmoid / total_value) + (current uncertainty - entropy) |                                   |
| tares_25_2.txt | tares      | 4.893 | 2     | 25      | 3000     | score = turn * (1 - word sigmoid / total_value) + (current uncertainty - entropy)       |                                   |
| tares_25_3.txt | tares      | 5.053 | 4     | 25      | 3000     | score = turn * (1 - word frequency / max_value) + (current uncertainty - entropy)       |                                   |