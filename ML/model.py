import pandas as pd
# importing the dataset
dataset = pd.read_csv('../dataset/dataset_savioroftheheart.csv')
X = dataset.iloc[:, :-2].values
y = dataset.iloc[:, 9].values

# Categorical data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_C = LabelEncoder()
X[:, 0] = labelencoder_C.fit_transform(X[:, 0])
X[:, 3] = labelencoder_C.fit_transform(X[:, 3])
X[:, 4] = labelencoder_C.fit_transform(X[:, 4])
X[:, 5] = labelencoder_C.fit_transform(X[:, 5])
onehotencoder = OneHotEncoder()
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the dummy variable trap
X_adum = X[:, [1, 3, 5, 7, 8, 9, 10, 11]]

# splitting the data set into training set and testing set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_adum, y, test_size=0.2, random_state=0)

# fitting random forest regression to the training set
from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=100, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

# Few Evaluation
from sklearn.metrics import r2_score, mean_squared_error
print("R2 cofficient is {:.4f}".format(regressor.score(X_test,y_test)))

# save the model to disk
import pickle

filename = 'finalized_model.sav'
pickle.dump(regressor, open(filename, 'wb'))