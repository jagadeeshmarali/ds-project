from aiohttp import ClientSession
from loguru import logger
from dataclasses import dataclass
from typing import Optional, Any
from uuid import UUID, uuid4

@dataclass
class DataServiceClient:
    DATASERVICE_BASE_URL: str
    @property
    def headers(self) -> dict:
        return {}

    async def create_empty_job(
        self,client: ClientSession, description:str, estimated_time:float,job_name:str,user_id:str
    ) -> str:
        payload = {
            "id":str(uuid4()),
            "description": description,
            "estimated_time": estimated_time,
            "status": "unknown",
            "name": job_name,
            "user_id": user_id
        }
        url = f"{self.DATASERVICE_BASE_URL}/job/"
        async with client.post(url=url, json=payload, headers=self.headers) as resp:
            resp_json = await resp.json()
            logger.info(f"{resp_json=}")
            return str(resp_json["id"])
        
    async def update_job(self,client: ClientSession,job_id:str,payload:Optional[Any])->Optional[Any]:
      url = f"{self.DATASERVICE_BASE_URL}/job/{job_id}"
      async with client.put(url=url, json=payload, headers=self.headers) as resp:
            resp_json = await resp.json()
            logger.info(f"{resp_json=}")
            return resp_json