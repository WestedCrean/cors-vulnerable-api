import os
from fastapi import FastAPI, Request, Cookie
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger


app = FastAPI()

logger.info("Setting up CORS policy")

index = """<html>
<head>
    <title>Damn Vulerable Python Web App</title>
    <style>
        h1 {
            text-align: center;
            margin-top: 100px;
        }
        a {text-align: center;}

        form {
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Subscribe for our newsletter</h1>
    <a href="/items/1">A link</a>
    <form action="" method="post">
        <div>
            <label for="name">Enter your name: </label>
            <input type="text" name="name" id="name" required>
        </div>
        <div>
            <label for="email">Enter your email: </label>
            <input type="email" name="email" id="email" required>
        </div>
        <div class="submit-btn">
            <input type="submit" value="Subscribe!">
        </div>
    </form>
</body>
</html>"""

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".+",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
logger.info("CORS policy set up")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    logger.info(f"Request ORIGIN headers: {request.headers}")
    response = await call_next(request)
    logger.info(f"Response ACAO headers:")
    logger.info(request.headers)
    return response


@app.get("/", response_class=HTMLResponse)
def read_root(req: Request, cookie_value: str = Cookie(None)):
    return index


@app.post("/")
def with_auth(req: Request, cookie_value: str = Cookie("fastapi_cookie")):
    logger.info(req)
    response = JSONResponse(content={"msg": "cookie set"})
    response.set_cookie(key="fastapi_cookie", value="fake-cookie-session-value")
    return response


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
