import streamlit as st

import webbrowser
st.header('Gbolade')
st.write("war thunder tips")
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
if st.button('open video'):
    webbrowser.open(url)