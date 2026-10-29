from w1.pairwise_distance.part_a import pairwise_distance
import numpy as np
import pytest

class TestParts:
    # Generate and return a "random" matrix
    def random_matrix(self, n: int, d: int) -> np.ndarray:
        rng = np.random.default_rng()
        return rng.uniform(low=1, high=100, size=(n, d))

    dimensions = [(1, 1), (3, 4), (8, 5)]
    
    # Test the shape of D
    @pytest.mark.parametrize("dimensions", dimensions) 
    def test_d_shape(self, dimensions):
        X = self.random_matrix(*dimensions)
        n = dimensions[0]

        # Calculate the pairwise distance and return D
        D = pairwise_distance(X)

        # Assert D's shape is the expected nxn
        assert D.shape == (n, n)
        

def main() -> None:
    ...
    
main()