import matplotlib.pyplot as plt
import squarify    # pip install squarify (algorithm for treemap)
 
import pandas as pd



df = pd.DataFrame({'nb_people':[8,3,4,2], 'group':["group A", "group B", "group C", "group D"] })
# alpha value specifies the opacity, the higher the value the brighter the colour of the square
squarify.plot(sizes=df['nb_people'], label=df['group'], alpha=.6 ) 
plt.axis('off')
plt.show()
