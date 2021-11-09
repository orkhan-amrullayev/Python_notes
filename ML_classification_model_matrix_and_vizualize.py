def run_model2(model, X_train, y_train, X_test, y_test, verbose=True):
    t0=time.time()          #calculates the time model run
    
    if verbose == False:
        model.fit(X_train,y_train.ravel(), verbose=0)
    else:
        model.fit(X_train,y_train.ravel())

    y_score = model.predict_proba(X_test)    #takes probabilities

    accuracy = accuracy_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_score[:, 1]) 
    time_taken = time.time()-t0
    print("Accuracy = {}".format(accuracy))
    print("ROC Area under Curve = {}".format(roc_auc))
    print("Time taken = {}".format(time_taken))
    print(classification_report(y_test,y_pred,digits=5))
    plot_confusion_matrix(model, X_test, y_test,cmap=plt.cm.pink, normalize = 'all')
    plot_roc_curve(model, X_test, y_test)                     
    
    return model, accuracy, roc_auc, time_taken


### how to run a model with this custom function

from sklearn.ensemble import RandomForestClassifier

params_rf = best_model_rgs_rf   #taken from results of Randomized/Grid Search CV of 'best_model_rgs_rf = model_rgs_rf.best_params_'

model_rf = RandomForestClassifier(**params_rf)
model_rf, accuracy_rf, roc_auc_rf, tt_rf = run_model2(model_rf, X_train, y_train, X_test, y_test)
