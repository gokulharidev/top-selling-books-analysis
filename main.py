import pandas as pd
book=pd.read_csv('book.csv')
book=book.sort_values(by='Year').reset_index(drop=True)

import matplotlib.pyplot as plt
import numpy as np
plt.bar(book['Name'],book['Reviews'])
plt.xticks(fontsize=2)
plt.xlabel("name of the book")
plt.ylabel("Reviews")
plt.title("highest reviews of book")
plt.show()

plt.bar(book['Name'],book['User Rating'])
plt.xticks(fontsize=2)
plt.xlabel("name of the book")
plt.ylabel("Rating")
plt.title("highest rating of book")
plt.show()

highra=book[book['User Rating']>4.8]

fig, ax = plt.subplots()
ax.axis('tight') 
ax.axis('on')
table = ax.table(cellText=highra.values, colLabels=highra.columns, cellLoc='center', loc='center',fontsize=10)
table.auto_set_font_size(False) 
table.set_fontsize(10)
plt.title("from 2008 to 2019, rating > 4.8")
plt.show()
#highly rated books over years includes repeated books 

fic=book['Genre'].value_counts()
plt.pie(fic,labels=fic.index,autopct='%1.1f%%')
plt.title("from 2008 to 2019, fiction and non-fiction percent rated by people")
plt.show()

ficyear=book[['Genre','Year']]
# Group by Year and Genre
ficyear = ficyear.groupby(['Year', 'Genre']).size().unstack(fill_value=0)

# Plotting
fig, ax = plt.subplots()
bar_width = 0.35
index = np.arange(len(ficyear.index))

# Create bars
bar1 = ax.bar(index, ficyear['Fiction'], bar_width, label='Fiction')
bar2 = ax.bar(index + bar_width, ficyear['Non Fiction'], bar_width, label='Non Fiction')

# Add labels, title, and legend
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.set_title('Count of Fiction and Non-Fiction by Year')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(ficyear.index)
ax.legend()
plt.show()
