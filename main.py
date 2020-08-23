import streamlit as st

from src.utils import Page, provide_state
from src.pages import Page1, Page2

from typing import Dict, Type

PAGE_MAP: Dict[str, Type[Page]] = {
    "Page 1": Page1,
    "Page 2": Page2,
}

@provide_state()
def main(state=None):
    current_page = st.sidebar.radio("Go To", list(PAGE_MAP))
    PAGE_MAP[current_page](state=state).write()

if __name__ == "__main__":
    main()