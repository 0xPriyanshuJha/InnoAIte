class ProposalAgent:
    def __init__(self, industry_info, company_info, use_cases, resources):
        self.industry_info = industry_info
        self.company_info = company_info
        self.use_cases = use_cases
        self.resources = resources
    
    def generate_proposal(self):
        proposal = f"## Industry Insights\n{self.industry_info}\n\n"
        proposal += f"## Company Focus\n{self.company_info}\n\n"
        proposal += "## AI Use Cases\n"
        for idx, case in enumerate(self.use_cases, 1):
            proposal += f"{idx}. {case}\n"
        
        proposal += "\n## Resources\n"
        for case, data in self.resources.items():
            proposal += "\n## Resources\n"

        for case, links in self.resources.items():
            proposal += f"### {case}\n"
            
            for link in links:
                proposal += f"- [{link['name']}]({link['url']})\n"

        return proposal