import asyncio
import os
import sys
from typing import Any, Dict, List, Tuple

from dotenv import load_dotenv
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
    # Load environment variables from .env file
    load_dotenv()
    # Initialize MCP toolkit and connect
    mcp_toolkit = MCPToolkit(config_path="examples/mcp_servers_config.json")

    try:
        await mcp_toolkit.connect()

        # Get task from command line or use default
        task = sys.argv[1] if len(sys.argv) > 1 else (
            "Using a web browser, search Google Scholar for Andrew Ng's academic profile. Create a comprehensive report that includes: (1) his main research directions in AI and machine learning, (2) at least five of his most influential published papers with citation counts, (3) his affiliated institutions throughout his career, and (4) a summary of his impact on the field."
        )

        # Setup model
        # Ensure the required environment variables are set
        pixtral_model_id = os.getenv("PIXTRAL_MODEL_ID")
        pixtral_api_key = os.getenv("PIXTRAL_API_KEY") # Optional, remove if not needed
        pixtral_url = os.getenv("PIXTRAL_URL")

        if not pixtral_model_id or not pixtral_url:
            raise ValueError("Please set the PIXTRAL_MODEL_ID and PIXTRAL_URL environment variables.")
            # If API key is mandatory, add: or not pixtral_api_key

        model = ModelFactory.create(
            model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
            model_type=pixtral_model_id,
            model_config_dict={},
            api_key=pixtral_api_key,
            url=pixtral_url
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
