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
from gtfs_pubsub.domain.model.gtfs.gtfs_types import ID, Text, Url, Timezone, LanguageCode, PhoneNumber, Email

class AgencyForeignData(BaseModel):
	agency_id: ID | None
	agency_name: Text
	agency_url: Url
	agency_timezone: Timezone
	agency_lang: LanguageCode | None
	agency_phone: PhoneNumber | None
	agency_fare_url: Url | None
	agency_email: Email | None


@dataclass
class AgencyData:

	agency_id: str | None
	agency_name: str
	agency_url: str
	agency_timezone: str
	agency_lang: str | None
	agency_phone: str | None
	agency_fare_url: str | None
	agency_email: str | None
