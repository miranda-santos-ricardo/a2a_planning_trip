from python_a2a import A2AServer, skill, agent, run_server, TaskStatus, TaskState
from dotenv import load_dotenv
import os
import requests
import logging 


load_dotenv()

@agent(
    name = "Weather Agent",
    description="Provides weather information",
    version = "1.0.0",
    url = "https://zzz.example.com"
)
class WeatherAgent(A2AServer):
    @skill(
        name = "get weather",
        description = "get current weather for a location",
        tags=["weather", "forecast"],
        examples="I am a weather agent for getting weather forecast from Open weather API"
    )
    def get_weather(self, location: str) -> str:
        """Get real weather fro a location using OpenWeatherMap API"""
        api_key = os.getenv("OPENWEATHER_API_KEY")

        if not api_key:
            return ValueError("API key for OpenWeatherMap is not set in environment variables.")
        
        try:
            url = (f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&appid={api_key}")
            logging.debug(f"Request URL: {url}")
            response = requests.get(url,timeout=5)
            response.raise_for_status()
            logging.debug(f"Response Status Code: {response.status_code} \n Response Status Text: {response.text}")

            data = response.json()
            #logging.debug(f"Response JSON: {data}")

            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            city_name = data["name"]

            logging.debug(f"Parsed Data: Temp = {temp}, Description = {description}, City = {city_name}")

            return f"The weather in {city_name} is {description} with a temperature of {temp}°F."
        
        except requests.RequestException as e:
            logging.debug(f"Error -> RequestException: {e}")
            return f"Error fetching weather: {e}"
        except (KeyError, TypeError):
            logging.debug(f"Error -> keyError: {KeyError} - TypeError{TypeError}")
            return "Could not parse weather data."

    def handle_task(self, task):
        # Extract location from message
        logging.debug(f"Task received: {task}")
        message_data = task.message or {}
        content = message_data.get("content", {})
        text = content.get("text", "") if isinstance(content, dict) else ""
        
        if "weather" in text.lower() and "in" in text.lower():
            location = text.split("in", 1)[1].strip().rstrip("?.")
            
            # Get weather and create response
            weather_text = self.get_weather(location)
            task.artifacts = [{
                "parts": [{"type": "text", "text": weather_text}]
            }]
            task.status = TaskStatus(state=TaskState.COMPLETED)
        else:
            task.status = TaskStatus(
                state=TaskState.INPUT_REQUIRED,
                message={"role": "agent", "content": {"type": "text", 
                         "text": "Please ask about weather in a specific location."}}
            )
        return task

# Run the server
if __name__ == "__main__":
    agent = WeatherAgent(google_a2a_compatible=True)
    run_server(agent, port=8001, debug=True)