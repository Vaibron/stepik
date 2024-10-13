import uvicorn
from fastapi import FastAPI

from routers import api_router, auth_router, user_router, course_router, admin_router


app = FastAPI()

app.include_router(api_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(course_router)
app.include_router(admin_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
