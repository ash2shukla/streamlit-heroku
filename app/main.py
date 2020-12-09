import streamlit as st

from src.utils import add_custom_css
from src.pages import PAGE_MAP
from src.state import provide_state

add_custom_css()

@provide_state()
def main(state=None):
    current_page = st.sidebar.radio("Go To", list(PAGE_MAP))
    PAGE_MAP[current_page](state=state).write()

if __name__ == "__main__":
    main()