# Pairwise Distance

## Problem

Let $`X \in \mathbb{M}_{n \times d}(\mathbb{R})`$, where each row $`x_i \in \mathbb{R}^{d}`$ is a point. Return $`D \in \mathbb{M}_{n \times n}(\mathbb{R})`$ where:

$$
D_{ij} = \sqrt{\sum_{k=1}^{d}(x_{ik} - x_{jk})^2}, \space \forall \space i,j \in \{1, ..., n \}
$$

## Restrictions

- Do not use loops (nor list comprehensions)
- Consider $n \ge 1$ and $d \ge 1$
- Do not modify $X$

## Signature

```py
def pairwise_distance(X: np.ndarray) -> np.ndarray:
    ...
```

## Steps

- Used _numpy_ **basic indexing** and **basic slicing** (`X[np.newaxis, :, :]` and `X[:, np.newaxis, :]`) to rearrange  the coordinates inside X

`np.newaxis` adds a new axis in its position in the tuple, increasing the dimension of the result by $1$.

- Learned the concept **broadcasting** from _numpy_

When trying to apply operations between two different matrices with different dimensions, _numpy_ "expands" the number of axes of both matrices in order to match their shape.
$\space$
