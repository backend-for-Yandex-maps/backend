# app/exception/exception.py

from fastapi.responses import JSONResponse


class ExceptionHandler:
    @staticmethod
    def handle_exception(e):
        return JSONResponse(status_code=500, content={"message": str(e)})


class ExceptionNotFound:
    @staticmethod
    def handle_exception(e):
        return JSONResponse(status_code=404, content={"message": str(e)})
