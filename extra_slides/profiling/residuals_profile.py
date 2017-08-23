import numpy as np
import theano
from theano import tensor as T

theano.config.profile_memory = True
theano.config.profile = True


SLOPE = 3.1
INTERCEPT = -1.2


def residual_stats_theano(x, y):
    expected = SLOPE * x + INTERCEPT
    residuals = y - expected
    return residuals.mean(), residuals.std()


x_var = T.vector()
y_var = T.vector()

residual_stats = theano.function(
    inputs=[x_var, y_var],
    outputs=residual_stats_theano(x_var, y_var),
    allow_input_downcast=True,
    profile=True,
)


if __name__ == '__main__':
    x = np.linspace(-10, 10, 1000)
    y = SLOPE * x + INTERCEPT
    y += np.random.normal(loc=0.1, scale=0.5, size=x.shape)
    mn, std = residual_stats(x, y)
    print('Residual mean=', mn, ', std=', std)
