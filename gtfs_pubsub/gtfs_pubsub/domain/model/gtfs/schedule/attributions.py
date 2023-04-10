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
from gtfs_pubsub.domain.model.gtfs.gtfs_types import ID, Text, Enum, Email, PhoneNumber

class AttributionsForeignData(BaseModel):
	attribution_id: ID | None
	agency_id: ID | None
	route_id: ID | None
	trip_id: ID | None
	organization_name: Text
	is_producer: Enum | None
	is_operator: Enum | None
	is_authority: Enum | None
	attribution_email: Email | None
	attribution_phone: PhoneNumber | None


@dataclass
class AttributionsData:
	attribution_id: str
	agency_id: str
	route_id: str
	trip_id: str
	organization_name: str
	is_producer: int
	is_operator: int
	is_authority: int
	attribution_email: str
	attribution_phone: str
