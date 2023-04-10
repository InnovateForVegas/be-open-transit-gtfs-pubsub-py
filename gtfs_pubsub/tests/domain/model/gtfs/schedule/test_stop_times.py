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

from gtfs_pubsub.domain.model.gtfs.schedule.stop_times import StopTimesForeignData
import pytest

def test_StopTimesForeignData_valid():
	s = StopTimesForeignData(
		trip_id=123, arrival_time="12:00:00", departure_time="12:00:01", stop_id=234, stop_sequence=3,
		stop_headsign="Headsign", pickup_type=0, drop_off_type=1, continuous_pickup=0, continuous_drop_off=1,
		shape_dist_traveled=34.56, timepoint=0
	)
	assert s is not None

def test_StopTimesForeignData_missing_stop_id():
	with pytest.raises(Exception) as e_info:
		s = StopTimesForeignData(
			trip_id=123, arrival_time="12:00:00", departure_time="12:00:01", stop_sequence=3,
			stop_headsign="Headsign", pickup_type=0, drop_off_type=1, continuous_pickup=0, continuous_drop_off=1,
			shape_dist_traveled=34.56, timepoint=0
		)
