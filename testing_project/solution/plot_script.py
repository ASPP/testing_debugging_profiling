
from plot_logistic import plot_trajectory, plot_bifurcation

# Example usage
n = 10
r = 3.6
x0 = 0.1
plot_trajectory(n, r, x0, fname="single_trajectory.png")

start = 2.5 # starting r value for the bifurcation diagram
end = 4.2 # ending r value for the bifurcation diagram
step = 0.001 # step size for the r values in the bifurcation diagram
it = 1000 # how many iterations to run for each r value
last = 300 # how many of the last iterates to plot
plot_bifurcation(start, end, step, fname="bifurcation.png", it=1000, last=300)
