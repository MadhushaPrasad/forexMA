import asyncio

import logging

from agent import Agent

log = logging.getLogger(Agent.Decision_Agent)


def print(*args, **kwargs):
    log.info(f"{args=}")


class DecisionAgent:
    publish = None
    display = None

    def __init__(self, *args, **kwargs):
        log.info(f"{self} Start")

    async def start(self):
        # await self.publish("AgentTwo", "Hi Agent 2")
        pass

    async def accept_message(self, agent, message):
        print(f"{agent=},{message=}")

    async def stop(self, *args, **kwargs):
        pass

    async def execute(self, *args, **kwargs):
        pass
        # while True:
        #     print("run")
        #     # await self.publish("AgentTwo", "Hello AGENT 2")
        #     await asyncio.sleep(2)
