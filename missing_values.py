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

        
#####
#####








