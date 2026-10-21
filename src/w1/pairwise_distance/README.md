# Pairwise Distance

**Problem**: Let $X \in \mathbb{R}_{n \times d}$, where each row $x_i \in \mathbb{R}^{d}$ is a point. Return $D \in \mathbb{R}_{n \times n}$ where:

$$
D_{ij} = \sqrt{\sum_{k=1}^{d}(x_{ik} - x_{jk})^2}, \space \forall \space i,j \in \{1, ..., n \}
$$

**Restrictions**:
- Do not use loops (nor list comprehensions)
- Consider $n \ge 1$ and $d \ge 1$
- Do not modify $X$


**Signature**:
```py
def pairwise_distance(X: np.ndarray) -> np.ndarray:
    ...
```
