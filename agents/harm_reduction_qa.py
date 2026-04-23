from core.agent_interface import NaturligAgent
import json

class HarmReductionQA(NaturligAgent):
    def execute(self, task, context=None):
        if task["action"] == "get_guide":
            with open('customer/harm_reduction/data/guides.json') as f:
                guides = json.load(f)
            return guides.get(task["substance"], "Guide not found.")
        else:
            return "Naturlig AI: Use /guide <substance> for advice."

    def register(self, registry):
        registry.register_agent("harm_reduction_qa", self)
