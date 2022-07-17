#! /usr/bin/python3
import _thread
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s :: %(module)s :: %(levelname)s :: %(message)s")
import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import ui

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return ui.root()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run(app, host="127.0.0.1", port=port)