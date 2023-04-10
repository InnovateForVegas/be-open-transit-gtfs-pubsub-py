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
from gtfs_pubsub.domain.model.gtfs.gtfs_types import ID, Enum, Text, LanguageCode, Email, PhoneNumber, Url

class TranslationsForeignData(BaseModel):
	table_name: Enum
	field_name: Text
	language: LanguageCode
	translation: Text | Url | Email | PhoneNumber
	record_id: ID | None
	record_sub_id: ID | None
	field_value: Text | Url | Email | PhoneNumber

@dataclass
class TranslationsData:
	table_name: int
	field_name: str
	language: str
	translation: str
	record_id: str
	record_sub_id: str
	field_value: str
