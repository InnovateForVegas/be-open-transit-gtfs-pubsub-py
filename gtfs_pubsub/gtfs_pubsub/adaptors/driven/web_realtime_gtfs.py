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

from gtfs_pubsub.domain.ports.driven.realtime_gtfs import RealtimeGtfs

from google.transit import gtfs_realtime_pb2
import urllib.request

class WebRealtimeGtfs(RealtimeGtfs):

	config = dict(realtime_url="http://rtcws.rtcsnv.com/gtfrt/tripUpdates.pb")

	def port_open(self):
		if self.config:
			self.feed = None
			self.response = None
			self.status = None

	def port_read(self):
		self.feed = gtfs_realtime_pb2.FeedMessage()
		self.response = urllib.request.urlopen(self.config.get("realtime_url"))
		self.feed.ParseFromString(self.response.read())

		return self.feed
#		for entity in feed.entity:
#			if entity.HasField('trip_update'):

	def port_write(self):
		pass

	def port_close(self):
		self.feed = None
		self.response = None
		self.status = None
