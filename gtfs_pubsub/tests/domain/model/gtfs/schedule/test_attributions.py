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

from gtfs_pubsub.domain.model.gtfs.schedule.attributions import AttributionsForeignData
import pytest

def test_AttributionsForeignData_valid():
		a = AttributionsForeignData (
			attribution_id=123, agency_id=234, route_id=345, trip_id=456,
			organization_name="Org Name", is_producer=1, is_operator=1, is_authority=1,
			attribution_email="test@example.com", attribution_phone="702-555-1212"
		)
		assert a is not None

def test_AttributionsForeignData_missing_organization_name():
	with pytest.raises(Exception) as e_info:
		a = AttributionsForeignData (
			attribution_id=123, agency_id=234, route_id=345, trip_id=456,
			is_producer=1, is_operator=1, is_authority=1,
			attribution_email="test@example.com", attribution_phone="702-555-1212"
		)
