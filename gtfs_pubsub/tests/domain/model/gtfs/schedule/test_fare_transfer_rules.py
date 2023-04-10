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

from gtfs_pubsub.domain.model.gtfs.schedule.fare_transfer_rules import FareTransferRulesForeignData
import pytest

def test_FareTransferRulesForeignData_valid():
	f = FareTransferRulesForeignData(
		from_leg_group=123, to_leg_group_id=234, transfer_count=3, duration_limit=1, duration_limit_type=1,
		fare_transfer_type=1, fare_product_id=999
	)
	assert f is not None

def test_FareTransferRuelsForeignData_missing_fare_product_id():
	with pytest.raises(Exception) as e_info:
		f = FareTransferRulesForeignData(
			from_leg_group=123, to_leg_group_id=234, transfer_count=3, duration_limit=1, duration_limit_type=1,
			fare_transfer_type=1
		)
