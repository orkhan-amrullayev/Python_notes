#adding a few extra parameters to the dataframe and getting rid of the date-month-year format
#this step is important because the time data cannot be preprocessed in the abovedescribed format

df_new["saleYear"] = df_new.saledate.dt.year
df_new["saleMonth"] = df_new.saledate.dt.month
df_new["saleDay"] = df_new.saledate.dt.day
df_new["saleDayOfYear"] = df_new.saledate.dt.dayofyear
df_new.drop("saledate",axis=1, inplace=True)
