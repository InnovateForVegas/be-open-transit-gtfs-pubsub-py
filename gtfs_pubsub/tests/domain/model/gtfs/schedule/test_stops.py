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

from gtfs_pubsub.domain.model.gtfs.schedule.stops import StopsForeignData
import pytest


def test_StopsForeignData_valid():
	s = StopsForeignData(
		stop_id=123, stop_code="StopCode", stop_name="Stop Name", tts_stop_name="Say StopName",
		stop_desc="Stop Description", stop_lat=45.0, stop_lon=45.0, zone_id=123, stop_url="https://example.com",
		location_type=1, parent_station=1, stop_timezone="America/Los Angeles", wheelchair_boarding=1,
		level_id=123, platform_code="Platform Code"
	)
	assert s is not None

def test_StopsForeignData_missing_stop_id():
	with pytest.raises(Exception) as e_info:
		s = StopsForeignData(
			stop_code="StopCode", stop_name="Stop Name", tts_stop_name="Say StopName",
			stop_desc="Stop Description", stop_lat=45.0, stop_lon=45.0, zone_id=123, stop_url="https://example.com",
			location_type=1, parent_station=1, stop_timezone="America/Los Angeles", wheelchair_boarding=1,
			level_id=123, platform_code="Platform Code"
		)
