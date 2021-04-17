from fastapi import FastAPI

import os

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

print(os.environ['USERNAME'])
print(os.environ['PASSWORD'])


