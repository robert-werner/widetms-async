from fastapi import FastAPI

app = FastAPI(title="WideTMS",
              description="The TMS server with wider possibilities",
              version=open('VERSION', 'r').read())