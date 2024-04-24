from crewai import Agent

class ComicAgents:
    def __init__(self, llm):
        self.llm = llm

    def writer(self):
        return Agent (
            role="A very successfull Comics story writer",
            goal=f"""Impress readers with your creative and exciting comics story""",
            backstory="""Very experienced Comics story writer with a great sense of humor.""",
            llm=self.llm,
            tools=[],
            verbose=True,
            allow_delegation=True
        )
    
    def screen_writer(self):
        return Agent (
            role="Comics screen writer",
            goal=f"""Given a story split it into a number of scenes. Each scene should contain a very detailed description of a image that will be generated and a short dialog or text that describes the scene""",
            backstory="""You are a great screen writer with a very creative imagination. You captivate the readers with images generated by your description.""",
            llm=self.llm,
            tools=[],
            verbose=True,
            allow_delegation=True
        )
    
    def artist(self):
        return Agent (
            role="Visual artist",
            goal="Generate a stunningly beautiful image based on a given description",
            backstory="One of the best visual artists in the World.",
            llm=self.llm,
            tools=[],
            verbose=True,
            allow_delegation=True
        )