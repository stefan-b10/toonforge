from crewai import Task, Agent
from textwrap import dedent

class ComicTasks():
    # def __init__(self):
    #     self.job_id = job_id

    def write_story(self, agent: Agent, input: str):
        return Task(
            description=dedent(f"""Write a short story for a comic book and choose a main character and a style and two colors that should be predominant in the illustrations. The story is about {input}  """),
            agent= agent,
            expected_output=dedent("""A JSON object containing title, story, style and colors.                                  
                                   Example output:
                                   {
                                   'title': 'The Happy wizard',
                                   'story': 'Once upon a time there was a wizard named Pepe {{...}}',
                                   'style': 'Classic Manga',
                                   'colors': ['red','blue']
                                   } 

                                   Important:
                                   - The final JSON object must include all fields. Do not leave any out.
                                   - Do NOT generate NSFW content
                                   - Make sure the story is short, coherent and with no spelling errors.
                                   """),
        )

    def write_screenplay(self, agent: Agent, number_scenes: int,  context):
        return Task(
            description=dedent(f"""Split the story in {number_scenes} scenes. Each scene should contain a detailed description of a image for the scene and a short dialog or text that describes the scene."""),
            agent= agent,
            context= context,
            expected_output=dedent(""""A JSON object that contains a Array of objects with image and text as fields
                                   Example Output:
                                   [
                                        {'image': 'A beautiful sunset on a green field with a black horse {{...}}', 'text': 'The day was over and {{...}}'},
                                        {{...}}
                                   ]"""),
        )

    def generate_image():
        pass