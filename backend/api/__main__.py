# python -m api

import uvicorn

if __name__ == "__main__":
    uvicorn.run("backend.api.main:app", reload=True)
