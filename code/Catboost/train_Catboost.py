#importing the required modules

import json
from catboost import CatBoostClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
import pickle
from sklearn.feature_extraction.text import CountVectorizer




def train_catboost(model_type,lables):
        '''train the training dataset with a help of catboost classifier with one vs rest classifier'''
        
        #loding the trained countVectorizer

        vect=pickle.load(open("../static/models/"+model_type+"/vectorizer_catboost", "rb"))
        
        #preprocessing the training data by trainforming it with the help of the CountVectorizer

        X_train,Y_train=[],[]
        with open("../data/train.json",'r') as file:
            js = json.loads("[" +file.read().replace("}\n{", "},\n{") + "]")
            x,y=[],[]
            for j in js:
                x.append(j['title'])
                y.append([lables[z]+1 for z in j['tags']])
           
            X_train,Y_train=vect.transform(x).toarray(),y
        
        # converting label column into a onehot encoding so it can it be trained

        all_labels=[]
        for i in ['train','test','val']:
            with open("../data/"+i+".json",'r') as file:
                js = json.loads("[" +file.read().replace("}\n{", "},\n{") + "]")
                for j in js:
                    
                    all_labels.append([lables[z]+1 for z in j['tags']])

        

        mlb = MultiLabelBinarizer()
        mlb.fit(all_labels)
        y_k_hot = mlb.transform(Y_train)

        iter=100
        depth=6
        
        ovr_1 = OneVsRestClassifier(estimator=CatBoostClassifier(iterations=iter,learning_rate=0.5,depth=depth))
        ovr_1.fit(X_train,y_k_hot)
        pickle.dump(ovr_1, open("../static/models/"+model_type+"/catboost_"+str(iter)+"_iter_"+str(depth)+"_depth.pickle", "wb"))

        return iter,depth
