import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel
file_path = '/Users/liujia/Desktop/data/arlo_camera_pro4/dns_query_counts.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Calculate the standard deviation of the number of each DNS query and sort by standard deviation in descending order
df['std_dev'] = df.iloc[:, 1:].std(axis=1)
sorted_df = df.sort_values(by='std_dev', ascending=False)

# Select the top 5 DNS with the largest standard deviation
top_dns = sorted_df.head(5)

# Draw a line chart
weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
for index, row in top_dns.iterrows():
    plt.plot(weeks, row[1:5], label=row[0])

plt.legend(loc='upper right')  # Top right corner of the general pattern
plt.title('arlo_camera_pro4: Top 5 DNS Query Counts Over 4 Weeks')
plt.xlabel('Weeks')
plt.ylabel('Query Counts')
plt.grid(True)
plt.tight_layout()
plt.show()
