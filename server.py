import random
from fastmcp import FastMCP

mcp = FastMCP(name="drink_dice_server")

@mcp.tool
def roll_drink_dice() -> str:
    """Rolls a drink dice and returns the result."""

    drink_options = [
        "萊恩不用喝",
        "萊恩隨意喝",
        "萊恩喝一杯",
        "萊恩喝兩杯",
        "萊恩左邊的幫忙喝",
        "萊恩右邊的幫忙喝",
    ]

    drink_result = random.choice(drink_options)
    return drink_result

if __name__ == "__main__":
    mcp.run(transport="sse", port=8000)
    # mcp.run(transport="stdio")
