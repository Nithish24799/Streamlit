import streamlit as st

def main_page():
    st.header('Census Data_cleaning')
    st.subheader('Github link')
    st.write("https://github.com/Nithish24799/Data_Science/tree/main/Data_analysis/Census_data_cleaning ")#github link
    st.header("Explaination")
    st.markdown("""The project i have taken from API and the Census data has
     District_code,State_name,District_name,Population,Male,Female,Literate,Workers,Male_Workers,Female_Workers,Christians,
     Sikhs,Buddhists,Jains,Secondary_Education,Higher_Education,Graduate_Education,Age_Group_0_29,Age_Group_30_49,Age_Group_50
     i have performed data preprocessing like\n
     1.groupby function\n
     2.add prefix and suffix to column name\n
     3.creating and deleting the column\n""")
    st.markdown("""using pandas library in python and you can see the source code on my github account""")
    st.sidebar.header("Description:")
    st.sidebar.markdown('''
The dataset describe the india census data according to state-wise
Need to analyse the data and find the unemployment in statewise  
\nData_Set link: 
''')

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
    st.markdown("""using pandas library in python and you can see the source code on my github account""")
    st.sidebar.header("Description:")
    st.sidebar.markdown('''
The dataset describe the Netflix data according to username
Need to analyse the data and find how many people are subscribed 
\n Data_Set link:
''')

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
    st.markdown("""using pandas and matplotlib library in python and you can see the source code on my github account""")
    st.sidebar.header("Description:")
    st.sidebar.markdown('''
The dataset describe the Sales according to every month 
Need to analyse the data and find how the sales is for every month \n
Data_Set link:
''')
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
    st.markdown("""used python code and you can see the source code on my github account""")
    st.sidebar.header("Description:")
    st.sidebar.markdown('''
    The project is to create a registration form using python code 
    with a concept of file handling,The Jupyter notebook link 
    and full explaination is given in the main page''' )

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
    st.markdown("""using pandas and numpy library in python and you can see the source code on my github account""")
    st.sidebar.header("Description:")
    st.sidebar.markdown('''
The dataset describe the weather data with windspeed,tempature etc,
Need to analyse the data and find how the tempature for every month
\nData_Set link:
''')

page_names_to_funcs = {
    "Census_data": main_page,
    "Netflix_data": page2,
    "Sales_insight": page3,
    "Registeration_Python": page4,
    "Weather_data": page5,
}
st.sidebar.header("Data_Analyst Project")
selected_page = st.sidebar.selectbox("Select a Project", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]() 
