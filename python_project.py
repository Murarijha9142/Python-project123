import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:/Users/hp/Downloads/project_data.csv")

#Basic overview
print("Initial shape:", df.shape)
print("Missing values per column:\n", df.isnull().sum())

#Drop columns with too many missing values 
df.drop(['Cross Street', 'Mocodes'], axis=1)

#Convert date columns to datetime
df['Date Rptd'] = pd.to_datetime(df['Date Rptd'], errors='coerce')
df['DATE OCC'] = pd.to_datetime(df['DATE OCC'], errors='coerce')

#Handle missing values in critical columns
# Fill missing victim gender and descent with 'Unknown'
df['Vict Sex'] = df['Vict Sex'].fillna('Unknown')
df['Vict Descent'] = df['Vict Descent'].fillna('Unknown')
df['Premis Desc'] = df['Premis Desc'].fillna('Unknown')
df['Weapon Desc'] = df['Weapon Desc'].fillna('None')


df['Year'] = df['DATE OCC'].dt.year


print("Cleaned shape:", df.shape)
print("Columns now:\n", df.columns)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Load and clean the dataset
df = pd.read_csv(r"C:/Users/hp/Downloads/project_data.csv")
df.drop(['Cross Street', 'Mocodes'], axis=1, errors='ignore')
df['Date Rptd'] = pd.to_datetime(df['Date Rptd'], errors='coerce')
df['DATE OCC'] = pd.to_datetime(df['DATE OCC'], errors='coerce')
df['Vict Sex'] = df['Vict Sex'].fillna('Unknown')
df['Vict Descent'] = df['Vict Descent'].fillna('Unknown')
df['Premis Desc'] = df['Premis Desc'].fillna('Unknown')
df['Weapon Desc'] = df['Weapon Desc'].fillna('None')
df['Year'] = df['DATE OCC'].dt.year

# Visualization theme
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)
data = df.copy()


sns.boxplot(data=df[df['Vict Sex'].isin(['M', 'F'])], x='Vict Sex', y='Vict Age',
            hue='Vict Sex', palette='Set3', legend=False)
plt.title("Victim Age Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Age")
plt.tight_layout()
plt.show()

# Crimes per Year
crimes_per_year = df['Year'].value_counts().sort_index()
plt.plot(crimes_per_year.index, crimes_per_year.values, marker='o', color='green', linestyle='-')
plt.title("Total Crimes Per Year (Line Chart)")
plt.xlabel("Year")
plt.ylabel("Number of Crimes")
plt.grid(True)
plt.tight_layout()
plt.show()


#Horizontal Bar Chart - Top 10 Crime Types
top_crimes = df['Crm Cd Desc'].value_counts().head(10)

sns.barplot(x=top_crimes.values, y=top_crimes.index,
            hue=top_crimes.index, palette='viridis')

plt.title("Top 10 Most Frequent Crime Types (Bar Plot)")
plt.xlabel("Number of Cases")
plt.ylabel("Crime Type")
plt.tight_layout()
plt.show()


#Pie Chart - Crimes by Area (Top 8)
top_areas = data['AREA NAME'].value_counts().head(8)
plt.pie(top_areas.values, labels=top_areas.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title("Crime Distribution by Area (Pie Chart)")
plt.gca().set_aspect('equal')
plt.tight_layout()
plt.show()

#Stacked Bar Chart - Victim Age Group and Gender
bins = [0, 12, 18, 30, 45, 60, 100]
labels = ['Child', 'Teen', 'Young Adult', 'Adult', 'Middle Age', 'Senior']
data['Age Group'] = pd.cut(data['Vict Age'], bins=bins, labels=labels)

age_gender = data.groupby(['Age Group', 'Vict Sex'], observed=False).size().unstack(fill_value=0)


age_gender.plot(kind='bar', stacked=True, colormap='Set2')
plt.title("Victim Age Group by Gender (Stacked Bar)")
plt.xlabel("Age Group")
plt.ylabel("Number of Victims")
plt.legend(title='Gender')
plt.tight_layout()
plt.show()

#Donut Chart - Weapon Usage
weapon_data = data[data['Weapon Desc'] != 'None']
top_weapons = weapon_data['Weapon Desc'].value_counts().head(6)
colors = sns.color_palette('coolwarm', len(top_weapons))
plt.pie(top_weapons.values, labels=top_weapons.index, colors=colors, startangle=90, wedgeprops={'width': 0.4})
plt.title("Top Weapons Used in Crimes (Donut Chart)")
plt.gca().set_aspect('equal')
plt.tight_layout()
plt.show()


# Filter for female victims
female_crimes = df[df['Vict Sex'] == 'F']

# Count crimes by area
female_crimes_by_area = female_crimes['AREA NAME'].value_counts().head(6)

# Pie chart
plt.pie(female_crimes_by_area.values, labels=female_crimes_by_area.index,
        autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2'))
plt.title("Crimes Against Women by Area (Pie Chart)")
plt.axis('equal')  
plt.tight_layout()
plt.show()
