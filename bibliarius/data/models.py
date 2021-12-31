from typing import Literal

from pydantic import BaseModel


class HealthStatus(BaseModel):
    """
    Health Check Payload
    """

    status: Literal["HEALTHY", "FAILING"]
