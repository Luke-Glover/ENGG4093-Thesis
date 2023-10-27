from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import PlainTextResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="webapp/static"), name="webapp")


@app.get("/api/generate", response_class=PlainTextResponse)
def generate():
    from Pensieve.old.generate import generate
    questions = generate()
    return questions


def create_app():
    return app
