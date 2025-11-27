import random
from fastmcp import FastMCP

mcp = FastMCP(name="drinkdiceserver")

@mcp.tool
def roll_drink_dice() -> str:
    """Rolls a drink dice and returns the result."""
    drink_options = [
        "Beer",
        "Wine",
        "Whiskey",
        "Vodka",
        "Rum",
        "Tequila",
        "Gin"
    ]
    
    drink_result = random.choice(drink_options)
    return drink_result


if __name__ == "__main__":
    mcp.run(transport="sse", port=8000)
