import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def hello():
    return 'hello jack'


def main():
    uvicorn.run(app=app, host='localhost', port=8282)


if __name__ == '__main__':
    main()
