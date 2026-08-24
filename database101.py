# Data visulization
# this is the process of representing data in a graphical or pictorial format to help understand trends,
# patterns, and insights from the data. it allows users to easily interpret complex data saets and make informed 
# decisions based on the visual representation of the data. common types of data visualization include bar charts, line grahphs,
# scatter plots, pie charts, and heat maps. 
# data visualisation is widely used in various fields such as business, finance, healthcare, and social sciences to communicate
#  information effectively and facilitate data-driven decision-making.

imprt matplotlib.pyplot as plt


months = ['January', 'February', 'March', 'April', 'May', 'June']
sales = [10000, 
         15000, 
         12000, 
         18000, 
         20000, 
         25000]
plt.plot(months, sales)
plt.title("month sales")
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()
