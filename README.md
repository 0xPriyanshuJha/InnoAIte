# InnoAIte

The **AI Research Proposal Generator** is an automated system that generates research proposals based on a user's specified company and industry. The system utilizes a multi-agent approach, where each agent performs specific tasks such as gathering industry insights, generating AI use cases, collecting relevant resources, and generating the final research proposal. The system is built using Streamlit for the frontend and integrates with open-source APIs to collect data from external platforms like Kaggle and Hugging Face.

## Features

- **Streamlit UI**: A simple web interface where users input the company name and industry.
- **Research Agents**: A set of agents that gather industry information, generate AI use cases, collect relevant resources, and compile the research proposal.
- **External Integrations**: The system integrates with Kaggle and Hugging Face to gather datasets and models related to the AI use cases.
- **Automatic Proposal Generation**: The system generates a comprehensive research proposal that includes:
  - Industry insights
  - Company strategic focus
  - AI use cases
  - Relevant resources (datasets and models)
  
## Prerequisites

- Python 3.7 or higher
- Streamlit
- Ollama (or another LLM provider)
- Kaggle and Hugging Face API (for dataset and model search)
  
## Installation

1. Clone the repository:
  ```bash
  git clone https://github.com/0xPriyanshuJha/InnoAIte.git
  ```

2. Navigate to your repository
  ```bash
   cd ai-research-proposal-generator
  ```

3. Install the requirements
  ```bash
   pip install -r requirements.txt
  ```

4. Start your Streamlit App
  ```bash
  streamlit run frontend.py
  ```
