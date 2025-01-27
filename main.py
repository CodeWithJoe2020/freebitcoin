from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()
import os

password = os.getenv('FREEBTC')
email = 'your email'
website = 'http://getfreebtc.lol'

async def main():
    while True:  # This will create an infinite loop
        agent = Agent(
            task=f"Go to ({website} and log in with this {email} and use the Password from {password},close those pop up windows, by clicking on 'no thanks' , once you logged in click on the  'verify human' button and than click 'ROLL withut verification' button, once this was succesfull, close the browser window",
            llm=ChatOpenAI(model="gpt-4o"),
        )
        result = await agent.run()
        print(result)
        
        # Wait for 61 minutes before repeating
        await asyncio.sleep(3660)  # 61 minutes in seconds

asyncio.run(main())
