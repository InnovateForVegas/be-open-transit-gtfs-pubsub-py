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
from gtfs_pubsub.domain.model.gtfs.gtfs_types import ID, Time, Integer, Text, Enum, Float


class StopTimesForeignData(BaseModel):
	trip_id: ID
	arrival_time: Time | None
	departure_time: Time | None
	stop_id: ID
	stop_sequence: Integer
	stop_headsign: Text | None
	pickup_type: Enum | None
	drop_off_type: Enum | None
	continuous_pickup: Enum | None
	continuous_drop_off: Enum | None
	shape_dist_traveled: Float | None
	timepoint: Enum | None

@dataclass
class StopTimesData:
	trip_id: str
	arrival_time: str
	departure_time: str
	stop_id: str
	stop_sequence: int
	stop_headsign: str
	pickup_type: int
	drop_off_type: int
	continuous_pickup: int
	continuous_drop_off: int
	shape_dist_traveled: float
	timepoint: int

