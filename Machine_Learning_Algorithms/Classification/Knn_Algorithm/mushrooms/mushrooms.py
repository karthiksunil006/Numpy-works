import pandas as pd
import numpy as np
import streamlit
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv("C:/Users/HP/OneDrive/Desktop/Numpy works/mushrooms/mushrooms.csv")
df=pd.DataFrame(data)
df

print(df.isna().sum())



Le=LabelEncoder()
for i in list(df):

    df[i]=Le.fit_transform(df[i])

X=df.iloc[:,:-1]
Y=df.iloc[:,-1]



X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)



scaler=StandardScaler()

X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)


knn=KNeighborsClassifier()

knn=knn.fit(X_train,Y_train)

Y_pred=knn.predict(X_test)



print(accuracy_score(Y_pred,Y_test))


def input_features():

    cls=streamlit.text_input("Enter the class : ")
    cap_shape=streamlit.text_input("Enter the cap_shape : ")
    cap_surface=streamlit.text_input("Enter the cap_surface : ")
    cap_color=streamlit.text_input("Enter the cap_color : ")
    bruises=streamlit.text_input("Enter the bruises : ")
    odor=streamlit.text_input("Enter the odor : ")
    gill_attachment=streamlit.text_input("Enter the gill_attachment : ")
    gill_spacing=streamlit.text_input("Enter the gill_spacing : ")
    gill_size=streamlit.text_input("Enter the gill_size : ")
    gill_color=streamlit.text_input("Enter the gill_color : ")
    stalk_shape=streamlit.text_input("Enter the stalk_shape : ")
    stalk_root=streamlit.text_input("Enter the Stalk_root : ")
    stalk_surface_above_ring=streamlit.text_input("Enter the Stalk_surface above ring : ")
    stalk_surface_below_ring=streamlit.text_input("Enter the stalk_surface below ring : ")
    stalk_color_above_ring=streamlit.text_input("Enter the stalk color above ring : ")
    stalk_color_below_ring=streamlit.text_input("Enter the stalk color below ring : ")
    veil_type=streamlit.text_input("Enter the veil type : ")
    veil_color=streamlit.text_input("Enter the veil color : ")
    ring_number=streamlit.text_input("Enter the ring number : ")
    ring_type=streamlit.text_input("Enter the ring type : ")
    spore_print_color=streamlit.text_input("Enter the spore sprint color : ")
    population=streamlit.text_input("Enter the population : ")


    features={
        "class":cls,
        "cap-shape":cap_shape,
        "cap-surface":cap_surface,
        "cap-color":cap_color,
        "bruises":bruises,
        "odor":odor,
        "gill-attachment":gill_attachment,
        "gill-spacing":gill_spacing,
        "gill-size":gill_size,
        "gill-color":gill_color,
        "stalk-shape":stalk_shape,
        "stalk-root":stalk_root,
        "stalk-surface-above-ring":stalk_surface_above_ring,
        "stalk-surface-below-ring":stalk_surface_below_ring,
        "stalk-color-above-ring":stalk_color_above_ring,
        "stalk-color-below-ring":stalk_color_below_ring,
        "veil-type":veil_type,
        "veil-color":veil_color,
        "ring-number":ring_number,
        "ring-type":ring_type,
        "spore-print-color":spore_print_color,
        "population":population
    }

    features=pd.DataFrame(features,index=[0])
    return features

input_df=input_features()

for i in list(input_df):

    input_df[i]=Le.fit_transform(input_df[i])


scaled_df=scaler.transform(input_df)

result=knn.predict(scaled_df)

if streamlit.button("show result"):

    if result[0]==0:

        streamlit.success(f"Habitat is d")

    elif result[0]==1:
        streamlit.success(f"Habitat is g")

    elif result[0]==2:
        streamlit.success(f"Habitat is I")

    elif result[0]==3:
        streamlit.success(f"Habitat is m")

    elif result[0]==4:
        streamlit.success(f"Habitat is p")

    elif result[0]==5:
        streamlit.success(f"Habitat is u")

    elif result[0]==6:
        streamlit.success(f"Habitat is w")






    #class,cap-shape,cap-surface,cap-color,bruises,odor,gill-attachment,gill-spacing,gill-size,gill-color,stalk-shape,stalk-root
    # ,stalk-surface-above-ring,stalk-surface-below-ring,stalk-color-above-ring,stalk-color-below-ring,veil-type,veil-color
    # ,ring-number,ring-type,spore-print-color,population,habitat

