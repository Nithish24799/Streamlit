import streamlit as st

def main_page():
    st.header('Instagram EDA')
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/ML_project/blob/main/Social_media_guvi_project/EDA%20on%20Instagram.ipynb")#github link
    st.header("Problem Statement")
    st.markdown("""1.Are there any correlated features in the given dataset? If yes, state the correlation
    coefficient of the pair of features which are highly correlated.\n
    2. What is the frequency distribution of the following features?
    ○ Influence Score
    ○ Followers
    ○ Posts\n
    3. Which country houses the highest number of Instagram Influencers? Please show the
    count of Instagram influencers in different countries using barchart.\n
    4. Who are the top 10 influencers in the given dataset based on the following features
    ● Followers
    ● Average likes
    ● Total Likes\n
    5. Describe the relationship between the following pairs of features using a suitable graph
    ● Followers and Total Likes
    ● Followers and Influence Score""")
    st.markdown("""Reference is taken on the third party API and code is written by Nithish(Aspiring Data Scientist)""")

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
    st.markdown("""Reference is taken on the third party API and code is written by Nithish(Aspiring Data Scientist)""")

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
    st.markdown("""Reference is taken on the third party API and code is written by Nithish(Aspiring Data Scientist)""")
    
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
    st.markdown("""Reference is taken on the third party API and code is written by Nithish(Aspiring Data Scientist)""")
    

def page5():
    st.header("Weather Data")
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/Data_Science/tree/main/Data_analysis/Weather_data_visualization ")#github link
    st.header("Explaination")
    st.markdown("""The project i have taken from API and the weather data has
    Date/Time,Temp_C,Dew Point,Temp_C,Rel Hum_%,Wind Speed_km/h,Visibility_km,Press_kPa,Weather
     i have performed data cleaning process like\n
     1.handling the missing value\n
     2.descriptive statistic\n
     3.datetime function\n""")
    st.markdown("""Reference is taken on the third party API and code is written by Nithish(Aspiring Data Scientist)""")
def page6():
    st.header("Twitter Sentimental analysis")
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/ML_project/blob/main/Social_media_guvi_project/Twitter_sentimental_analysis.ipynb")#github link
    st.header("Problem statement")
    st.markdown("""It contains the following 6 fields:\n
    1. target: the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)\n
    2. ids: The id of the tweet .\n
    3. date: The date of the tweet (Sat May 16 23:58:44 UTC 2009)\n
    4. flag: The query. If there is no query, then this value is NO_QUERY.\n
    5. user: The user that tweeted\n
    6. text: The text of the tweet.\n
    Design a classification model that correctly predicts the polarity of the tweets provided in the
    dataset""")
    st.markdown("""Reference is taken on the third party API and code is written by Nithish(Aspiring Data Scientist)""")
def page7():
    st.header("Flight fare price prediction")
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/ML_project/tree/main/Flight_Fare_prediction")#github link
    st.header("Problem statement")
    st.markdown("""The Flight fare prediction.\n
    The feature are Airline,Date_of_Journey,Source,Destination,Route,Dep_Time,Arrival_Time,Duration,Total_Stops,Additional_Info,\n
    And the price is dependent feature remaining feature are independent.\n
    Data cleaning process and feature selection are performed in the dataset.\n
    Also handled the categorical value concept used here is onehotencoding and replace function.\n
    model used in the project is randomforestregressor.\n
    The dataset taken from the youtube source Channel name: Skillcate""")
    st.markdown("""Reference is taken on the third party API and code is written by Nithish(Aspiring Data Scientist)""")
def page8():
    st.header("Bangalore house price prediction")
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/ML_project/tree/main/Bangalore_price_prediction")#github link
    st.header("Problem statement")
    st.markdown("""The Bangalore house pricw prediction.\nThe feature are area_type,availability,location,size,society,total_sqft,bath,balcony,price\n
    And the price is dependent feature remaining feature are independent\n
    Data cleaning process and feature selection are performed in the dataset\n
    Also handled the categorical value concept used here is onehotencoding\n
    model used in the project is linear regression\n
    The dataset taken from the youtube source Channel name: Codebasics""")
    st.markdown("""Reference is taken on the third party API and code is written by Nithish(Aspiring Data Scientist)""")
def page9():
    st.header("Time series Forecasting")
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/ML_project/tree/main/Time_series_forecasting")#github link
    st.header("Problem statement")
    st.markdown("""The oil price prediction based on time series forecasting.\nThe feature are timestamp,Price and these are taken from quandl\n 
    And the price is dependent feature timestamp feature are independent\n
    Data cleaning process and feature selection are performed in the dataset\n
    model used in the project is linear regression\n
    The dataset taken from the quandl api""")
    st.markdown("""Reference is taken on the third party API and code is written by Nithish(Aspiring Data Scientist)""")
def page10():
    st.header("Movie recommendation system")
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/ML_project/tree/main/movie_recommendation")#github link
    st.header("Problem statement")
    st.markdown("""Building Movie recommendation system.\nThe feature are genres,keywords,tagline,cast,director.\n
    Data cleaning process and feature selection are performed in the dataset\n
    The closet match is finded by difflib libraries\n
    The netflix movie and the concept are cosine similarity\n
    The dataset taken from the youtube channel name: datascience love""")
    st.markdown("""Reference is taken on the third party API and code is written by Nithish(Aspiring Data Scientist)""")
def page11():
    st.header("Guvi project")
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/Guvi_project")#github link
    st.header("Problem statement")
    st.markdown("""The GUVI institution has given several task to pratice for data science and namely the topics are\n
    1.Pandas\n
    2.Numpy\n
    3.Statistics\n
    4.visualization\n
    5.EDA process\n
    6.Feature selection\n
    7.Model buliding\n
    8.data analysis project\n
    9.data sciencist project and many more project...""")
    st.markdown("""Reference is taken on the third party API and code is written by Nithish(Aspiring Data Scientist)""")

page_names_to_funcs = {
    "Instagram EDA":main_page,
    "Netflix_data": page2,
    "Sales_insight": page3,
    "Registeration_Python": page4,
    "Weather_data": page5,
    "Twitter Sentimental analysis":page6,
    "Flight fare price prediction":page7,
    "Bangalore house price prediction":page8,
    "Time series forecasting":page9,
    "Movie recommendation":page10,
    "Guvi project":page11
}
st.sidebar.header("Data Science Project")
selected_page = st.sidebar.selectbox("Select a Project ", page_names_to_funcs.keys())
st.sidebar.markdown("In Datascience project,some Data analyst work and some Data scientist work and its a combination of analysis and model buliding is there and the reference of dataset for each project is taken from different source.")
page_names_to_funcs[selected_page]() 