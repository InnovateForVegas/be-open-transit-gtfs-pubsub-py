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
from gtfs_pubsub.domain.model.gtfs.gtfs_types import ID, Text, Latitude, Longitude, Url, Enum, Timezone

class StopsForeignData(BaseModel):
	stop_id: ID
	stop_code: Text | None
	stop_name: Text | None
	tts_stop_name: Text | None
	stop_desc: Text | None
	stop_lat: Latitude | None
	stop_lon: Longitude | None
	zone_id: ID | None
	stop_url: Url | None
	location_type: Enum | None
	parent_station: ID | None
	stop_timezone: Timezone | None
	wheelchair_boarding: Enum | None
	level_id: ID | None
	platform_code: Text | None


@dataclass
class StopsData:
	stop_id: str
	stop_code: str
	stop_name: str
	tts_stop_name: str
	stop_desc: str
	stop_lat: float
	stop_lon: float
	zone_id: str
	stop_url: str
	location_type: int
	parent_station: str
	stop_timezone: str
	wheelchair_boarding: int
	level_id: str
	platform_code: str

