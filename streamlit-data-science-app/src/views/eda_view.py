from src.utils.logger import setup_logger
import streamlit as st
import ydata_profiling as ydp
import dtale
import sweetviz as sv

logger = setup_logger()

def render_eda_view(dataset):
    try:
        st.title("Exploratory Data Analysis")
        
        # YData Profiling
        if st.checkbox("Generate YData Profile Report"):
            profile = ydp.ProfileReport(dataset)
            st_profile_report = profile.to_streamlit()
        
        # D-Tale
        if st.checkbox("Launch D-Tale"):
            d = dtale.show(dataset)
            st.write("D-Tale is running. Click [here](%s) to view." % d._url)
        
        # Sweetviz
        if st.checkbox("Generate Sweetviz Report"):
            report = sv.analyze(dataset)
            report.show_html('sweetviz_report.html')
            st.write("Sweetviz report generated. Check the file 'sweetviz_report.html'.")

    except Exception as e:
        logger.error("Error in EDA view: %s", e)
        st.error("An error occurred while generating EDA results.")