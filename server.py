from fastmcp import FastMCP
import math

# Initialize the MCP server
mcp = FastMCP("PythonCalculator")

@mcp.tool()
def calculate(expression: str) -> str:
    """
    Evaluates a mathematical expression using Python's math library.all trigonometric functions take radians .
    
    Supported Python functions:
    - Basic: +, -, *, /, **
    - Absolute: abs(x)
    - Rounding: round(x, n)
    - Power/Root: pow(x, y), math.sqrt(x)
    - Trig: math.sin(x), math.cos(x), math.tan(x)
    
    Example: 'math.sqrt(abs(-144)) + math.sin(math.radians(45))'
    """
    try:
        # A safe dictionary containing the tools you requested
        safe_dict = {
            "math": math,
            "abs": abs,
            "round": round,
            "pow": pow,
            "sum": sum,
            "min": min,
            "max": max
        }
        
        # Restricted evaluation for security
        result = eval(expression, {"__builtins__": None}, safe_dict)
        if isinstance(result, (int, float)):
            # 1e-15 is 0.000000000000001
            if abs(result) < 1e-15:
                result = 0.0
        
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
