from fastapi import FastAPI

# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from starlette.requests import Request
# from starlette.staticfiles import StaticFiles

app = FastAPI()


# Set up Jinja2 template rendering
# templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")
#
#
# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     # Pass dynamic data to the template
#     return templates.TemplateResponse(
#         "index.html", {"request": request, "title": "Dynamic FastAPI Page"
#
#                        }
#         )
#
#
# @app.get("/admin", response_class=HTMLResponse)
# async def read_item(request: Request):
#     # Pass dynamic data to the template
#     return templates.TemplateResponse(
#         "admin_page/admin_dashboard.html", {"request": request, "title": "Dynamic FastAPI Page"
#
#                                             }
#         )
@app.get("/")
async def check():
    return "ITS FINALLY WORKING"
