from fastapi import FastAPI

app = FastAPI(title="security-log-collector")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
