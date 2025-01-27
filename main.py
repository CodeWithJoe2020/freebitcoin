from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()
import os

password = os.getenv('FREEBTC')
email = ''

async def main():
    while True:  # This will create an infinite loop
        agent = Agent(
            task=f"Go to  getfreebtc.lol  ('https:// getfreebtc.lol'),close those pop up windows and log in with this (your-email) and use the Password from {password} , once you logged in click on the 'ROLL' button, once this was succesfull, close the browser window",
            llm=ChatOpenAI(model="gpt-4o"),
        )
        result = await agent.run()
        print(result)
        
        # Wait for 61 minutes before repeating
        await asyncio.sleep(3660)  # 61 minutes in seconds

asyncio.run(main())
