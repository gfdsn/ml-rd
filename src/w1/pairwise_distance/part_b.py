import numpy as np

def pairwise_distance(X: np.ndarray) -> np.ndarray:
    # Gram Matrix, G = X * X^T
    G = X.dot(X.transpose())

    # N stands for norms
    N = np.diagonal(G)

    # Pairwise sum through broadcasting
    X1 = N[np.newaxis, :] + N[:, np.newaxis]

    # Squared distances
    Z = X1 - (2 * G)

    return np.sqrt(Z)

def main() -> None:

    # Sample matrix
    X = np.array([
        [0, 0,],
        [3, 4,],
        [0, 4]
    ])

    D = pairwise_distance(X)
    print()
    
main()