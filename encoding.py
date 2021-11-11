## ENCODING


#######################################################################
##### OneHotEndcoding

oneHot = pd.get_dummies(X[nominal_columns])
X = pd.concat([X, oneHot], axis=1)
X = X.drop(nominal_columns, axis=1)
X.head()


#######################################################################
####  Custom map encoding

# defining nominal columns manually

# ordinal column
ordinal_column1_map = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
}

# binary column
binary_column1_map = {
    'N': 0,
    'Y': 1,
}

# maping the custom encoding

X['ordinal_column'] = X.loan_grade.map(ordinal_column1_map)
X.head()

X['binary_column1_map'] = X.binary_column1_map.map(binary_column1_map)
X.head()

#########################################################
