import pickle
print("Spam Testing!")
print("Loading Trained Model..")
loaded_model = pickle.load(open(r'E:\My Codes\New Codes\spam_detection_model.jac', 'rb'))
loaded_cv=pickle.load(open(r'E:\My Codes\New Codes\spam_vectorizer.jac','rb'))

test_tube=[]
message=input("Please Enter Message:")
test_tube.append(message)
test_tube_launch=loaded_cv.transform(test_tube)
print(f"The message that you have entered is {loaded_model.predict(test_tube_launch)[0]}")