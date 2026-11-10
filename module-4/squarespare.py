# Visualize equimaterial zones on a rolled cylinder

import numpy as np
import matplotlib.pyplot as plt

def product_remaining(r, R_new=3):
    """Fraction of product remaining by visible roll radius.

    Parameters
    ----------
    r : float, 1 <= r
        Visible radius of roll in units of r0, the cardboard cylinder radius.
    R_new : scalar, optional, default: 3
        Radius of roll when new, in units of r0.
    
    Returns
    -------
    Current remaining length as fraction of original length of new roll.
    """
    return (r ** 2 - 1) / (R_new ** 2 - 1) ### REPLACE WITH CORRECT FORMULA

def product_visible(el_frac, R_new=3):
    """Visible roll radius by fraction of remaining product.

    Parameters
    ----------
    el_frac : float, 0 <= el_frac <= 1
        Current remaining length as fraction of original length of new roll.
    R_new : scalar, optional, default: 3
        Radius of roll when new, in units of r0, the cardboard cylinder radius.

    Returns
    -------
    Current visible radius of roll, in units of r0, the cardboard cylinder
    radius.
    """
    return np.sqrt(el_frac * (R_new ** 2 - 1) + 1) ### REPLACE WITH CORRECT FORMULA

def visualize_danger(n, R_new=3, saveas=''):
    """Use n line segments of equal product to visualize paradox of the roll.

    Parameters
    ----------
    n : int scalar
        Number of line segments to display.
    R_new : scalar, optional, default: 3
        Radius of roll when new, in units of r0, the cardboard cylinder radius.
    saveas : str, optional, default: empty
        If not empty save figure to file 

    Returns
    -------
    None
    """

    # Start with a new figure window
    plt.close('all') # this helps get rid of old figures you forgot to close
    fh = plt.figure(figsize=(8,6)) # my favorite figure size

    ### YOUR CODE HERE ###

    # Do the core plotting commands here
    ## use the functions defined above to calculate the line segments to plot
    ax = fh.add_subplot(1, 1, 1)
    fractions = np.linspace(0, 1, n + 1)        # n equal slices of paper -> n+1 boundaries
    radii = product_visible(fractions, R_new)   # boundary radii, from r0 = 1 out to R_new

    ax.add_patch(plt.Circle((0, 0), 1, color='gray'))   # cardboard core, radius r0
    for r in radii:
        ax.add_patch(plt.Circle((0, 0), r, fill=False,
                                edgecolor='black', linewidth=1.5))

    # Set axes properties here for a better view
    ## things like axis limits and tick marks

    # Stylize and annotate
    ## things like axes labels, font sizes, or any other finishing touches

    ######################

    # Finally, show on screen and/or save to file
    if saveas:
        plt.savefig(saveas)
    plt.close()   # figures in this course are files: look at the saved PNG (plt.show() would pop a window instead)

if __name__ == '__main__':
    visualize_danger(5, saveas='roll_paradox_5.png')
    visualize_danger(3, saveas='roll_paradox_3.png')
    visualize_danger(9, saveas='roll_paradox_9.png')