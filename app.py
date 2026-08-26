import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
d= pd.read_csv("C:/Users/DELL/Downloads/archive (2)/placement.csv")
print(d)
print(d.isnull().sum())

x=d[['cgpa']]
y=d[['package']]
print(x.shape,y.shape)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
print(x_train,'\n',x_test,'\n',y_train,'\n',y_test)

lr=LinearRegression()
lr=lr.fit(x_train,y_train)

y_pred=lr.predict(x_test)
print("prediction of salary:",y_pred)

train_ac=lr.score(x_train,y_train)
test_ac=lr.score(x_test,y_test)
print("traing accuracy:",train_ac)
print("testing accuracy:",test_ac)


model=LinearRegression()
model.fit(x,y)
st.title("PACKAGE PREDICTOR")
st.write("enter your CGPA to get package prediction")

st.sidebar.header("Enter your details")

cgpa=st.sidebar.text_input("enter your CGPA")

if st.sidebar.button('predict package'):
    try:
        cgpa=float(cgpa)
        input_data=pd.DataFrame({'cgpa':[cgpa]})
        prediction = model.predict(input_data)


        st.success(f"Predicted Package: {prediction[0][0]:.2f} LPA")
    except ValueError:
        st.error("please enter valid input")   