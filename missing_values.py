#####
#####


# checking the missing values of dataset

df_new.isna().sum()


#####
#####


# filling missing data with median of the column 
# you can change it to mean as well

for label, value in df_new.items():
    
    #in the dataset if any numeric data type value is null , fill it with the median of the column
    
    if pd.api.types.is_numeric_dtype(value):
        if pd.isnull(value).sum():
            df_new[label] = content.fillna(value.median())

            
#####
#####


#checking for leftover missing values
#leftovers are categoricals, because they do not have any median to calculate, so they remained unchanged.
df_new.isna().sum()



#####
#####

# creating a list of those labels which have missing values
# missing values

missing = []
for label in df_new:
    if df_new[label].isna().sum():
        missing.append(label)
        
missing



#####
#####
df.isna().sum()

#or

df.isnull().sum()

# creating a list of columns with non numeric data type content

not_numeric = []
for label,value in df_new.items():
    if not pd.api.types.is_numeric_dtype(value):
        not_numeric.append(label)
        
not_numeric


#####
#####


# By default, the categorical code for a missing values is assigned -1 in Pandas. We can change this by adding 1 to the categorical code of missing values

for label,value in df_new.items():
    if not pd.api.types.is_numeric_dtype(value):
        
        df_new[label] = pd.Categorical(value).codes+1

        
#####################
#####################

## Percentages of NA values.
nan_columns = dict()
temp = df.isna().sum()
for index, column in enumerate(df.columns):
    if temp[index] != 0:
        nan_columns[column] = (temp[index], f"{round((temp[index]/df.shape[0])*100, 2)}%") 
print(nan_columns)

## take the names of columns from the input of the code just above and pass it to XXX/YYY so that you can fill NaN values with mode and median
df['XXX'].fillna(df['XXX'].mode()[0], inplace=True)
df['YYY'].fillna(df['YYY'].median(), inplace=True)



### number of duplicated rows in dataframe
print('The number of duplicates is {}\n'.format(df.duplicated().sum()))
print('The total numer of rows is {}\n'.format(df.shape[0]))
print(f"Ratio is {round((df.duplicated().sum()/df.shape[0])*100, 2)}%")
