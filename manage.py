from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi_directory_routing import DirectoryRouter
from utils.environments import Environment
import os


load_dotenv()

title = os.getenv('APP_TITLE', 'ScannerAPI')
root_path = os.getenv('APP_PREFIX', '')

app = FastAPI(
        title = title,
        root_path = root_path,
        openapi_prefix = root_path
    )

env = os.getenv('ENVIRONMENT', Environment.DEV)
# Disable open API if PROD
if env == Environment.PROD:
    app.openapi = None

allow_origins = ['*']
allow_methods = ['*']
allow_headers = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Router based on directory
api_routers = DirectoryRouter(base_directory='routes')
app.include_router(router=api_routers)
