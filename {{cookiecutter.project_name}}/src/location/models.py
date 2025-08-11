from pydantic import BaseModel
from typing import Tuple


class LocationCreate(BaseModel):
    name: str
    coordinates: Tuple[float, float]  # (longitude, latitude)

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "name": "Test Location",
    #             "coordinates": [12.9716, 77.5946]
    #         }
    #     }
