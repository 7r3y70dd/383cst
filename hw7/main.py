from scipy.stats import binom

n = 5

p = 0.6

k = 3

probability = binom.pmf(k, n, p)
print(probability)