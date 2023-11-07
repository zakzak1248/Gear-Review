import json
from itertools import groupby
ratings = []
with open("scrapy/spiders/bountique.jsonl", "rb") as file:
    data = file.read().decode('utf-8')
    json_data = [json.loads(line) for line in data.splitlines()]
    ratings = list(map(lambda i: i['rating'], json_data))
# ratings = list(filter(lambda i: i is not None, ratings))
grouped_items = {key: list(group) for key, group in groupby(sorted(json_data, key=lambda i: i['brand']),
                                                            key=lambda i: i['brand'])}
def averagee(i):
    tmp = list(filter(lambda i: i != '' and i != None, map(lambda i: i['rating'], grouped_items[i])))
    if(len(tmp)!=0 and len(tmp) > 1): return  (i, sum(tmp)/len(tmp))
    else: return None

rating_by_group = list(filter(lambda i: i != None, map(averagee, grouped_items)))
(x,y) = zip(*rating_by_group)

import matplotlib.pyplot as plt


# Create a bar chart
plt.figure(figsize=(15,9))  # Set the figure size (optional)
plt.plot(x, y)

# Set labels and title
plt.xlabel('Ratings')
plt.xticks(rotation=75)
plt.tight_layout(rect=[0, .0, 1, .95])


plt.ylabel('Frequency')
plt.title('Distribution of Ratings of softsynths on pluginboutique on average')


# Show the bar chart
plt.show()
