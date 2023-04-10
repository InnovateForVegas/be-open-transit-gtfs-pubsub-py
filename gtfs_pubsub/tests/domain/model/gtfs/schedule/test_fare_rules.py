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

from gtfs_pubsub.domain.model.gtfs.schedule.fare_rules import FareRulesForeignData
import pytest

def test_FareRulesForeignData_valid():
	f = FareRulesForeignData(
		fare_id=123, route_id=234, origin_id=345, destination_id=345, contains_id=456
	)
	assert f is not None

def test_FareRulesForeignData_missing_fare_id():
	with pytest.raises(Exception) as e_info:
		f = FareRulesForeignData(
			route_id=234, origin_id=345, destination_id=345, contains_id=456
		)
