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

from gtfs_pubsub.domain.model.gtfs.gtfs_types import Integer

from gtfs_pubsub.domain.model.gtfs.realtime.trip_descriptor import TripDescriptorForeignData
from gtfs_pubsub.domain.model.gtfs.realtime.vehicle_descriptor import VehicleDescriptorForeignData
from gtfs_pubsub.domain.model.gtfs.realtime.stop_time_update import StopTimeUpdateForeignData
from gtfs_pubsub.domain.model.gtfs.realtime.trip_properties import TripPropertiesForeignData

class TripUpdateForeignData(BaseModel):
	trip: TripDescriptorForeignData
	vehicle: VehicleDescriptorForeignData | None
	stop_time_update: StopTimeUpdateForeignData | None
	timestamp: Integer | None
	delay: Integer | None
	trip_properties: TripPropertiesForeignData | None

