# Import python packages
import streamlit as st
# from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col




title = st.text_input('Name on Smoothie', value="Mar1")
st.write('The name on your smoothie will be',title)

# cnx = st.connection("snowflake")
# session = cnx.session  # Access the existing session

# # Query the table
# my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
cnx = st.connection("snowflake")
session = cnx.session()

my_dataframe = session.table(
    "smoothies.public.fruit_options").select(col('FRUIT_NAME'), col('FRUIT_NAME'))

# st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect('Choose up to 5 ingredients',my_dataframe,max_selections=5)
NAME_ON_ORDER = title

if ingredients_list:
    # st.write(ingredients_list)
    # st.text(ingredients_list)

    ingredients_string = ""
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '


    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,NAME_ON_ORDER)
            values ('""" + ingredients_string + """','""" + NAME_ON_ORDER +"""')"""
    # st.write(my_insert_stmt)

    time_to_insert = st.button('Submit Order')


    
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!'+ ' ' + NAME_ON_ORDER, icon="✅")











