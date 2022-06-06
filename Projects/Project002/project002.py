# This is just the code in the jupyter notebook

# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import joblib
# from sklearn import tree
#
# # import the data from the csv
# music_data = pd.read_csv("music.csv")
#
# # we must split the data into two data sets
# # age and gender; input set
# # genre; output set
# X = music_data.drop(columns=["genre"])  # by convention, we use capital X
# # for naming this set
# # "drops" the "genre" column,
# # leaving the other two
#
# y = music_data["genre"]  # by convention, we use y
# # for naming this set
# # creates a new set with the
# # "genre" column
#
# # split the data into data for training (80%) and testing (20%), hence 0.2 size
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#
# # modeling / training
# model = DecisionTreeClassifier()
# model.fit(X_train.values, y_train.values)  # takes the input set and the output set
#
# tree.export_graphviz(model, out_file="music-recommender.dot",
#                      feature_names=["age", "gender"],
#                      class_names=sorted(y.unique()),
#                      label="all", rounded=True,
#                      filled=True)
#
# # # saving the model for reloading
# # joblib.dump(model, "music-recommender.joblib")
#
# # # loading the saved model
# # model = joblib.load("music-recommender.joblib")
#
# # # predictions after training
# # predictions = model.predict(X_test.values)
#
# # # measuring the accuracy of the predictions
# # score = accuracy_score(y_test.values, predictions) # returns a value from 0 to 1
# # score
#
# # If you get an error about feature names, just add .values to it
