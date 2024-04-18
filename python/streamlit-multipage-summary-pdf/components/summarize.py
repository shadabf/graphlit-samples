import streamlit as st
import time
from datetime import datetime
from other import client
from graphlit_api import *

async def handle_summarize(summarization_type, summarization_prompt):
    if st.session_state['token']:
        if st.session_state['specification_id'] is not None:
            with st.spinner('Deleting existing specification... Please wait.'):
                await client.delete_specification()
            st.session_state["specification_id"] = None

        error_message = await client.create_specification()

        if error_message is not None:
            st.error(error_message)
        else:
            start_summary_time = time.time()

            with st.spinner('Generating summary... Please wait.'):
                if summarization_prompt.strip() != "":
                    summarization_type = SummarizationTypes.CUSTOM

                placeholder = st.empty()

                summary, error_message = await client.summarize_contents(summarization_type, summarization_prompt)

                if error_message is not None:
                    st.error(error_message)
                    return
                
                placeholder.markdown(summary)

                summary_duration = time.time() - start_summary_time

                current_time = datetime.now()
                formatted_time = current_time.strftime("%H:%M:%S")

                st.success(f"Summary generation took {summary_duration:.2f} seconds. Finished at {formatted_time} UTC.")
