import matplotlib.pyplot as plt
import numpy as np


plt.title("Movies years and revenue")
plt.xlabel('Years')
plt.ylabel('Revenue in (million $)')


## oscar movies 


oscar_movies = [
    "The Dark Knight", 
    "The Hurt Locker",  
    "The King's Speech", 
    "The Artist",     
    "Argo"
]
years = [2008, 2009, 2010, 2011, 2012]

oscar_revenue = [1005, 170, 427, 133, 232]

# creating x positions
x = []

for i in range(len(years)):
    x.append(i)

width = 0.4    # bydefault width=0.8    x--> positions 

x=np.array(x)
# Oscar movies bars
plt.bar(x-width/2,
        oscar_revenue,
        label="Oscar movies",
        color="blue",
        width=width)


# text on bars
for i in range(len(years)):
    plt.text(x[i]-width/2,
             oscar_revenue[i]+10,
             oscar_movies[i],
             ha="center")



# non oscar data
non_oscar_movies = [
    "Slumdog Millionaire",
    "Avatar",
    "Inception",
    "Hugo",
    "Lincoln"
]

non_oscar_revenue = [378, 2788, 829, 185, 275]

# non-oscar bars
plt.bar(x+width/2,
        non_oscar_revenue,
        label="Non-Oscar movies",
        color="pink",
        width=width)

# text on bars
for i in range(len(years)):
    plt.text(x[i]+width/2,
             non_oscar_revenue[i]+10,
             non_oscar_movies[i],
             ha="center")
    

plt.legend()
plt.ylim(0, max(max(oscar_revenue), max(non_oscar_revenue)) + 300)

plt.xticks(x, years)
plt.tight_layout
plt.show()