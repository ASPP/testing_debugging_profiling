# Testing Project Exercises

## Hands on 1
Add a new test for these generic cases using the for-loop pattern:

    x=0.1, r=2.2 => f(x, r)=0.198
    x=0.2, r=3.4 => f(x, r)=0.544
    x=0.5, r=2   => f(x, r)=0.5


## Hands on 2:
parametrize the above test using @pytest.mark.parametrize


# Hands on 3
Implement a function iterate_f that runs f for it iterations. Write tests for the following cases:
    x=0.1, r=2.2, it=1 => iterate_f(it, x, r)=[0.1, 0.198]
    x=0.2, r=3.4, it=4 => iterate_f(it, x, r)=[0.2, 0.544, 0.843418, 0.449019, 0.841163]
    x=0.5, r=2, it=3 => iterate_f(it, x, r)=[0.5, 0.5, 0.5, 0.5]

# Hands on 4
Write a test for the function fit_r using the parameters recovery method in a new `test_logistic_fit.py` test file.
The test should:
1. Set a initial value for x0 and r
2. Use iterate_f to generate a population trajectory
3. Pass the population trajectory to fit_r and collect the result parameters
4. Check that the fitted r is close enough to the original r

# Hands on 5
In `test_logistic_fit.py` write a randomized test that checks that `fit_r` can recover r for any random value of x0 and r
Write a for loop of 100 iterations, in each iteration create a random x0 and r
Test that `fit_r(xs) == r` ,  where `xs = iterate_f(…)`


# Hands on 6
Write a test that checks for chaotic behavior when r=3.8. Run the logistic
map for 100’000 iterations and verify that the trajectory is between 0 and 1
and then, check that the last 100 iterations are not all the same value.


# Bonus Exercise -- The Butterfly Effect
For the same value of r, test the sensitive dependence on initial conditions, a.k.a. the butterfly effect. Use the following definition of SDIC.
    f is a function and x0 and y0 are two possible seeds. If f has SDIC then:
    there is a number delta such that for any x0 there is a y0 that is not
    more than init_error away from x0, where the initial condition y0 has the
    property that there is some integer n such that after n iterations, the
    orbit is more than delta away from the orbit of x0.
    That is |xn-yn| > delta

