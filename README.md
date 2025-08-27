# A2A Trip Planner
A2A Trip Planner is a network of agents working together to help you plan your trip.

## Architecture

<img width="1076" height="408" alt="image" src="https://github.com/user-attachments/assets/b6e772a7-5471-4462-acd1-346b5a1202ba" />



## 🔥 Features
- Agent Networks that get the City you want to visit and when, with these 2 informations provide you sugestion based in the forecast weather.

## 📦 Tech Stack
- Python,
- Brave Search API,
- Open Weather API

## 🚀 Getting Started

```bash
git clone https://github.com/rikardoms/a2a_planning_trip
cd a2a_planning_trip
pip install -r requirements.txt (need to include your BRAVESeARCH and OPENWEATHER KEYs in the .env file)
.\venv\Script\activate

to run Weather Agent (separated terminal)

```bash
python .\WeatherAgent.py

to run braveSearch Agent (separated terminal)

```bash
python .\BraveSearchAgent.py

to run Travel Agent Agent (separated terminal)
```bash
python .\Travel_Planner_Agent.py
