import pandas as pd
import numpy as np
import streamlit
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


streamlit.title("DIABETES PREDICTION MODEL")

data=pd.read_csv("C:/Users/HP/OneDrive/Desktop/Numpy works/Streamlit/diabetes_streamlit/diabetes.csv")
df=pd.DataFrame(data)
#print(df)

#print(df.isna().sum())

X=df.iloc[:,:-1]
Y=df.iloc[:,-1]

#print(X)
#print(Y)

#print(df.dtypes)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)

scaler=StandardScaler()

X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

knn=KNeighborsClassifier()

knn=knn.fit(X_train,Y_train)

Y_pred=knn.predict(X_test)

#print(Y_pred)

#print(accuracy_score(Y_test,Y_pred))



def input_features():

    pregnancies=streamlit.number_input("Enter the pregnancies : ",0,20,1)
    glucose=streamlit.number_input("Enter the glucose : ",0,300,120)
    bp=streamlit.number_input("Enter the blood pressure : ",0,122,70)
    skin_thickness=streamlit.number_input("Enter the skin thickness : ",0,100,20)
    insulin=streamlit.number_input("Enter the insulin : ",0,900,80)
    bmi=streamlit.number_input("Enter the bmi : ",0,70,25)
    diabetese_pedigree_function=streamlit.number_input("Enter the diabete pedigree function : ",0,3,1)
    age=streamlit.number_input("Enter the age : ",1,120,33)

    data={
        "Pregnancies":pregnancies,
        "Glucose":glucose,
        "BloodPressure":bp,
        "SkinThickness":skin_thickness,
        "Insulin":insulin,
        "BMI":bmi,
        "DiabetesPedigreeFunction":diabetese_pedigree_function,
        "Age":age
    }

    features=pd.DataFrame(data,index=[0])
    return features


input_df=input_features()

scaled_input=scaler.transform(input_df)

result=knn.predict(scaled_input)

if streamlit.button("Show Result"):

    final_result="Diabetic" if result[0]==0 else "Not Diabetic"

    streamlit.success(final_result)


