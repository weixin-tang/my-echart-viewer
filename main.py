from fastapi import FastAPI, HTTPException , Request
from fastapi.middleware.cors import CORSMiddleware
import httpx
import uvicorn
from typing import Optional
from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import json

app = FastAPI()

# 添加CORS中间件，允许前端与后端通信
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境下应该指定确切的源，而不是"*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up the template directory
templates = Jinja2Templates(directory="templates")

@app.get("/echart-render", response_class=HTMLResponse)
async def get_index(request: Request, dataUrl: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(dataUrl)
        response.raise_for_status()  # 如果响应状态码是4xx/5xx，抛出异常
        echart_data = response.json()
        echart_data_str = json.dumps(echart_data, indent=4)
        print( json.dumps(echart_data , indent=4) , type(echart_data))
    
    return templates.TemplateResponse("index.html", {"request": request, "echart_data": echart_data_str })

# 添加一个新的API端点，直接返回JSON数据
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8091, reload=True)