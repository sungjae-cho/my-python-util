import numpy as np

def shuffle_np_arrays(x, y):
    '''
    This only shuffle two numpy arrays along 0-dimension.
    Reference: https://tech.pic-collage.com/tips-of-numpy-shuffle-multiple-arrays-e4fb3e7ae2a
    '''
    
    # The dimension to shuffle is 0.
    dim_to_shuffle = 0
    
    # Generate the permutation index array.
    permutation = np.random.permutation(x.shape[dim_to_shuffle])
    
    # Shuffle the arrays by giving the permutation in the square brackets.
    shuffled_x = x[permutation]
    shuffled_y = y[permutation]
    
    return shuffled_x, shuffled_y
