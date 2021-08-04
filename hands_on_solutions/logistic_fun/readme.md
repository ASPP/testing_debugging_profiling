# Testing Project for ASPP 2021 Bordeaux

## Setup
In the file logistic.py complete the code for the two functions
Implement the logistic function f(𝑥)=𝑟∗𝑥∗(1−𝑥)
Implement a function runs for n iterations, each time passing the result back into f. This is called an iterated function.

## Visualize
Look at the file `plot_logfun.py` and change lines 37-40 to use the parameter values you like. Then run `plot_logfun.py` to generate the plots.

## Exercise 1
Create a `test_logistic.py` file. Import the relevant libraries!
Write a basic test, that checks that once a point is on the attractor it doesn't move off it! For an r = 1.5 the attracting fixed point is at 1/3!

## Exercise 2
Now write a test for checking that with different starting values the trajectories all converge on the same attractor. Use the same r value as above but use parametrize to try a few different starting values.

## Exercise 3:
Trajectories using r values above 4 diverge to negative infinity. Pick an r value above 5 and check that a few iterations later the outcome is -inf for different starting values.

## Exercise 3.2:
Expand your test to use numerical fuzzing to pick an arbitrary value of r > 4.
**hint** to chose an arbitrary number between two bounds, how about np.random.uniform(low=4, high=15)

## Exercise 3.3:
Now take 3 as a lower bound for r! Run the code a couple of times. Is there a problem? Use the visualization script to investigate what is going on with values that dont seem to work.
**hint:** if you want print statements to show up in your pytest output you can use the flag `-s`

## Exercise 4:
r values or 3 < r > 4 have some interesting properties. A chaotic trajectory doesn't diverge but also doesn't converge. Write a test that checks that after a lot (e.g. 100000) of iterations the last 100 are all different. Use r=3.8.
## Exercise 4.2:
parametrize your test with some other r values: like 3.001, and 3.453. Your test should fail. Why? Use the plotting function `plot_trajectory` to find out what is going on.

## Exercise 4.3:
Mark the `test_aperiodic` function as expected to fail!

## Exercise 5:
To test chaotic behavior we will need to be a bit more advanced.
Let's test that what we're seeing is actually chaos:
- orbits mus be bounded, i.e. not diverge: you can use your divergence code for this
- orbits must be aperiodic, i.e. only values of r that pass the test_aperiodic function can qualify
- sensitive dependence on initial conditions
- it has to be deterministic

We already established the first two. Lets write tests for the last two!

## Exercise 5.1:
Look at the bifurcation plot and single trajectory plot and pick an r value that you think will likely yield chaos. Then write a test to verify that the trajectory is deterministic.

## Exercise 5.2:
For the same r value, test the sensitive dependence on initial conditions, or the butterfly effect. Use the following definition of SDIC.

>`f` is a function and `x0` and `y0` are two possible seeds.
>If `f` has SDIC then:
>there is a number `delta` such that for any `x0` there is a `y0` that is not
>more than `init_error` away from `x0`, where the initial condition `y0` has
>the property that there is some integer n such that after n iterations, the
>orbit is more than `delta` away from the orbit of `x0`. That is
>|xn-yn| > delta