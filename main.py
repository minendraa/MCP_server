import streamlit as st
import os
from dotenv import load_dotenv
from mcp_server import MCPServer

# --- Page Configuration ---
st.set_page_config(
    page_title="MCP AI Analysis Bot",
    page_icon="🤖",
    layout="wide"
)

# --- Application Setup ---
# Load environment variables from .env file
load_dotenv()

# Function to get the MCP Server instance, cached for performance
@st.cache_resource
def get_mcp_server():
    """Creates and caches the MCP Server instance."""
    # Check for API key after loading .env
    if not os.getenv("OPENAI_API_KEY"):
        st.error("OpenAI API key not found. Please add it to your .env file.", icon="🚨")
        st.stop()
    
    server = MCPServer()
    return server

# --- UI Layout ---
st.title("🤖 Multi-Agent Company Analysis Bot")
st.info("Enter a company name below. Three specialized AI agents will collaborate to produce a research report, a financial analysis, and a final SWOT analysis.")

# Get the server instance
mcp_server = get_mcp_server()

# --- Main Application Logic ---
company_name = st.text_input("Enter the name of the company you want to analyze:", placeholder="e.g., Apple, Nvidia, Microsoft")

if st.button("Analyze Company", type="primary"):
    if not company_name:
        st.warning("Please enter a company name.", icon="⚠️")
    else:
        st.success(f"Starting analysis for: {company_name}")

        # --- Step 1: Research ---
        with st.spinner("Step 1/3: The Researcher is gathering information..."):
            try:
                research_report = mcp_server.run_research_step(company_name)
            except Exception as e:
                st.error(f"An error occurred during research: {e}")
                st.stop()
        
        with st.expander("✅ Research Report", expanded=True):
            st.markdown(research_report)

        # --- Step 2: Financial Analysis ---
        with st.spinner("Step 2/3: The Financial Analyst is crunching the numbers..."):
            try:
                financial_analysis = mcp_server.run_financial_analysis_step(research_report, company_name)
            except Exception as e:
                st.error(f"An error occurred during financial analysis: {e}")
                st.stop()

        with st.expander("✅ Financial Analysis", expanded=True):
            st.markdown(financial_analysis)

        # --- Step 3: Strategic Analysis ---
        with st.spinner("Step 3/3: The Strategist is creating the SWOT analysis..."):
            try:
                swot_analysis = mcp_server.run_strategy_step(research_report, financial_analysis, company_name)
            except Exception as e:
                st.error(f"An error occurred during strategic analysis: {e}")
                st.stop()

        st.subheader("🎯 Final Strategic (SWOT) Analysis", anchor=False)
        st.markdown(swot_analysis)

        st.balloons()
        st.success("Analysis Complete!")