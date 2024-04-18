import streamlit as st

def create_sidebar():
    with st.sidebar:
        st.info("""
                ### ✅ Demo Instructions
                - [Sign up for Graphlit](https://docs.graphlit.dev/getting-started/signup) 🆓  
                - **Step 1:** Generate Graphlit project token.
                - **Step 2:** Fill in the Reddit subreddit name.
                - **Step 3:** Click to generate summary of recent Reddit subreddit posts using [Anthropic](https://www.anthropic.com) Claude 3 Haiku LLM.     
                """)

        st.markdown("""
            [Support on Discord](https://discord.gg/ygFmfjy3Qx)            
            [API Reference](https://docs.graphlit.dev/graphlit-data-api/api-reference)     
            [More information](https://www.graphlit.com)      
            """)
