# if a string is in the value of a column, find their index numbers

len([n for n, x in enumerate(dataset['Date'].tolist()) if "Reviewed in" in x])


# find those rows

badRows = [n for n, x in enumerate(dataset['Date'].tolist()) if "Reviewed in" not in x]
badRows


# have a look at those rows

for i in badRows:
  print(dataset.iloc[i])
  
  
# drop those rows

dataset.drop(dataset.index[badRows],inplace=True)
