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

from gtfs_pubsub.domain.model.gtfs.schedule.transfers import TransfersForeignData
import pytest

def test_TransfersForeignData_valid():
	t = TransfersForeignData(
		from_stop_id=123, to_stop_id=234, from_route_id=345, to_route_id=456,
		from_trip_id=678, to_trip_id=789, transfer_type=0, min_transfer_time=3
	)
	assert t is not None

def test_TransfersForeignData_missing_transfer_type():
	with pytest.raises(Exception) as e_info:
		t = TransfersForeignData(
			from_stop_id=123, to_stop_id=234, from_route_id=345, to_route_id=456,
			from_trip_id=678, to_trip_id=789, min_transfer_time=3
		)
