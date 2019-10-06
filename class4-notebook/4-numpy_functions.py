#!/usr/bin/env python3

import numpy as np


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# Let's first create a sample array to check its functions
random_int_array = np.random.randint(1, 100, 20)

pretty_print('random_int_array', random_int_array)

# We can use mean, min, max and std to immediately extract stats on our datasets
pretty_print('random_int_array.mean()', random_int_array.mean())
pretty_print('random_int_array.min()', random_int_array.min())
pretty_print('random_int_array.max())', random_int_array.max())
pretty_print('random_int_array.std()', random_int_array.std())

# Let's reshape this array into a matrix
reshaped_random_int_matrix = random_int_array.reshape(5, 4)

# We can apply the very same operations on a numpy matrix
pretty_print('reshaped_random_int_matrix.mean()', reshaped_random_int_matrix.mean())
pretty_print('reshaped_random_int_matrix.min()', reshaped_random_int_matrix.min())
pretty_print('reshaped_random_int_matrix.max()', reshaped_random_int_matrix.max())
pretty_print('reshaped_random_int_matrix.std()', reshaped_random_int_matrix.std())

# We then can for example apply the same method to a row only
pretty_print('reshaped_random_int_matrix[1].mean()', reshaped_random_int_matrix[1].mean())
