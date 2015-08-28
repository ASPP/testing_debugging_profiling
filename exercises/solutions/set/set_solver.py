import numpy
import itertools

ndims = 4
nfeatures = 3

def random_deck():
    """Generate a deck of cards shuffled at random."""
    # initialize cards deck
    cards = numpy.array([card for card in itertools.product(range(nfeatures),
                                                            repeat=ndims)]).T
    n = cards.shape[1]
    # shuffle
    return cards[:, numpy.random.permutation(n)]


def random_cards(ncards=12):
    """Return a set of random cards.

    ncards -- number of cards to return
    """
    return random_deck()[:, :ncards]


# -----------------------------------------------------------------------------


def same(x):
    """Returns True if all elements are the same."""
    return numpy.all(x == x[0])

def different(x):
    """Returns True if all elements are different."""
    return len(numpy.unique(x)) == len(x)

def is_set(cards, indices):
    """Checks that the cards indexed by 'indices' form a valid set."""
    ndims = cards.shape[0]

    subset = cards[:, indices]
    for dim in range(ndims):
        # cards must be all the same or all different for all dimensions
        if not same(subset[dim, :]) and not different(subset[dim, :]):
            return False
    return True



def find_sets(cards):
    """Brute-force Sets solver.

    Returns a list of tuples; each tuple contains the indices of 3 cards that
    form a set.
    """
    n = cards.shape[1]
    sets = []

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if is_set(cards, (i, j, k)):
                    sets.append((i, j, k))
     
    return sets

def find_sets_fast(cards):
    """Brute-force Sets solver."""
    return [indices
            for indices in itertools.combinations(range(cards.shape[1]), 3)
            if is_set(cards, indices)]
