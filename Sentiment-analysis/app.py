from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext
import emoji

st.title("Sentiment Web Analyzer")
background_image = 'image.jpg'
st.image(background_image, use_column_width=True)

st.header("Now Scale Your Thoughts")

with st.expander("Analyze Your Text"):
    text = st.text_input("Text here:")

    if text:
        blob = TextBlob(text)
        p= round(blob.sentiment.polarity,2)
        st.write('Polarity :',p)
        if p>=0.1:
               st.write(emoji.emojize("Positive Speech :grinning_face_with_big_eyes:"))
        elif p==0.0:
            st.write(emoji.emojize("Neutral Speech :zipper-mouth_face:"))
        else :
            st.write(emoji.emojize("Negative Speech :disappointed_face:"))
        st.write('Subjectivity', round(blob.sentiment.subjectivity,2))


    pre = st.text_input('Clean Your Text: ')
    if pre:
        st.write(cleantext.clean(pre, clean_all= False, extra_spaces=True ,
                                 stopwords=True ,lowercase=True ,numbers=True , punct=True))

with st.expander('Analyze Excel files'):
    st.write("_**Note**_ : Your file must contain the column Name'Tweets' that contain the text to be analyzed.")
    upl = st.file_uploader('Upload file')

    def score(x):
        blob1 = TextBlob(x)
        return blob1.sentiment.polarity

#
    def analyze(x):
        if x >= 0.5:
            return 'Positive'
        elif x <= -0.5:
            return 'Negative'
        else:
            return 'Neutral'

#
    if upl:
        df = pd.read_excels(upl)
        # del df['Unnamed: 0']
        df['score'] = df['tweets'].apply(score)
        df['analysis'] = df['score'].apply(analyze)
        st.write(df.head(10))

        @st.cache
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='sentiment.csv',
            mime='text/csv',
        )
st.write("\n\n\n\n\n")

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("\t\t\t\t\t\tCopy© 2023 Adeel Munir")