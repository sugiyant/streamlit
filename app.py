import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Sugiyanto Site", page_icon=":smiley:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Header Section
with st.container():
        st.title("Hello, I'm Sugiyanto", ":smiley:")
        st.text("Ini adalah aplikasi web sederhana untuk menampilkan data analisis, dibuat menggunakan Streamlit, dan saya sedang belajar Streamlit")
        st.write("[Learn More Streamlit](https://www.streamlit.io/)")

# load assets
lotie_coding = load_lottieurl("https://lottie.host/4f9fd3db-973c-408f-9472-230275be3db7/uHCxTONHuF.json")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.image("https://avatars.githubusercontent.com/u/83605928?v=4", width=200)
        st.header("Apa yang bisa dilakukan aplikasi ini?")
        st.write("###")
        st.write(
            """
            - Menampilkan data analisis
            - Menampilkan data visualisasi
            - Menampilkan data prediksi
            - Menampilkan data hasil prediksi
            - Menampilkan data hasil analisis
            - Menampilkan data hasil visualisasi
            - Menampilkan data hasil analisis dan visualisasi
            - Menampilkan data hasil analisis dan prediksi
            - Menampilkan data hasil visualisasi dan prediksi
            """
        )
        st.write("[Learn More Streamlit](https://www.streamlit.io/)")
    with right_column:
        st_lottie(lotie_coding, speed=1, height=400, key="initial")