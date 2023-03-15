import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

#cmap = mpl.cm.get_cmap('Greys')
#colors = cmap(np.linspace(0.2,0.8,10))
#mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=colors) 

linewidth = 0.2

# Generate the x and y data
x = np.linspace(0,1,100)
y = np.flip(x)


fig, ax = plt.subplots(dpi=200)

# Create the plot
for i in range(len(x)):
    plt.plot([x[i], 0], [0, y[i]], lw=linewidth)
    plt.plot([x[i], 0], [0, -y[i]], lw=linewidth)
    plt.plot([-x[i], 0], [0, y[i]], lw=linewidth)
    plt.plot([-x[i], 0], [0, -y[i]], lw=linewidth)

ax.set_aspect("equal")
plt.xticks([])
plt.yticks([])