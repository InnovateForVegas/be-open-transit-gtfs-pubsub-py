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

from gtfs_pubsub.domain.model.gtfs.gtfs_types import Text, Boolean

from gtfs_pubsub.domain.model.gtfs.realtime.vehicle_position import VehiclePositionForeignData
from gtfs_pubsub.domain.model.gtfs.realtime.trip_update import TripUpdateForeignData
from gtfs_pubsub.domain.model.gtfs.realtime.alert import AlertForeignData
from gtfs_pubsub.domain.model.gtfs.realtime.shape import ShapeForeignData

class FeedEntityForeignData(BaseModel):
	id: Text
	is_deleted: Boolean | None
	trip_update: TripUpdateForeignData | None
	vehicle: VehiclePositionForeignData | None
	alert: AlertForeignData | None
	shape: ShapeForeignData | None
