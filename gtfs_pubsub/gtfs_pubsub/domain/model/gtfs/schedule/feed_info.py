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
from gtfs_pubsub.domain.model.gtfs.gtfs_types import Text, Url, LanguageCode, Date, Email

class FeedInfoForeignData(BaseModel):
	feed_publisher_name: Text
	feed_publisher_url: Url
	feed_lang: LanguageCode
	default_lang: LanguageCode | None
	feed_start_date: Date | None
	feed_end_date: Date | None
	feed_version: Text | None
	feed_contact_email: Email | None
	feed_contact_url: Url | None

@dataclass
class FeedInfoData:
	feed_publisher_name: str
	feed_publisher_url: str
	feed_lang: str
	default_lang: str
	feed_start_date: str
	feed_end_date: str
	feed_version: str
	feed_contact_email: str
	feed_contact_url: str
