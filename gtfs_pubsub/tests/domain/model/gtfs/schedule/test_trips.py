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

from gtfs_pubsub.domain.model.gtfs.schedule.trips import TripsForeignData
import pytest

def test_TripsForeignData_valid():
	t = TripsForeignData(
		route_id=123, service_id=234, trip_id=345, trip_short_name="Short Name", direction_id=1,
		block_id=567, shape_id=678, wheelchair_accessible=2, bikes_allowed=1
	)
	assert t is not None

def test_TripsForeignData_missing_trip_id():
	with pytest.raises(Exception) as e_info:
		t = TripsForeignData(
			route_id=123, service_id=234, trip_short_name="Short Name", direction_id=1,
			block_id=567, shape_id=678, wheelchair_accessible=2, bikes_allowed=1
		)
