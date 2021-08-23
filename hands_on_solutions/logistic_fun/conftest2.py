import numpy as np
import pytest

SEED = 42

@pytest.fixture
def random_state():
    print(f'Seed: {SEED}')
    random_state = np.random.RandomState(SEED)
    return random_state
