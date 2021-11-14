import pandas as pd
import sklearn, sklearn.svm
import d6tflow
import luigi

# define workflow
class TaskGetData(d6tflow.tasks.TaskPqPandas):  # save dataframe as parquet

    def run(self):
        data = download_data()
        data = clean_data(data)
        self.save(data) # quickly save dataframe

class TaskPreprocess(d6tflow.tasks.TaskCachePandas):  # save data in memory
    do_preprocess = luigi.BoolParameter(default=True) # parameter for preprocessing yes/no

    def requires(self):
        return TaskGetData() # define dependency

    def run(self):
        df_train = self.input().load() # quickly load required data
        if self.do_preprocess:
            df_train = preprocess(df_train)
        self.save(df_train)

class TaskTrain(d6tflow.tasks.TaskPickle): # save output as pickle
    do_preprocess = luigi.BoolParameter(default=True)

    def requires(self):
        return TaskPreprocess(do_preprocess=self.do_preprocess)

    def run(self):
        df_train = self.input().load()
        model = sklearn.svm.SVC()
        model.fit(df_train.iloc[:,:-1], df_train['y'])
        self.save(model)

# Check task dependencies and their execution status
d6tflow.preview(TaskTrain())

'''
└─--[TaskTrain-{'do_preprocess': 'True'} (PENDING)]
   └─--[TaskPreprocess-{'do_preprocess': 'True'} (PENDING)]
      └─--[TaskGetData-{} (PENDING)]
'''

# Execute the model training task including dependencies
d6tflow.run(TaskTrain())

'''
===== Luigi Execution Summary =====

Scheduled 3 tasks of which:
* 3 ran successfully:
    - 1 TaskGetData()
    - 1 TaskPreprocess(do_preprocess=True)
    - 1 TaskTrain(do_preprocess=True)
'''

# Load task output to pandas dataframe and model object for model evaluation
model = TaskTrain().output().load()
df_train = TaskPreprocess().output().load()
print(sklearn.metrics.accuracy_score(df_train['y'],model.predict(df_train.iloc[:,:-1])))
# 0.9733333333333334
