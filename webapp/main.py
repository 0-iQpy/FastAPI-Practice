from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Set up Jinja2 template rendering
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # Pass dynamic data to the template
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Dynamic FastAPI Page"

                       }
        )
