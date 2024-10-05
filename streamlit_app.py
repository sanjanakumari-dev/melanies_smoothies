# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Example Streamlit App :balloon:")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)



name_on_order = st.text_input('name on smoothie:')
st.write(' The name on your smoothie will be:', name_on_order)



cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'choose upto 5 ingredients:'
    , my_dataframe
)

if ingredients_list:
    st.write(ingredients_list)
    st.text(ingredients_list)


    ingredients_string = ''

    for fruit_choosen in ingredients_list:
        ingredients_string += fruit_choosen

    #st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """','"""+name_on_order+"""')"""

    st.write(my_insert_stmt)
    st.stop
    time_to_insert = st.button('submit order')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
    
    st.success('Your Smoothie is ordered!', icon="✅")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response.json())
