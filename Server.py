from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
import uvicorn
import asyncio
import main  # This imports your CLI tool logic from main.py

app = FastAPI()

# Mount the 'frontend' directory to serve static files (the GUI)
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

@app.get("/api")
def home():
    return {"message": "Welcome to the Web Version of the AI Tool!"}

@app.post("/api/run")
async def run_tool(request: Request):
    data = await request.json()
    user_input = data.get("input", "")

    # Call your existing tool's logic. 
    # Here, we assume run_controller is an async function in main.py that processes the task.
    result = await main.run_controller(
        config=main.AppConfig(),  # Create a default configuration
        initial_user_action=main.MessageAction(content=user_input)
    )

    return {"result": str(result)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
