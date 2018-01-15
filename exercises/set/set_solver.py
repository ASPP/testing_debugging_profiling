import numpy

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


def is_set(cards, indices):
    """Checks that the cards indexed by 'indices' form a valid set."""
    return False


def find_sets(cards):
    """Brute-force Sets solver.

    Returns a list of tuples; each tuple contains the indices of 3 cards that
    form a set.
    """
    return []
