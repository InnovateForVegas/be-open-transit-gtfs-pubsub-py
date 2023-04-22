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

from gtfs_pubsub.domain.ports.driven.schedule_gtfs import ScheduleGtfs

import urllib.request
import zipfile


class WebScheduleGtfs(ScheduleGtfs):

	config = dict(zipfile_url = "http://rtcws.rtcsnv.com/g/google_transit.zip")

	def port_open(self):
		if self.config:
			self.feed = None
			self.response = None
			self.status = None

	def port_read(self, param:dict) -> None:
		self.response = urllib.request.urlopen('http://rtcws.rtcsnv.com/gtfrt/tripUpdates.pb')
		self.feed.ParseFromString(self.response.read())

		return self.feed
#		for entity in feed.entity:
#			if entity.HasField('trip_update'):

	def port_write(self, param:dict) -> None:
		pass

	def port_close(self):
		self.feed = None
		self.response = None
		self.status = None

	def _get_zipfile(self):
		schedule_zipfile_loc = urllib.request.urlopen(self.config.get("zipfile_url"))
		schedule_zipfile = None
