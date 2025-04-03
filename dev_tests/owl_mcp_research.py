import asyncio
import sys
from typing import Any, Dict, List, Tuple

from camel.models import ModelFactory
from camel.toolkits import MCPToolkit
from camel.types import ModelPlatformType, ModelType
from camel.societies import RolePlaying
from camel.logger import set_log_level

from owl.utils.enhanced_role_playing import arun_society

set_log_level(level="DEBUG")

async def main() -> None:
    """
    Main function to run the MCP research task.
    """
    # Initialize MCP toolkit and connect
    mcp_toolkit = MCPToolkit(config_path="examples/mcp_servers_config.json")

    try:
        await mcp_toolkit.connect()

        # Get task from command line or use default
        task = sys.argv[1] if len(sys.argv) > 1 else (
            "Using a web browser, search Google Scholar for Andrew Ng's academic profile. Create a comprehensive report that includes: (1) his main research directions in AI and machine learning, (2) at least five of his most influential published papers with citation counts, (3) his affiliated institutions throughout his career, and (4) a summary of his impact on the field."
        )

        # Setup model
        model = ModelFactory.create(
            model_platform=ModelPlatformType.GEMINI,
            model_type="gemini-1.5-flash-latest",
        )

        # Create and run society
        society = RolePlaying(
            task_prompt=task,
            user_role_name="user",
            user_agent_kwargs={"model": model},
            assistant_role_name="assistant",
            assistant_agent_kwargs={
                "model": model,
                "tools": mcp_toolkit.get_tools(),
            },
            task_specify_agent_kwargs={"model": model},
        )

        answer, chat_history, token_count = await arun_society(society)
        print(f"\033[94mAnswer: {answer}\033[0m")

    finally:
        try:
            await mcp_toolkit.disconnect()
        except Exception:
            print("Disconnect failed")

if __name__ == "__main__":
    asyncio.run(main())
