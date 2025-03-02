import streamlit as st


def main():
    if st.session_state.get("search_in_progress"):
        st.title("Started searching. We'll send you an email when we find something.")
        return
    st.title("Find available properties to rent")
    email = st.text_input("What is your email?", help="We will send you the available properties we found via email", placeholder="your@email.com")
    query = st.text_input("What are you looking for?", help="e.g. '1 bed flat in south London, £1-2k pcm'", placeholder="1 bed flat in south London, £1-2k pcm")
    if st.button("Search", disabled=not email or not query, key="search"):
        # props = await run_search_and_extract(query)
        # st.write(props)
        st.session_state["search_in_progress"] = True
        st.rerun()


if __name__ == "__main__":
    main()
