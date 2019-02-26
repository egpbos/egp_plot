# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


def subplots(total, wrap=None, **kwargs):
    """
    Make `total` subplots, wrapped horizontally by `wrap` columns.
    `kwargs` passed to `plt.subplots`.
    """
    if wrap is not None:
        cols = min(total, wrap)
        rows = 1 + (total - 1)//wrap
    else:
        cols = total
        rows = 1
    fig, ax = plt.subplots(rows, cols, **kwargs)
    return fig, ax
