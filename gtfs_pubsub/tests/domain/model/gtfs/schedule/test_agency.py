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

from gtfs_pubsub.domain.model.gtfs.schedule.agency import AgencyForeignData
import pytest

def test_AgencyForeignData_valid():
	a = AgencyForeignData(
		agency_id=123, agency_name="Agency Name", agency_url="https://example.com", agency_timezone="America/Los Angeles",
		agency_lang="en-US", agency_phone="702-555-1212", agency_fare_url="https://example.com", agency_email="agency@example.com"
	)
	assert a is not None

def test_AgencyForeignData_missing_agency_name():
	with pytest.raises(Exception) as e_info:
		a = AgencyForeignData(
			agency_id=123, agency_url="https://example.com", agency_timezone="America/Los Angeles",
			agency_lang="en-US", agency_phone="702-555-1212", agency_fare_url="https://example.com", agency_email="agency@example.com"
		)
