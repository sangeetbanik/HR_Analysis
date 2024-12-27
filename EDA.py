## Calculating the Attrition rate in the company
# Attrition Rate

attrition = df['Attrition'].value_counts(normalize= True) 
print(attrition )

sns.barplot(x= attrition.index , y= attrition.values , hue= attrition.index )
plt.title("Attrition Rate")
plt.xlabel("Attrition")
plt.ylabel("Count")

ax = plt.gca()

for p in ax.patches:
    ax.annotate(f'{p.get_height() * 100:.2f}%', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='bottom')

plt.show()

#### Employee Demographics

fig , ax = plt.subplots(1,4, figsize=(20,5))

# PLOT : Distribution of Employees by Age

sns.histplot(data = df, x = 'Age', kde= True, ax=ax[0])
ax[0].set_title('Distribution of Employees by Age')
ax[0].set_xlabel('Age')
ax[0].set_ylabel('Count')

# PLOT : Distibution of Employees by Gender
sns.countplot(data = df, x = 'Gender', hue= 'Gender', ax=ax[1])
ax[1].set_title('Distribution of Employees by Gender')
ax[1].set_xlabel('Gender')
ax[1].set_ylabel('Count')

for p in ax[1].patches:
    height = p.get_height()
    ax[1].text(p.get_x() + p.get_width()/2.0, height+0.1, '{:1.0f}'.format(height) , ha = "center")

# PLOT : Distribution of Employees by Department
sns.countplot(data = df, x = 'Department', hue = 'Department', ax=ax[2])
ax[2].set_title('Distribution of Employees by Department')
ax[2].set_xlabel('Department')
ax[2].set_ylabel('Count')
ax[2].tick_params( axis = 'x' , rotation = 45 )
for p in ax[2].patches:
    height = p.get_height()
    ax[2].text(p.get_x() + p.get_width()/2.0, height+0.1, '{:1.0f}'.format(height) , ha = "center")

# PLOT : Distribution of employees by Education Field
sns.countplot(data=df, x='EducationField', hue='EducationField',ax=ax[3])
ax[3].set_title('Distribution of Employees by Education Field')
ax[3].set_xlabel('Education Field')
ax[3].set_ylabel('Count')
ax[3].tick_params( axis = 'x' , rotation = 45 )
for p in ax[3].patches:
    ax[3].annotate(p.get_height(),
                   (p.get_x()+p.get_width()/2.0,p.get_height()),
                   ha='center',va='bottom')

plt.show()

## Sub-Table for Positive attrition
df_attrition = df[df['Attrition'] == 'Yes']
df_attrition.head()

## Function to calculate Attrition rate
def cal_attrition_rate(df, column ):
    attrition_counts = df.groupby([column, 'Attrition']).size().unstack(fill_value=0)
    attrition_rate = attrition_counts['Yes'] / attrition_counts.sum(axis=1) * 100
    attrition_rate_df = attrition_rate.reset_index()
    attrition_rate_df.columns = [column, 'AttritionRate']
    return attrition_rate_df

## 
fig , ax = plt.subplots(1,2, figsize=(15,5))

# PLOT : KDE plot of Age with Attrition hue

sns.kdeplot(data = df_attrition, x = 'Age', fill= True, ax=ax[0])
ax[0].set_title('Distribution of Attrition rate by Age')
ax[0].set_xlabel('Age')
ax[0].set_ylabel('Count')

# PLOT : Barplot of Gender with Attrition hue

attrition_rate_df = cal_attrition_rate(df, 'Gender')
print(attrition_rate_df)
sns.barplot(data= attrition_rate_df, x= 'Gender', y='AttritionRate', hue = 'Gender', ax = ax[1])
ax[1].set_title('Attrition Rate by Gender')
ax[1].set_xlabel('Gender')
ax[1].set_ylabel('Attrition rate %')

for p in ax[1].patches:
    ax[1].annotate(f'{p.get_height():.2f}%' , 
                   (p.get_x() + p.get_width()/2.0 , p.get_height() ),
                   ha = 'center' , va= 'bottom')
   


plt.show()
