
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random

# Step 1: Generate sample data
np.random.seed(42)
random.seed(42)

# Sample values
domains = ['Data Science', 'Web Development', 'Cybersecurity', 'AI/ML', 'IoT', 'Cloud Computing']
branches = ['CSE', 'ECE', 'EEE', 'Mechanical', 'Civil']
statuses = ['Applied', 'Selected', 'Rejected']

n = 300  # number of records

data = {
    'Student ID': [f"MITS{1000+i}" for i in range(n)],
    'Name': [f"Student_{i}" for i in range(n)],
    'Year': np.random.choice([2, 3, 4], size=n),
    'Branch': np.random.choice(branches, size=n),
    'Internship Domain': np.random.choice(domains, size=n, p=[0.3, 0.25, 0.15, 0.1, 0.1, 0.1]),
    'Applied Date': pd.to_datetime(np.random.choice(pd.date_range("2025-01-01", "2025-06-30"), size=n)),
    'Status': np.random.choice(statuses, size=n, p=[0.6, 0.3, 0.1])
}

df = pd.DataFrame(data)

# Step 2: Most Popular Domains
plt.figure(figsize=(10,6))
popular_domains = df['Internship Domain'].value_counts()
sns.barplot(x=popular_domains.values, y=popular_domains.index, palette="viridis")
plt.title("Top Internship Domains by Applications")
plt.xlabel("Number of Applications")
plt.ylabel("Internship Domain")
plt.tight_layout()
plt.show()

# Step 3: Monthly Trends (Emerging Domains)
df['Month'] = df['Applied Date'].dt.to_period('M')
monthly_trends = df.groupby(['Month', 'Internship Domain']).size().unstack().fillna(0)
monthly_trends.plot(figsize=(12,6), marker='o')
plt.title("Monthly Trend of Applications by Domain")
plt.xlabel("Month")
plt.ylabel("Applications")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Step 4: Domain Popularity by Branch
plt.figure(figsize=(12,6))
sns.countplot(data=df, x='Branch', hue='Internship Domain')
plt.title("Internship Domain Preference by Branch")
plt.xlabel("Branch")
plt.ylabel("Count")
plt.legend(title='Domain', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Step 5: Status Distribution
status_counts = df['Status'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title("Application Status Distribution")
plt.axis('equal')
plt.show()
