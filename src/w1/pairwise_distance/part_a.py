import numpy as np

def pairwise_distance(X: np.ndarray) -> np.ndarray:

    Y = X[:, np.newaxis, :] - X[np.newaxis, :, :]

    # raise every element from Y to 2  
    Z = np.float_power(Y, 2)

    # sum every element 
    W = np.sum(Z, axis=2)

    # square root everything and return the final array
    return np.sqrt(W)

def main() -> None:
    X = np.array([
        [1, 2],
        [3, 4],
        [5, 6],
    ], dtype=float)

    D = pairwise_distance(X)
    #print(D)
    
main()