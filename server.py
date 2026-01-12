from fastmcp import FastMCP
import math

# Initialize the MCP server instance
# The cloud entrypoint will look for this 'mcp' object
mcp = FastMCP("CalculatorCloud")

@mcp.tool()
def calculate(expression: str) -> str:
    """
    Evaluates a mathematical expression safely.
    Example: 'math.sqrt(144) + 2'
    """
    try:
        # Define allowed math functions for safety
        safe_dict = {
            "math": math,
            "abs": abs,
            "round": round,
            "pow": pow,
            "sum": sum
        }
        
        # We use a restricted eval for this example
        result = eval(expression, {"__builtins__": None}, safe_dict)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # This block is for local testing; the cloud will use its own runner
    mcp.run()
