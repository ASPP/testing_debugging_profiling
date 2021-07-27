import numpy as np
import matplotlib.pyplot as plt

def f(x, r):
  return r*x*(1-x)

def iterate_f(it, xi, r):
  l = []
  x = xi
  for i in range(it):
    l.append(x)
    x = f(x, r)
  return np.array(l)