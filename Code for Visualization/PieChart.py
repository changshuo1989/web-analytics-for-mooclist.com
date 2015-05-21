# -*- coding: utf-8 -*-

"""
Demo of a basic pie chart plus a few additional features.
"""

import matplotlib.pyplot as plt


# The slices will be ordered and plotted counter-clockwise.
labels = 'France', 'England', 'Germany', 'USA'

#size of each slice. These don;t have to sum up to 100. Python normalizes values automatically.
sizes = [100 ,100, 405, 120]

#color of each slice
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

#The explode value determines if a slice should be sticking out and to what extent.
explode = (0, 0.5, 0, 0)

#make the chart. Autopct is used to also add the percentage on top of the slice.
#You can add/remove the shadow with the shadow feature.
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%.1f%%', shadow=True)
        
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

plt.show()
