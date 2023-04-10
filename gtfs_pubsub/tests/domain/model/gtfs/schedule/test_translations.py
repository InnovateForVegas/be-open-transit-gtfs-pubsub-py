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

from gtfs_pubsub.domain.model.gtfs.schedule.translations import TranslationsForeignData
import pytest

def test_TranslationsForeignData_valid():
	t = TranslationsForeignData(
		table_name=0, field_name="Field Name", language="en-US", translation="Translation Text",
		record_id=123, record_sub_id=234, field_value="Field Value"
	)
	assert t is not None

def test_TranslationsForeignData_missing_field_name():
	with pytest.raises(Exception) as e_info:
		t = TranslationsForeignData(
			table_name=0, language="en-US", translation="Translation Text",
			record_id=123, record_sub_id=234, field_value="Field Value"
		)
