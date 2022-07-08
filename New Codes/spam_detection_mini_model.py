from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
import pandas as pd
import pickle

dataset = pd.read_csv(r'E:\My Codes\New Codes\spam.csv',encoding='latin-1')
z = dataset['v2']
y = dataset["v1"]
z_train, z_test,y_train, y_test = train_test_split(z,y,test_size = 0.2)

cv = CountVectorizer()
features = cv.fit_transform(z_train)

model = svm.SVC()
model.fit(features,y_train)

features_test = cv.transform(z_test)
print(model.score(features_test,y_test))

pickle.dump(model, open('spam_detection_model.jac', 'wb'))
pickle.dump(cv,open("spam_vectorizer.jac",'wb'))