from openai import OpenAI
from configparser import ConfigParser

# Load configuration from config.ini
config = ConfigParser()
config.read('config.ini')

client = OpenAI(
    api_key=config.get('AzureOpenAI', 'APIKEY'),
    base_url=config.get('AzureOpenAI', 'ENDPOINT'),
)

default_query = "api-version=2024-08-01-preview"

question = input("question: ")

response = client.chat.completions.create(
    model=config.get('AzureOpenAI', 'DEPLOYMENTNAME'),  # Replace with your model deployment name
    messages=[
        {"role": "user", "content": question}
    ],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the weather forecast for a location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The location to get weather for"
                        },
                        "days": {
                            "type": "integer",
                            "description": "Number of days for forecast"
                        }
                    },
                    "required": ["location"]
                }
            }
        },
        {
            "type": "mcp",
            "server": {
                "label": "drinkdiceserver",
                "server_url": "https://prelusively-nonburnable-audra.ngrok-free.dev/sse",
                "require_approval": "never"
            }
        }
    ],
    tool_choice="auto",
)

print(response.choices[0].message.content)

if response.choices[0].message.tool_calls:
    for tool_call in response.choices[0].message.tool_calls:
        print(f"Tool call: {tool_call.function.name}")
        print(f"Arguments: {tool_call.function.arguments}")

# Allowed tools configuration
allowed_tools = ["get_simple_price"]
