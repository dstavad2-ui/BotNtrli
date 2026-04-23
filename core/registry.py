class Registry:
    def __init__(self):
        self.agents = {}

    def register_agent(self, name, agent):
        self.agents[name] = agent

    def execute_agent(self, name, task):
        return self.agents[name].execute(task)
