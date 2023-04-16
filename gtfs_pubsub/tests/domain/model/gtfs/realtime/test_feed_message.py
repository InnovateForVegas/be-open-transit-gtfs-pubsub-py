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

from gtfs_pubsub.domain.model.gtfs.realtime.feed_message import FeedMessageForeignData
from gtfs_pubsub.domain.model.gtfs.realtime.feed_header import FeedHeaderForeignData
from gtfs_pubsub.domain.model.gtfs.realtime.feed_entity import FeedEntityForeignData
import pytest

def test_FeedMessageForeignData_valid_minimum():
  fe = FeedEntityForeignData(id="1234")
  fh = FeedHeaderForeignData(gtfs_realtime_version="Version String", incrementality="FULL_DATASET", timestamp="123456")
  f = FeedMessageForeignData(header=fh, entity=fe)
  assert f is not None
