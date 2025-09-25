from numpy.testing import assert_allclose

from logistic import f


def test_f_corner_cases():
    # Test cases are (x, r, expected)
    cases = [
        (0, 1.1, 0),
        (1, 3.7, 0),
    ]
    for x, r, expected in cases:
        result = f(x, r)
        assert_allclose(result, expected)

# Hands on 1
#Add a new test for these generic cases using the for-loop pattern:
# x=0.1, r=2.2 => f(x, r)=0.198
# x=0.2, r=3.4 => f(x, r)=0.544
# x=0.5, r=2   => f(x, r)=0.5


# Hands on 2:
# parametrize the above test using @pytest.mark.parametrize


# Hands on 3
# Implement a function iterate_f that runs f for it iterations. Write tests for the following cases:
# x=0.1, r=2.2, it=1 => iterate_f(it, x, r)=[0.1, 0.198]
# x=0.2, r=3.4, it=4 => iterate_f(it, x, r)=[0.2, 0.544, 0.843418, 0.449019, 0.841163]
# x=0.5, r=2, it=3 => iterate_f(it, x, r)=[0.5, 0.5, 0.5, 0.5]
