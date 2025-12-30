from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import string
import random

from schemas import UrlInput
import repository

app = FastAPI(title="URL Shortener")

repository.init_storage()


def generate_code(length: int = 6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


@app.post("/shorten")
def shorten_url(data: UrlInput):
    code = generate_code()
    repository.save_link(code, data.url)
    return {"short_url": f"http://localhost:8000/{code}"}


@app.get("/{code}")
def redirect(code: str):
    url = repository.fetch_link(code)
    if not url:
        raise HTTPException(status_code=404, detail="Link not found")
    return RedirectResponse(url)


@app.get("/stats/{code}")
def stats(code: str):
    url = repository.fetch_link(code)
    if not url:
        raise HTTPException(status_code=404)
    return {"code": code, "original_url": url}
