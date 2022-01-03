from os import environ

from fastapi import FastAPI

from bibliarius.logging import get_logger
from bibliarius.routers.models import HealthStatus
from bibliarius.data.sql import verify_db_connection

APP = FastAPI(
    title="bibliarius",
    debug=environ.get("DEBUGGING", "false").lower() == "true",
)
_LOGGER = get_logger(__name__)


@APP.get("/healthz")
def healthcheck() -> HealthStatus:
    """
    App Health Check
    """

    # Run status checks concurrently
    status_checks = (verify_db_connection(),)

    if all(status_checks):
        _LOGGER.debug("Successful Health Check")
        return HealthStatus(status="HEALTHY")

    _LOGGER.debug("Failed Health Check!")
    return HealthStatus(status="FAILING")
