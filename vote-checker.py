from dotenv import load_dotenv
from pyzeebe import ZeebeWorker, create_camunda_cloud_channel
import os
import asyncio

load_dotenv()

# Get the Zeebe connection details from the environment variables
client_id = os.getenv('ZEEBE_CLIENT_ID')
client_secret = os.getenv('ZEEBE_CLIENT_SECRET')
cluster_id = os.getenv('ZEEBE_CLUSTER_ID')

channel = create_camunda_cloud_channel(client_id, 
                                       client_secret, 
                                       cluster_id)

worker = ZeebeWorker(channel)

@worker.task(task_type="check-database", single_value=True, variable_name="id_valid")
async def check_database(id: str):
    print(f"Checking database for id {id}")
    return True

if __name__ == "__main__":
    loop = asyncio.get_running_loop()
    loop.run_until_complete(worker.work())