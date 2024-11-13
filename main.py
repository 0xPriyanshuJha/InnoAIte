import streamlit as st
from agents.indus_agent import IndusResearch
from agents.usecase_agent import UsecaseResearch
from agents.collection_agent import ResourceCollectionAgent
from agents.proposal_agent import ProposalAgent

def main():
    st.title("Industry & Company Research Proposal Generator")
    company_name = st.text_input("Enter the Company Name", "Tesla")
    industry = st.text_input("Enter the Industry", "Automotive")

    if st.button("Generate Proposal"):
        st.write("Generating research proposal...")

        research_agent = IndusResearch(company_name, industry)
        industry_info = research_agent.gather_indus_info()
        company_info = research_agent.gather_info()

        usecase_agent = UsecaseResearch(industry, company_name)
        use_cases = usecase_agent.generate_usecases()

        collection_agent = ResourceCollectionAgent(use_cases)
        resources = collection_agent.collect_resources()

        proposal_agent = ProposalAgent(industry_info, company_info, use_cases, resources)
        proposal = proposal_agent.generate_proposal()

        st.write("### Research Proposal")
        st.write(proposal)

if __name__ == "__main__":
    main()
