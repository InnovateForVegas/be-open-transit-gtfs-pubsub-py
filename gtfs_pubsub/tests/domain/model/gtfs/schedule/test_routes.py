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

from gtfs_pubsub.domain.model.gtfs.schedule.routes import RoutesForeignData
import pytest

def test_RoutesForeignData_valid():
	r = RoutesForeignData(
		route_id=123, agency_id=234, route_short_name="Short Name", route_long_name="Long Name", route_desc="Route Description",
		route_type=1, route_url="http://example.com", route_color="000000", route_text_color="FFFFFF", route_sort_order=2,
		continuous_pickup=1, continuous_drop_off=1, network_id=456
	)
	assert r is not None

def test_RoutesForeignData_missing_route_id():
	with pytest.raises(Exception) as e_info:
		r = RoutesForeignData(
			agency_id=234, route_short_name="Short Name", route_long_name="Long Name", route_desc="Route Description",
			route_type=1, route_url="http://example.com", route_color="000000", route_text_color="FFFFFF", route_sort_order=2,
			continuous_pickup=1, continuous_drop_off=1, network_id=456
		)
