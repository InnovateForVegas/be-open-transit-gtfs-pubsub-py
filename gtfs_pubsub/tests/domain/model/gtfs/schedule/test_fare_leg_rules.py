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

from gtfs_pubsub.domain.model.gtfs.schedule.fare_leg_rules import FareLegRulesForeignData
import pytest

def test_FareLegRulesForeignData_valid():
	f = FareLegRulesForeignData(
		leg_group_id=123, network_id=234, from_area_id=345, to_area_id=456, fare_product_id=1
	)
	assert f is not None

def test_FareLegRulesForeignData_missing_fare_product_id():
	with pytest.raises(Exception) as e_info:
		f = FareLegRulesForeignData(
			leg_group_id=123, network_id=234, from_area_id=345, to_area_id=456
		)
