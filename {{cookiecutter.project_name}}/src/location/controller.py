import logging
from typing import Annotated
from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from starlette import status
from . import models
from . import service
from ..database.core import DbSession, get_db
from ..entities.location import Location
from ..rate_limiter import limiter
from geoalchemy2.shape import from_shape
from shapely.geometry import Point

router = APIRouter(prefix="/location", tags=["location"])


@router.post("/create/")
async def create_location(location: models.LocationCreate, db=Depends(get_db)):
    point = from_shape(Point(location.coordinates), srid=4326)
    db_location = Location(name=location.name, geom=point)
    db.add(db_location)
    db.commit()
    logging.info(f"Successfully location created")
    return JSONResponse(
        content={"id": db_location.id, "name": db_location.name}, status_code=201
    )
