from utils.dataset_tools import search_kaggle, search_huggingface

class ResourceCollectionAgent:
    def __init__(self, use_cases):
        self.use_cases = use_cases

    def collect_resources(self):
        resources = {}
        for case in self.use_cases:
            kaggle_data = search_kaggle(case) or []
            hf_data = search_huggingface(case) or []
            resources[case] = kaggle_data + hf_data
        return resources
