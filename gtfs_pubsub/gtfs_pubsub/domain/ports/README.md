<!--
 Copyright (C) 2023 Innovate for Vegas Foundation
 
 This file is part of be-open-transit-gtfs-pubsub-py.
 
 be-open-transit-gtfs-pubsub-py is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 be-open-transit-gtfs-pubsub-py is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with be-open-transit-gtfs-pubsub-py.  If not, see <http://www.gnu.org/licenses/>.
-->

# Domain Port Interfaces

How to communicate with the domain, through interface definitions.

Adaptors are outside of the domain, inside the hex, as implementations of the domain ports.

External driving or incoming communications take place as though each is passing through a port, through an adaptor.

Similarly, when the domain or the hex in general conducts driven outgoing communications with other services (database is a common example)

Thus, ports are abstract interfaces, adaptors are concrete implementations.
