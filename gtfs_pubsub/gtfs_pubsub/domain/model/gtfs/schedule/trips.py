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
from gtfs_pubsub.domain.model.gtfs.gtfs_types import ID, Enum, Text

class TripsForeignData(BaseModel):
	route_id: ID
	service_id: ID
	trip_id: ID
	trip_headsign: Text | None
	trip_short_name: Text | None
	direction_id: Enum | None
	block_id: ID | None
	shape_id: ID | None
	wheelchair_accessible: Enum | None
	bikes_allowed: Enum | None


@dataclass
class TripsData:
	route_id: str
	service_id: str
	trip_id: str
	trip_headsign: str
	trip_short_name: str
	direction_id: int
	block_id: str
	shape_id: str
	wheelchair_accessible: int
	bikes_allowed: int

