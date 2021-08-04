import numpy as np
from logistic import iterate_f
from matplotlib import pyplot as plt


def plot_trajectory(n, r, x0, fname="single_trajectory.png"):
    l = iterate_f(n, x0, r)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(list(range(n)), l)
    fig.suptitle('Logistic Function')

    fig.savefig(fname)
    return fig, ax

def plot_bifurcation(start, end, step, fname="bifurcation.png"):
    r_range=np.arange(start, end, step)
    it = 100000
    last = 200
    x=[]
    y=[]
    #rrannge
    for r in r_range:
        l = iterate_f(it, 0.1, r)
        ll = l[len(l)-last::].copy()
        lll = np.unique(ll)
        y.extend(lll)
        x.extend(np.ones(len(lll))*r)

    fig, ax = plt.subplots(figsize=(20,10))
    ax.scatter(x,y, s=0.1)
    ax.set_xlabel("r")
    fig.savefig(fname)
    return fig, ax


if __name__=="__main__":
    n_conv = 15
    l1 = iterate_f(n_conv, 0.1, 1.5)
    l2 = iterate_f(n_conv, 0.3, 1.5)
    l3 = iterate_f(n_conv, 0.5, 1.5)

    n_div = 8
    r2 = 5
    l4 = iterate_f(n_div, 0.001, r2)
    l5 = iterate_f(n_div, 0.0011, r2)
    l6 = iterate_f(n_div, 0.00111, r2)
    #print(l4)

    fig, ax = plt.subplots(1,2, figsize=(10,5))
    ax[0].plot(list(range(n_conv)), l1, label=str(0.1))
    ax[0].plot(list(range(n_conv)), l2, label=str(0.3))
    ax[0].plot(list(range(n_conv)), l3, label=str(0.5))
    ax[0].legend()
    ax[0].set_title("r = 1.5")

    ax[1].plot(list(range(n_div)), l4, label=str(0.001))
    ax[1].plot(list(range(n_div)), l5, label=str(0.0011))
    ax[1].plot(list(range(n_div)), l6, label=str(0.00111))
    ax[1].legend()
    ax[1].set_title("r = 5")

    fig.suptitle('Logistic Function')
    fig.savefig("log_fun.png")


    n_ch = 15
    r3 = 3.8
    l7 = iterate_f(n_ch, 0.1, r3)
    l8 = iterate_f(n_ch, 0.3, r3)
    l9 = iterate_f(n_ch, 0.5, r3)

    fig, ax = plt.subplots(1,3, figsize=(15,5))
    ax[0].plot(list(range(n_conv)), l1, label=str(0.1))
    ax[0].plot(list(range(n_conv)), l2, label=str(0.3))
    ax[0].plot(list(range(n_conv)), l3, label=str(0.5))
    ax[0].legend()
    ax[0].set_title("r = 1.5")

    ax[1].plot(list(range(n_ch)), l7, label=str(0.1))
    ax[1].plot(list(range(n_ch)), l8, label=str(0.3))
    ax[1].plot(list(range(n_ch)), l9, label=str(0.5))
    ax[1].legend()
    ax[1].set_title("r = 3.8")


    ax[2].plot(list(range(n_div)), l4, label=str(0.001))
    ax[2].plot(list(range(n_div)), l5, label=str(0.0011))
    ax[2].plot(list(range(n_div)), l6, label=str(0.00111))
    ax[2].legend()
    ax[2].set_title("r = 5")

    fig.suptitle('Logistic Function')
    fig.savefig("log_fun2.png")

    plot_bifurcation(1, 4, 0.01, fname="bifurcation.png")
    plot_bifurcation(3, 4, 0.003, fname="bifurcation_zoom.png")
    plot_trajectory(300, 3.5, 0.1, fname="single_trajectory.png")