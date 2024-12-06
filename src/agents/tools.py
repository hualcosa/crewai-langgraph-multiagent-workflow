from langchain.tools import tool
from ..config import weather


class Tools:
    @tool("Tool to get the weather of any location")
    def weather_tool(location):
        """
        Use this tool when you have given a location and you want to find the weather of that location
        """
        return weather.run(location)
