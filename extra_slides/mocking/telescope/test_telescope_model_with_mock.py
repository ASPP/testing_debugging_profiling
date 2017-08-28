from unittest import mock

import numpy as np
from py.test import raises

from telescope_model import TelescopeModel


def test_unsafe_elevation_angle():
    with mock.patch('telescope_model.telescope_driver'):
        telescope = TelescopeModel(address='10.2.1.1')
        elevation_angle = np.pi / 2.0
        with raises(ValueError):
            telescope.set_elevation_angle(elevation_angle)


def test_model_initialization():
    connection_id = 'bogus_connection'
    initial_angle = 1.23

    with mock.patch('telescope_model.telescope_driver') as driver:
        driver.connect.return_value = connection_id
        driver.get_angle.return_value = initial_angle

        telescope = TelescopeModel(address='10.2.1.1')
        assert telescope.connection == connection_id
        assert driver.connect.call_count == 1
        assert telescope.current_angle == initial_angle
    
