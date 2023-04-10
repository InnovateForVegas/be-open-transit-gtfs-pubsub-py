# Copyright (C) 2023 Innovate for Vegas Foundation
#
# This file is part of be-open-transit-gtfs-pubsub-py.
#
# be-open-transit-gtfs-pubsub-py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# be-open-transit-gtfs-pubsub-py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with be-open-transit-gtfs-pubsub-py.  If not, see <http://www.gnu.org/licenses/>.

from dataclasses import dataclass
from pydantic import BaseModel
from gtfs_pubsub.domain.model.gtfs.gtfs_types import ID, Latitude, Longitude, Integer, Float

class ShapesForeignData(BaseModel):
	shape_id: ID
	shape_pt_lat: Latitude
	shape_pt_lon: Longitude
	shape_pt_sequence: Integer
	shape_dist_traveled: Float | None

@dataclass
class ShapesData:
	shape_id: str
	shape_pt_lat: float
	shape_pt_lon: float
	shape_pt_sequence: int
	shape_dist_traveled: float
