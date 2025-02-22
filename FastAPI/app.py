import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse



app = FastAPI()

@app.get("/start")
def start():
    # return JSONResponse({"message": "Hello World"}, status_code=200)
    # return HTMLResponse("<h1 style='color: red;'>Hello world!</h1>")
    return FileResponse("pages/index_1.html")


@app.post("/post")
def post():
    return JSONResponse({"message": "Hello World"}, status_code=200)




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)