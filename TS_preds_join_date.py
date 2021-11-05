# Time Series
# list of test y into DataFrame and joining it with date from its original (the one with all Xs) dataframe

df_preds = pd.DataFrame()
df_preds["date"] = df_test_raw683["date"]
df_preds["y"] = test_preds
df_preds
