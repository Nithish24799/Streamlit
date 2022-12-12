import streamlit as st

def main_page():
    st.header('Instagram EDA')
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/ML_project/tree/main/Social_media_guvi_project")#github link
    st.header("Explaination")
    st.markdown("""Twitter sentimental analysis

    problem statement: Design a classification model that correctly predicts the polarity of the tweets provided in the
    dataset

    instagram data have to do EDA process""")
    st.markdown("""The project is taken from the third party API and the code is written by Nithish(Aspiring Data Scientist)""")

def page2():
    st.header("Netflix data")
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/Data_Science/tree/main/Data_analysis/Netfix_data_analysis ")#github link
    st.header("Explaination")
    st.markdown("""The project i have taken from API and the Netflix data has
     Show_Id,Category,Title,Director,Cast,Country,Release_Date,Rating,Duration,Type,Description 
     i have performed data cleaning process like\n
     1.handling the missing value\n
     2.duplicate handling\n
     3.datetime function\n""")
    st.markdown("""The project is taken from the third party API and the code is written by Nithish(Aspiring Data Scientist)""")

def page3():
    st.header("Sales insight")
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/Data_Science/tree/main/Data_analysis/Sales_insight ")#github link
    st.header("Explaination")
    st.markdown("""The project i have taken from API and the Sales insight data which has
     Multiple csv with the column name of Order ID,Product,Quantity Ordered,Price Each,Order Date,Purchase Address
     i have performed data cleaning process like\n
     1.merge the multiple csv to one csv file\n
     2.type casting the datatype\n
     3.use some visualization\n""")
    st.markdown("""The project is taken from the third party API and the code is written by Nithish(Aspiring Data Scientist)""")
def page4():
    st.header("Registration")
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/Data_Science/tree/main/Data_analysis/Task_1_registration_folder ")#github link
    st.header("Explaination")
    st.markdown("""The project is given by GUVI institution and it has to be done using python
     under the concept of File handling
     i have seprate the process like\n
     1.First user to register with username and password 
     (username and password want to check if it is valid or not with some criteria)
     then save it in the text file\n
     2.Login with the valid username and password and check whether the username and
      password are in the file or not if not go to the registration \n
     3.Forget password if the user click on forget pasword two thing to do\n
     A)Retrive the data with the username itself\n
     B)Provide new password and replace the new password with the 
     usernamme in the file """)
    st.markdown("""The project is taken from the third party API and the code is written by Nithish(Aspiring Data Scientist)""")

def page5():
    st.header("Twitter sentimental analysis")
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/ML_project/tree/main/Twitter_API_sentimental_analysis")#github link
    st.header("Explaination")
    st.markdown("""The Sentimental analysis on live tweet.....

    The feature are text and the data is taken from the tweepy library using twitter API.

    Data cleaning process and feature selection are performed in the dataset

    Handling the text data using the countvectorizer method

    The model used is multinomial naives bayes

    The dataset taken from the twitter API""")
    st.markdown("""The project is taken from the third party API and the code is written by Nithish(Aspiring Data Scientist)""")

def page6():
    st.header("Bangalore house price prediction")
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/ML_project/tree/main/Bangalore_price_prediction")#github link
    st.header("Explaination")
    st.markdown("""The Bangalore house pricw prediction.

    The feature are area_type,availability,location,size,society,total_sqft,bath,balcony,price

    And the price is dependent feature remaining feature are independent
        
    Data cleaning process and feature selection are performed in the dataset
            
    Also handled the categorical value concept used here is onehotencoding
            
    model used in the project is linear regression
                
    The dataset taken from the youtube source Channel name: Codebasics""")
    st.markdown("""The project is taken from the third party API and the code is written by Nithish(Aspiring Data Scientist)""")

def page7():
    st.header("Flight Fare Price Prediction")
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/ML_project/tree/main/Flight_Fare_prediction")#github link
    st.header("Explaination")
    st.markdown("""The Flight fare prediction.....

    The feature are Airline,Date_of_Journey,Source,Destination,Route,Dep_Time,Arrival_Time,Duration,Total_Stops,Additional_Info,Price

    And the price is dependent feature remaining feature are independent
        
    Data cleaning process and feature selection are performed in the dataset
            
    Also handled the categorical value concept used here is onehotencoding and replace function
            
    model used in the project is randomforestregressor
                
    The dataset taken from the youtube source Channel name: Skillcate""")
    st.markdown("""The project is taken from the third party API and the code is written by Nithish(Aspiring Data Scientist)""")

def page8():
    st.header("Time series Analysis")
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/ML_project/tree/main/Time_series_forecasting")#github link
    st.header("Explaination")
    st.markdown("""The oil price prediction based on time series forecasting.....

    The feature are timestamp,Price and these are taken from quandl 

    And the price is dependent feature timestamp feature are independent
        
    Data cleaning process and feature selection are performed in the dataset
            
    model used in the project is linear regression
                
    The dataset taken from the quandl api""")
    st.markdown("""The project is taken from the third party API and the code is written by Nithish(Aspiring Data Scientist)""")

def page9():
    st.header("Movie Recommendation system")
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/ML_project/tree/main/movie_recommendation")#github link
    st.header("Explaination")
    st.markdown("""Building Movie recommendation system.....

    The feature are genres,keywords,tagline,cast,director.

    Data cleaning process and feature selection are performed in the dataset

    The closet match is finded by difflib libraries

    The netflix movie and the concept are cosine similarity

    The dataset taken from the youtube channel name: datascience lover""")
    st.markdown("""The project is taken from the third party API and the code is written by Nithish(Aspiring Data Scientist)""")

def page10():
    st.header("GUVI project")
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/Guvi_project")#github link
    st.header("Explaination")
    st.markdown("""IITM Advance Professional Programing with Master data science program with Guvi Task for practice
    
    Project like:
    1.Pandas\n
    2.Numpy\n
    3.Statistics\n
    4.Machine learning\n
    5.NLP  and goes on...""")
    st.markdown("""The project is taken from the third party API and the code is written by Nithish(Aspiring Data Scientist)""")

page_names_to_funcs = {
    "Census_data": main_page,
    "Netflix_data": page2,
    "Sales_insight": page3,
    "Registeration_Python": page4,
    "Twitter Sentimental analysis": page5,
    "Bangalore house price prediction ":page6,
    "Flight fare price prediction":page7,
    "Time series analysis":page8,
    "Movie recommendation system":page9,
    "GUVI project":page10
}
st.sidebar.header("Data Science project")
selected_page = st.sidebar.selectbox("Select a Project", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]() 
