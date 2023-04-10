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


# GTFS Types and per-type comments/examples taken from https://gtfs.org/schedule/reference/#field-types


import re
import decimal
from isocodes import currencies
from dateutil.parser import parse
import datetime
import dateutil.tz
from bcp47 import bcp47
import phonenumbers
from urllib.parse import urlparse



class Color(str):

	"""
	A color encoded as a six-digit hexadecimal number. Refer to https://htmlcolorcodes.com to generate a valid value (the leading "#" must not be included).
	Example: FFFFFF for white, 000000 for black or 0039A6 for the A,C,E lines in NYMTA.
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, str):
			raise TypeError('string required')

		m = re.findall(r'[0-9a-fA-F]{6}', v)

		if len(m) != 1:
			raise ValueError('invalid Color value')

		return cls(f'{m[0]}')

	def __repr__(self):
		return f'Color({super().__repr__()})'


class CurrencyCode(str):

	"""
	An ISO 4217 alphabetical currency code. For the list of current currency, refer to https://en.wikipedia.org/wiki/ISO_4217#Active_codes.
  Example: CAD for Canadian dollars, EUR for euros or JPY for Japanese yen.
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, str):
			raise TypeError('string required')

		m = currencies.get(alpha_3=v.upper())

		if 'alpha_3' not in m:
			raise ValueError('invalid CurrencyCode value')

		return cls(f'{m.get("alpha_3")}')

	def __repr__(self):
		return f'CurrencyCode({super().__repr__()})'


class CurrencyAmount(decimal.Decimal):

	"""
	A decimal value indicating a currency amount. The number of decimal places is specified by ISO 4217 for the accompanying Currency code.
	All financial calculations should be processed as decimal, currency, or another equivalent type suitable for financial calculations
	depending on the programming language used to consume data. Processing currency amounts as float is discouraged due to gains or
	losses of money during calculations.
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, (str, float, decimal.Decimal)):
			raise TypeError('float or float-convertible string required')

		m = decimal.Decimal(v)

		if not m:
			raise ValueError('invalid CurrencyAmount value')

		return cls(m)

	def __repr__(self):
		return f'CurrencyAmount({super().__repr__()})'


class Date(str):

	"""
	Service day in the YYYYMMDD format. Since time within a service day may be above 24:00:00, a service day may contain information for the subsequent day(s).
	Example: 20180913 for September 13th, 2018.
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, str):
			raise TypeError('string required')

		m = parse(v)

		if not isinstance(m, datetime.datetime):
			raise ValueError('invalid Date value')

		return cls(f'{m.strftime("%Y%m%d")}')

	def __repr__(self):
		return f'Date({super().__repr__()})'



class Email(str):

	"""
	An email address.
	Example: example@example.com
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, str):
			raise TypeError('string required')

		m = re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', v)

		if not m:
			raise ValueError('invalid Email address value')

		return cls(f'{m.string}')

	def __repr__(self):
		return f'Email({super().__repr__()})'


class Enum(int):

	"""
	An option from a set of predefined constants defined in the "Description" column.
  Example: The route_type field contains a 0 for tram, a 1 for subway...
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, (int, str)):
			raise TypeError('integer or integer-convertible string required')

		m = int(v)

		if m is None or m < 0:
			raise ValueError('invalid Enum value')

		return cls(m)

	def __repr__(self):
		return f'Enum({super().__repr__()})'


class ID(str):

	"""
	An ID field value is an internal ID, not intended to be shown to riders, and is a sequence of any UTF-8 characters. Using only printable ASCII characters is recommended. An ID is labeled "unique ID" when it must be unique within a file. IDs defined in one .txt file are often referenced in another .txt file. IDs that reference an ID in another table are labeled "foreign ID".
  Example: The stop_id field in stops.txt is a "unique ID". The parent_station field in stops.txt is a "foreign ID referencing stops.stop_id".
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, (str, int)):
			raise TypeError('string or string-convertible integer required')

		m = str(v)

		if not m:
			raise ValueError('invalid ID value')

		return cls(m)

	def __repr__(self):
		return f'ID({super().__repr__()})'


class LanguageCode(str):

	"""
	An IETF BCP 47 language code. For an introduction to IETF BCP 47, refer to http://www.rfc-editor.org/rfc/bcp/bcp47.txt and http://www.w3.org/International/articles/language-tags/.
  Example: en for English, en-US for American English or de for German.
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, str):
			raise TypeError('string required')

		m = bcp47(v)

		if not m:
			raise ValueError('invalid Language Code value')

		return cls(f'{str(m)}')

	def __repr__(self):
		return f'LanguageCode({super().__repr__()})'


