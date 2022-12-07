import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import warnings
warnings.simplefilter("ignore")
data=pd.read_csv('bengaluru_house_prices.csv')
data=data.drop(['area_type','availability','balcony','society'],axis=1)
data=data.dropna()
data['BHK']=data['size'].apply(lambda x: int(x.split(' ')[0]))
def isfloat(x):
    try:
        float(x)
    except:
        return False
    return True

def convert_sqft_tonum(x):
    token=x.split('-')
    if len(token)==2:
        return (float(token[0])+float(token[1]))/2
    try:
        return float(x)
    except:
        return None

data=data.copy()
data['total_sqft']=data['total_sqft'].apply(convert_sqft_tonum)
data1=data.copy()
data1['price_per_sqft']=data1['price']*1000000/data1['total_sqft']

data1.location=data1.location.apply(lambda x: x.strip())
location_stats=data1.groupby('location')['location'].agg('count').sort_values(ascending=False)
locationlessthan10=location_stats[location_stats<=10]
data1.location=data1.location.apply(lambda x: 'other' if x in locationlessthan10 else x)
data2=data1[~(data1.total_sqft/data1.BHK<300)]
data2["price_per_sqft"].describe().apply(lambda x:format(x,'f'))

def remove_pps_outliers(df):
    df_out=pd.DataFrame()
    for key,subdf in df.groupby('location'):
        m=np.mean(subdf.price_per_sqft)
        st=np.std(subdf.price_per_sqft)
        reduced_df=subdf[(subdf.price_per_sqft>(m-st))& (subdf.price_per_sqft<(m+st))]
        df_out=pd.concat([df_out,reduced_df],ignore_index=True)
    return df_out
data3=remove_pps_outliers(data2)
def remove_bhk_outliers(df):
    exclude_indices=np.array([])
    for location, location_df in df.groupby('location'):
        bhk_sats={}
        for BHK,BHK_df in location_df.groupby('BHK'):
            bhk_sats[BHK]={
                'mean':np.mean(BHK_df.price_per_sqft),
                'std':np.std(BHK_df.price_per_sqft),
                'count':BHK_df.shape[0]
            }
        for BHK,BHK_df in location_df.groupby('BHK'):
            stats=bhk_sats.get(BHK-1)
            if stats and stats['count']>5:
                exclude_indices=np.append(exclude_indices,BHK_df[BHK_df.price_per_sqft<(stats['mean'])].index.values)
    return df.drop(exclude_indices,axis='index')
data4=remove_bhk_outliers(data3)
data5=data4[data4.bath<data4.BHK+2]
data6=data5.drop(['size','price_per_sqft'],axis='columns')
dummies=pd.get_dummies(data6.location)
data7=pd.concat([data6,dummies.drop('other',axis='columns')],axis='columns')
data8=data7.drop('location',axis='columns')
X=data8.drop('price',axis='columns')
y=data8.price
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,y_train)

def price_predict(location,sqft,bath,BHK):
    loc_index=np.where(X.columns==location)[0][0]
    x=np.zeros(len(X.columns))
    x[0]=sqft
    x[1]=bath
    x[2]=BHK
    if loc_index >=0:
        x[loc_index]=1
    return round((model.predict([x])[0]*100000),0)
import streamlit as st
st.title("Bangalore house price prediction")
BHK=st.text_input("Please select size(BHK) 1,2,3,4,5")
sqft=st.text_input("Please select sqftf from 1000 - 5000")
bath=st.text_input("Please select bath 1,2,3,4,5,")
location=st.text_input("Please choose area if not specify known please fill 'other'")
if st.button("Calcuate"):
    try:
        st.success(price_predict(location,sqft,bath,BHK))
    except:
        st.error("Location is not found Try again")




