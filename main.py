from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader

#app = FastAPI()


api_key_header = APIKeyHeader(name="Authorization", auto_error=True)

def verify_token(auth_header: str = Depends(api_key_header)):
    if auth_header != "expected_token":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid authentication token",
        )


app = FastAPI(
    title="test-fastapi",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "todos",
            "description": "タスク管理に関する操作。",
        },
        {
            "name": "users",
            "description": "ユーザー管理に関する操作。",
        },
    ],
    dependencies=[Depends(verify_token)],
)


@app.get("/")
async def get_hello():
    return {"message": "Hello World"}
