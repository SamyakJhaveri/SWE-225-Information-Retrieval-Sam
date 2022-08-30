
from this import d
import streamlit as st
import time
milliseconds = int(round(time.time() * 1000))
print(milliseconds)
# from idf import searchUrls
from searchUrls import getSortedDocs
def main():
    st.title('Hello! Are you looking for something? :thinking_face:')
    st.write('Search Engine by Team 9')
    # Form for Text Input and Search Button.
    with st.form(key ='form1'):
        search_keywords = st.text_input('We have  Search Engine to help you with that!')
        submit_button = st.form_submit_button('Search!')
    if submit_button:
        start = int(round(time.time() * 1000))
        urls = getSortedDocs(search_keywords)
        end = int(round(time.time() * 1000))
        print(end-start)
        st.success(f"Showing results for '{search_keywords}' in '{end-start}' milliseconds")
        # The format thatshould be displayed here is the result and itss corresponsding TF-IDF value
        # Could you a table with this
        with st.container():
            for url in urls[:5]:
                st.write(url)
        end = int(round(time.time() * 1000))
if __name__ == '__main__':
    main()
