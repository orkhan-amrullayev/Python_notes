#making a grid of hyperparameters for RandomizedSearchCV

grid = {"n_estimators": np.arange(10,100,10),
          "max_depth": [None,3,5,10],
          "min_samples_split": np.arange(2,20,2),
          "min_samples_leaf": np.arange(1,20,2),
          "max_features": [0.5,1,"sqrt","auto"],
          "max_samples": [10000]}

# creating a model of the RandomizedSearchCV by passing in the grid, the number of iterations(n_iter) and number of folds(cv)

gs_model = RandomizedSearchCV(RandomForestRegressor(n_jobs=-1,
                                                   random_state=42),
                             param_distributions=grid,
                             n_iter = 10,
                             cv=5,
                             verbose=True)
gs_model.fit(x_train,y_train)
