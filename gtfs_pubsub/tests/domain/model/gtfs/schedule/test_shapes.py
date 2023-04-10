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

from gtfs_pubsub.domain.model.gtfs.schedule.shapes import ShapesForeignData
import pytest

def test_ShapesForeignData_valid():
	s = ShapesForeignData(
		shape_id=123, shape_pt_lat=34.56, shape_pt_lon=45.65, shape_pt_sequence=3, shape_dist_traveled=34.56
	)
	assert s is not None

def test_ShapesForeignData_missing_shape_id():
	with pytest.raises(Exception) as e_info:
		s = ShapesForeignData(
			shape_pt_lat=34.56, shape_pt_lon=45.65, shape_pt_sequence=3, shape_dist_traveled=34.56
		)
