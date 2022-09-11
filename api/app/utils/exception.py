from ..app import app
from fastapi import Request
from fastapi.responses import JSONResponse

class InitializationException(Exception):
    pass

class GenerationException(Exception):
    pass

@app.exception_handler(Exception)
async def unknown_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={'message': 'Internal error.'})

@app.exception_handler(InitializationException)
async def initialization_exception_handler(request: Request, exc: InitializationException):
    return JSONResponse(status_code=400, content={'message': 'Initialization error.'})

@app.exception_handler(GenerationException)
async def generation_exception_handler(request: Request, exc: GenerationException):
    return JSONResponse(status_code=400, content={'message': 'Failed to generate music.'})
