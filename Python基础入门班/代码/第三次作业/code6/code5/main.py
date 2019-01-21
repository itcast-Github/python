from sklearn import svm, datasets
import json

with open('x_train.txt', 'r') as file_x_train:
	X_train = json.load(file_x_train)
	
with open('y_train.txt', 'r') as file_y_train: 
	y_train = json.load(file_y_train)
	
with open('x_test.txt', 'r') as file_x_test: 
	X_test = json.load(file_x_test)

with open('y_test.txt', 'r') as file_y_test:
	y_test = json.load(file_y_test)
	
clf = svm.SVC()
print(clf.fit(X_train, y_train))

predict_result = [] 
for element in X_test: 
    predict_result.append(clf.predict(element))
cnt = 0; 
for i in range(0, len(predict_result), 1): 
    if predict_result[i] == y_test[i]: 
        cnt += 1 
precision_ratio = cnt / len(predict_result) 
print('precision ratio = ', precision_ratio) 