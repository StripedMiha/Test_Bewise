import time

import uvicorn as uvicorn
from fastapi import FastAPI
from routers.questions import router as router_questions
from db.tables import init_db

app = FastAPI()
app.include_router(router_questions)


@app.on_event("startup")
async def on_startup():
    try:
        init_db()
    except:
        pass

if __name__ == "__main__":
    time.sleep(3)
    uvicorn.run(app, host="0.0.0.0", port=4000, debug='true')
