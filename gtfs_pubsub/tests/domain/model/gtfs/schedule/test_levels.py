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

from gtfs_pubsub.domain.model.gtfs.schedule.levels import LevelsForeignData
import pytest

def test_LevelsForeignData_valid():
	l = LevelsForeignData(
		level_id=123, level_index=1.23, level_name="Level Name"
	)
	assert l is not None

def test_LevelForeignData_missing_level_id():
	with pytest.raises(Exception) as e_info:
		l = LevelsForeignData(
			level_index=1.23, level_name="Level Name"
		)
