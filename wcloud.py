import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="WordCloud Generator",
                layout="wide"
                )

# Remove header and footer
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

def generate_wordcloud(text):
    wordcloud = WordCloud(width=1800, height=900, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot()

def main():
    st.title("WordCloud Generator App")
    st.write("Enter the text below (separated by space) to generate a WordCloud:")
    
    input_text = st.text_area("Input Text")

    if st.button("Generate WordCloud"):
        if input_text.strip() == "":
            st.warning("Please enter some text!")
        else:
            generate_wordcloud(input_text)

if __name__ == "__main__":
    main()

st.markdown("<h6 style='text-align:right;'>WordCloud Generator -- KentKatigbak</h6>", unsafe_allow_html=True)

st.set_option('deprecation.showPyplotGlobalUse', False)
