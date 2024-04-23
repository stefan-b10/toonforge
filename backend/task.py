from crewai import Task, Agent
from textwrap import dedent

class ComicsTasks():
    def __init__(self, job_id:str):
        self.job_id = job_id

    def write_story(self, agent: Agent, tasks: list[Task]):
        return Task(
            description=dedent(f"""  """),
            agent= agent,
            expected_output=dedent(""" """),
            callback=self.append_event_callback,
            context=tasks,
            output_json=PositionInfoList
        )

    def write_screenplay():
        pass

    def generate_image():
        pass