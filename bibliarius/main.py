from fastapi import FastAPI

from bibliarius.data.models import HealthStatus

APP = FastAPI()


@APP.get("/healthz")
async def healthcheck() -> HealthStatus:
    """
    App Health Check
    """

    return HealthStatus(status="HEALTHY")
