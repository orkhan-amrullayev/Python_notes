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