class Latitude(decimal.Decimal):

	"""
	WGS84 latitude in decimal degrees. The value must be greater than or equal to -90.0 and less than or equal to 90.0.
  Example: 41.890169 for the Colosseum in Rome.
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, str) and not isinstance(v, (decimal.Decimal, float)):
			raise TypeError('string or decimal required')

		m = decimal.Decimal(v)

		if not m or m < -90.0 or m > 90.0:
			raise ValueError('invalid Latitude value')

		return cls(m)

	def __repr__(self):
		return f'Latitude({super().__repr__()})'



class Longitude(decimal.Decimal):

	"""
	WGS84 longitude in decimal degrees. The value must be greater than or equal to -180.0 and less than or equal to 180.0.
  Example: 12.492269 for the Colosseum in Rome.
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, str) and not isinstance(v, (decimal.Decimal, float)):
			raise TypeError('string or decimal required')

		m = decimal.Decimal(v)

		if not m or m < -180.0 or m > 180.0:
			raise ValueError('invalid Longitude value')

		return cls(m)

	def __repr__(self):
		return f'Longitude({super().__repr__()})'


class Float(float):

	"""
	A floating point number.
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, (str, float, decimal.Decimal)):
			raise TypeError('float or Decimal or float-convertible string required')

		m = decimal.Decimal(v)

		if not m:
			raise ValueError('invalid Float value')

		return cls(m)

	def __repr__(self):
		return f'Float({super().__repr__()})'


class Integer(int):

	"""
	An integer
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, (str, int)):
			raise TypeError('integer or integer-convertible string required')

		m = int(v)

		if not m:
			raise ValueError('invalid Integer value')

		return cls(m)

	def __repr__(self):
		return f'Integer({super().__repr__()})'


class PhoneNumber(str):

	"""
	A phone number.
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, str):
			raise TypeError('string required')

		m = phonenumbers.parse(v, "US")

		if not phonenumbers.is_possible_number(m):
			raise ValueError('invalid Phone Number value')

		return cls(f'{phonenumbers.format_number(m, phonenumbers.PhoneNumberFormat.E164)}')

	def __repr__(self):
		return f'PhoneNumber({super().__repr__()})'


class Time(str):

	"""
	Time in the HH:MM:SS format (H:MM:SS is also accepted). The time is measured from "noon minus 12h" of the service day
	(effectively midnight except for days on which daylight savings time changes occur). For times occurring after midnight,
	enter the time as a value greater than 24:00:00 in HH:MM:SS local time for the day on which the trip schedule begins.
  Example: 14:30:00 for 2:30PM or 25:35:00 for 1:35AM on the next day.
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, str):
			raise TypeError('string required')

		m = re.fullmatch(r'[0-2]{0,1}[0-9]{1}:[0-9]{2}:[0-9]{2}', v)

		if not m:
			raise ValueError('invalid Time value')

		return cls(f'{m.string}')

	def __repr__(self):
		return f'Time({super().__repr__()})'


class Text(str):

	"""
	A string of UTF-8 characters, which is aimed to be displayed and which must therefore be human readable.
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, str):
			raise TypeError('string required')

		m = str(v)

		if not m:
			raise ValueError('invalid Text value')

		return cls(m)

	def __repr__(self):
		return f'Text({super().__repr__()})'


class Timezone(str):

	"""
	TZ timezone from the https://www.iana.org/time-zones. Timezone names never contain the space character but may contain
	an underscore. Refer to http://en.wikipedia.org/wiki/List_of_tz_zones for a list of valid values.
  Example: Asia/Tokyo, America/Los_Angeles or Africa/Cairo.
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, str):
			raise TypeError('string required')

		m = dateutil.tz.gettz(name=v)

		if not m:
			raise ValueError('invalid Timezone value')

		return cls(v)

	def __repr__(self):
		return f'Timezone({super().__repr__()})'


class Url(str):

	"""
	A fully qualified URL that includes http:// or https://, and any special characters in the URL must be correctly escaped.
	See the following http://www.w3.org/Addressing/URL/4_URI_Recommentations.html for a description of how to create fully qualified URL values.
	"""

	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not isinstance(v, str):
			raise TypeError('string required')

		m = urlparse(v)

		if not all([m.scheme, m.netloc]):
			raise ValueError('invalid Url value')

		return cls(v)

	def __repr__(self):
		return f'Url({super().__repr__()})'
