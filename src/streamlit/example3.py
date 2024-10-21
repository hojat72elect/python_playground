import streamlit

# Text elements
streamlit.title("The title of My First App")
streamlit.header("This is a header")
streamlit.subheader("This is a subheader")

# markdown
streamlit.markdown("""
This is  how we can write **important markdown**
in _streamlit_; but it doesn't support HTML tags inside markdown.
""")

streamlit.caption("This is a tiny and small caption")