# -*-coding:utf8-*-
import sklearn
# Multinomial Naive Bayes Classifier

def naive_bayes(x_train, y_train):
    from sklearn.naive_bayes import MultinomialNB
    model = MultinomialNB(alpha=0.01)
    model.fit(x_train, y_train)
    return model
# KNN classifier

def knn(x_train, y_train):
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier()
    model.fit(x_train, y_train)
    return model

# logistic Regression classifier
def logistic_regression(x_train, y_train):
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(penalty = 'l2')
    model.fit(x_train, y_train)
    return model

# Random Forest Classifier    
def random_forest(x_train, y_train):    
    from sklearn.ensemble import RandomForestClassifier    
    model = RandomForestClassifier(n_estimators=8)    
    model.fit(x_train, y_train)    
    return model 

# Decision Tree Classifier    
def decision_tree(x_train, y_train):    
    from sklearn import tree    
    model = tree.DecisionTreeClassifier()    
    model.fit(x_train, y_train)    
    return model    
    
    
# GBDT(Gradient Boosting Decision Tree) Classifier    
def gradient_boosting(x_train, y_train):    
    from sklearn.ensemble import GradientBoostingClassifier    
    model = GradientBoostingClassifier(n_estimators=200)    
    model.fit(x_train, y_train)    
    return model    
    
    
# SVM Classifier    
def svm(x_train, y_train):    
    from sklearn.svm import SVC    
    model = SVC(kernel='rbf', probability=True)    
    model.fit(x_train, y_train)    
    return model   

# NN classifier
def neural_network(x_train, y_train):
    from sklearn.neural_network import MLPClassifier
    model = MLPClassifier(solver='lbfgs',alpha=1e-5, hidden_layer_sizes=(5,2),random_state=1)
#     model = MLPClassifier(solver='sgd', activation='relu',alpha=1e-4,hidden_layer_sizes=(50,50), random_state=1,max_iter=10,verbose=10,learning_rate_init=.1)
    model.fit(x_train, y_train)
    return model

    