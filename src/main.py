from fastapi import FastAPI, HTTPException, Request
from presentation.api.task_controller import router
from fastapi.responses import JSONResponse
from presentation.responses.response import GeneralErrorResponse
from infrastructure.logging.logger import logger


app = FastAPI(title="Task Management System")
app.include_router(router)


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    logger.info(
        f"HTTPException caught: status_code={exc.status_code}, "
        f"detail={exc.detail}, "
        f"method={request.method}, path={request.url.path}"
    )

    err = GeneralErrorResponse(code=exc.status_code, message=exc.detail)
    return JSONResponse(status_code=exc.status_code, content=err.model_dump())
