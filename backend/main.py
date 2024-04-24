from crewai import Crew
from agents import ComicAgents
from tasks import ComicTasks
from langchain_community.llms import HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    endpoint_url="HuggingFaceH4/zephyr-7b-beta",
    huggingfacehub_api_token="",
    task="text-generation",
    max_new_tokens=512
)

agents = ComicAgents(llm)
tasks = ComicTasks()

# Setting up agents
writer = agents.writer()
screen_writer = agents.screen_writer()
# artist = agents.artist()

test_input = "A little boy having adventures in a fantasy land"
test_number_scenes = 9
# Setting up tasks
write_story = tasks.write_story(writer, test_input)
write_screenplay = tasks.write_screenplay(screen_writer, test_number_scenes, [write_story])

# generate_image = tasks.generate_image()

# Setting up tools


crew = Crew(
    agents=[writer, screen_writer],
    tasks=[write_story, write_screenplay],
    manager_llm=llm
    )

result = crew.kickoff()

print("Result:")
print(result)

