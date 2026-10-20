import numpy as np

def pairwise_distance(X: np.ndarray) -> np.ndarray:

    Y = X[:, None, :] - X[None, :, :]

    # raise every element from Y to 2  
    Z = np.float_power(Y, 2)

    # sum every element 
    # try to understand the changes in the array made by the axis, in the sum
    W = np.sum(Z, axis=2)

    # square root everything and return the final array
    return np.sqrt(W)

def main() -> None:
    X = np.array([
        [1, 2, 5],
        [4, 6, 5],
        [1, 2, 1],
    ], dtype=float)

    D = pairwise_distance(X)
    print(D)

main()