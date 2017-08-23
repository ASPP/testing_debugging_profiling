
def connect(address):
    import time
    time.sleep(5)
    return '1'

def get_angle(address):
    return 0.0

def set_angle(address, angle):
    if angle < 0 or angle > 1.40:
        raise IOError('Telescope jammed -- please call technical support')
    return True
