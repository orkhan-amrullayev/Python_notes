for label, content in df_new.items():
    
    #in the new dataset, search for string data type cintents and convert them to category type
    
    if pd.api.types.is_string_dtype(content):
        df_new[label] = content.astype("category").cat.as_ordered()
