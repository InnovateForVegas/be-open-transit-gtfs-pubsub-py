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

from gtfs_pubsub.domain.model.gtfs.schedule.feed_info import FeedInfoForeignData
import pytest

def test_FeedInfoForeignData_valid():
	f = FeedInfoForeignData(
		feed_publisher_name="Publisher Name", feed_publisher_url="https://example.com", feed_lang="en-US", default_lang="en-US",
		feed_start_date="20230101", feed_end_date="20231231", feed_version="Feed Version",
		feed_contact_email="feed@example.com", feed_contact_url="http://feed.example.com"
	)
	assert f is not None

def test_FeedInfoForeignData_missing_feed_publisher_name():
	with pytest.raises(Exception) as e_info:
		f = FeedInfoForeignData(
			feed_publisher_url="https://example.com", feed_lang="en-US", default_lang="en-US",
			feed_start_date="20230101", feed_end_date="20231231", feed_version="Feed Version",
			feed_contact_email="feed@example.com", feed_contact_url="http://feed.example.com"
		)
