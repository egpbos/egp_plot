# -*- coding: utf-8 -*-

import matplotlib as mpl
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
    
    # disable superfluous subplots
    for ix in range(-1, -1 - (cols * rows - total), -1):
        ax.flatten()[ix].axis('off')

    return fig, ax


def draw_arrow_between_axes(fig, ax0, ax1, ax0x, ax0y, ax1x, ax1y,
                            fc="g", connectionstyle="arc3,rad=0.2",
                            arrowstyle='simple', alpha=0.3,
                            mutation_scale=40.):
    """
    The arrow starts in ax0 at ax0x, ax0y and ends in ax1.
    """
    # Create the arrow
    # 1. Get transformation operators for axis and figure
    ax0tr = ax0.transData # Axis 0 -> Display
    ax1tr = ax1.transData # Axis 1 -> Display
    figtr = fig.transFigure.inverted() # Display -> Figure
    # 2. Transform arrow start point from axis 0 to figure coordinates
    ptB = figtr.transform(ax0tr.transform((ax0x, ax0y)))
    # 3. Transform arrow end point from axis 1 to figure coordinates
    ptE = figtr.transform(ax1tr.transform((ax1x, ax1y)))
    # 4. Create the patch
    arrow = mpl.patches.FancyArrowPatch(
        ptB, ptE, transform=fig.transFigure,  # Place arrow in figure coord system
        fc=fc, connectionstyle=connectionstyle, arrowstyle=arrowstyle, alpha=alpha,
        mutation_scale=mutation_scale
    )
    # 5. Add patch to list of objects to draw onto the figure
    fig.patches.append(arrow)
