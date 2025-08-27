from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
from python_a2a import AgentNetwork, A2AClient, AIAgentRouter
from dotenv import load_dotenv
import asyncio 

load_dotenv()

async def main():

    #create an agent Network
    network = AgentNetwork(name="Travel Assistant Network")

    #add agents to the party
    network.add("weather","http://localhost:8001")
    network.add("search","http://localhost:8002")

    #list all available agents
    for agent_info in network.list_agents():
        print(f"- {agent_info["name"]}: {agent_info["description"]}.")

    
    location = input("Which City you want to visit? ")   
    travel_dates = input("When? ")          
    
    weather_agent = network.get_agent("weather")
    forecast = weather_agent.ask(f"What's the weather in {location}?")
    print ("Weather forecast: "+ forecast)
    search_agent = network.get_agent("search")
    activities = ""
    if "sunny" in forecast.lower() or "clear" in forecast.lower():
        activities = search_agent.ask(f"Recommend outdoor activities in {location}")
    else:
        activities = search_agent.ask(f"Recommend indoor activities in {location}")
    print("Activities")
    print(activities)
    
    
if __name__ == "__main__":
    asyncio.run(main())