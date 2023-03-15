import numpy as np
import matplotlib.pyplot as plt


def trapezoid(x, center=0, slope=1, width=1, height=1, offset=0):
    """
    For given array x, returns a (symmetric) trapezoid with plateau at y=h (or -h if 
    slope is negative), centered at center value of "x".
    Note: Negative widths and heights just converted to 0

    Parameters
    ----------
    x : array_like
        array of x values at which the trapezoid should be evaluated
    center : float
        x coordinate of the center of the (symmetric) trapezoid
    slope : float
        slope of the sides of the trapezoid
    width : float
        width of the plateau of the trapezoid
    height : float
        (positive) vertical distance between the base and plateau of the trapezoid
    offset : array_like
        vertical shift (either single value or the same shape as x) to add to y before returning

    Returns
    -------
    y : array_like
        y value(s) of trapezoid with above parameters, evaluated at x

    """
    
    # ---------- input checking ----------
    if width < 0: width = 0
    if height < 0: height = 0

    x = np.asarray(x)

    slope_negative = slope < 0
    slope = np.abs(slope)  #  Do all calculations with positive slope, invert at end if necessary

    # ---------- Calculation ----------
    y = np.zeros_like(x)
    mask_left = x - center < -width/2.0
    mask_right = x - center > width/2.0

    y[mask_left] = slope*(x[mask_left] - center + width/2.0)
    y[mask_right] = -slope*(x[mask_right] - center - width/2.0)


    y += height     # Shift plateau up to y=h
    y[y < 0] = 0    # cut off below zero (so that trapezoid flattens off at "offset")

    if slope_negative: y = -y          # invert non-plateau

    return y + offset


# ---------- example usage ----------
import matplotlib.pyplot as plt
plt.style.use("seaborn-colorblind")

x = np.linspace(-5,5,1000)

for i in range(1,4):
    plt.plot(x,trapezoid(x, center=0, slope=1, width=i, height=i, offset = 0), label=f"width = height = {i}\nslope=1")

plt.plot(x,trapezoid(x, center=0, slope=-1, width=2.5, height=1, offset = 0), label=f"width = height = 1.5,\nslope=-1")
plt.ylim((-2.5,3.5))
plt.legend(frameon=False, loc='lower center', ncol=2)
plt.tight_layout()
plt.savefig("example.png")