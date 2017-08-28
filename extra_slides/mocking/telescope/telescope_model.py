import telescope_driver


class TelescopeModel(object):

    # Minimum safe elevation angle (see handbook).
    MIN_ANGLE = 0.0

    # Maximum safe elevation angle (see handbook).
    MAX_ANGLE = 80.0

    def __init__(self, address):
        self.address = address
        # Connect to telescope
        self.connection = telescope_driver.connect(address)
        # Get initial state of telescope.
        self.current_angle = telescope_driver.get_angle(self.connection)

    def set_elevation_angle(self, angle):
        """ Set the elevation angle of the telescope (in rad).

        If the angle is outside the range allowed by the manufacturer,
        raise a ValueError.
        """

        if angle < self.MIN_ANGLE or angle > self.MAX_ANGLE:
            raise ValueError('Unsafe elevation angle: {}'.format(angle))

        telescope_driver.set_angle(self.connection, angle)
        self.current_angle = angle
