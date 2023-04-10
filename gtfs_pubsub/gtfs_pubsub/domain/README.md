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

# Domain of this hexagonal system

This is where the business logic of this hexagon lives.

There should be as little external code as possible inside the domain.

This does not mean there can be no standard modules and libraries, it does mean that the domain becomes less isolated as it depends on more external code.
