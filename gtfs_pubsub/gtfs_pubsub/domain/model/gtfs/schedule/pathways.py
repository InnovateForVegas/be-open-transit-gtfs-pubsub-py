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
from gtfs_pubsub.domain.model.gtfs.gtfs_types import ID, Enum, Float, Integer, Text

class PathwaysForeignData(BaseModel):
	pathway_id: ID
	from_stop_id: ID
	to_stop_id: ID
	pathway_mode: Enum
	is_bidirectional: Enum
	length: Float | None
	traversal_time: Integer | None
	stair_count: Integer | None
	max_slope: Float | None
	min_width: Float | None
	signposted_as: Text | None
	reversed_signposted_as: Text | None

@dataclass
class PathwaysData:
	pathway_id: str
	from_stop_id: str
	to_stop_id: str
	pathway_mode: int
	is_bidirectional: int
	length: float
	traversal_time: int
	stair_count: int
	max_slope: float
	min_width: float
	signposted_as: str
	reversed_signposted_as: str
