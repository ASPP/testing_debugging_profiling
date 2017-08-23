import numpy as np
from py.test import raises

from telescope_model import TelescopeModel


def test_unsafe_elevation_angle():
    telescope = TelescopeModel(address='10.2.1.1')
    elevation_angle = np.pi / 2.0

    with raises(ValueError):
        telescope.set_elevation_angle(elevation_angle)
