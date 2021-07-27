import numpy as np
from logistic import iterate_f
from matplotlib import pyplot as plt


n_conv = 15
l1 = iterate_f(n_conv, 0.1, 1.5)
l2 = iterate_f(n_conv, 0.3, 1.5)
l3 = iterate_f(n_conv, 0.5, 1.5)


n_div = 15
l4 = iterate_f(n_div, 0.1, 4)
l5 = iterate_f(n_div, 0.11, 4)
l6 = iterate_f(n_div, 0.111, 4)


fig, ax = plt.subplots(1,2, figsize=(10,5))
ax[0].plot(list(range(n_conv)), l1, label=str(0.1))
ax[0].plot(list(range(n_conv)), l2, label=str(0.3))
ax[0].plot(list(range(n_conv)), l3, label=str(0.5))
ax[0].legend()
ax[0].set_title("r = 1.5")

ax[1].plot(list(range(n_div)), l4, label=str(0.1))
ax[1].plot(list(range(n_div)), l5, label=str(0.11))
ax[1].plot(list(range(n_div)), l6, label=str(0.111))
ax[1].legend()
ax[1].set_title("r = 4")

fig.suptitle('Logistic Function')

fig.savefig("log_fun.png")