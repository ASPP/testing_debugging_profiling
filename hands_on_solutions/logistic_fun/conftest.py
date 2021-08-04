import numpy as np
import pytest

# add a commandline option to pytest
def pytest_addoption(parser):
    """Add random seed option to py.test.
    """
    parser.addoption('--seed', dest='seed', type=int, action='store',
                     help='set random seed')

# configure pytest to automatically set the rnd seed if not passed on CLI
def pytest_configure(config):
    seed = config.getvalue("seed")
    # if seed was not set by the user, we set one now
    if seed is None or seed == ('NO', 'DEFAULT'):
        config.option.seed = int(np.random.randint(2**31-1))

def pytest_runtest_setup(item):
    # set random seed before running each test
    # so that a failure in a test can be reproduced just running
    # that particular test. if this was not done, you would need
    # to run the whole test suite again
    np.random.seed(item.config.option.seed)

def pytest_report_header(config):
    return f'Using random seed: {config.option.seed}'

