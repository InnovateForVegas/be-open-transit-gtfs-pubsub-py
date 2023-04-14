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

from gtfs_pubsub.domain.model.gtfs.gtfs_types import CauseEnum, EffectEnum, SeverityLevelEnum

from gtfs_pubsub.domain.model.gtfs.realtime.time_range import TimeRangeForeignData
from gtfs_pubsub.domain.model.gtfs.realtime.entity_selector import EntitySelectorForeignData
from gtfs_pubsub.domain.model.gtfs.realtime.translated_string import TranslatedStringForeignData
from gtfs_pubsub.domain.model.gtfs.realtime.translated_image import TranslatedImageForeignData


class AlertForeignData(BaseModel):
	active_period: TimeRangeForeignData | None
	informed_entity: EntitySelectorForeignData | None
	cause: CauseEnum | None
	cause_detail: TranslatedStringForeignData | None
	effect: EffectEnum | None
	effect_detail: TranslatedStringForeignData | None
	url: TranslatedStringForeignData | None
	header_text: TranslatedStringForeignData
	description_text: TranslatedStringForeignData
	tts_header_text: TranslatedStringForeignData | None
	tts_description_text: TranslatedStringForeignData | None
	severity_level: SeverityLevelEnum | None
	image: TranslatedImageForeignData | None
	image_alternative_text: TranslatedStringForeignData | None
