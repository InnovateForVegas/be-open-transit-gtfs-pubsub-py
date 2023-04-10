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

from gtfs_pubsub.domain.model.gtfs.gtfs_types import Color, CurrencyCode, CurrencyAmount, Date, Email, Enum, ID, LanguageCode, Latitude, Longitude, Float, Integer, PhoneNumber, Time, Text, Timezone, Url
from pydantic import BaseModel
import pytest
import decimal


# ########### Color

class ColorModel(BaseModel):
	test_Color: Color

def test_Color_valid():
	c = ColorModel(test_Color = "FFFFFF")
	assert c is not None

def test_Color_valid_hashtag():
	c = ColorModel(test_Color = "#FFFFFF")
	assert c is not None

def test_Color_invalid_value():
	with pytest.raises(Exception) as e_info:
		c = ColorModel(test_Color = "FFFF")

def test_Color_invalid_type():
	with pytest.raises(Exception) as e_info:
		c = ColorModel(test_Color = 1234)



# ########### CurrencyCode

class CurrencyCodeModel(BaseModel):
	test_CurrencyCode: CurrencyCode

def test_CurrencyCode_valid():
	c = CurrencyCodeModel(test_CurrencyCode = 'USD')
	assert c.test_CurrencyCode == 'USD'



# ########### CurrencyAmount

class CurrencyAmountModel(BaseModel):
	test_CurrencyAmount: CurrencyAmount

def test_CurrencyAmount_valid_string():
	c = CurrencyAmountModel(test_CurrencyAmount="1.23")
	assert c.test_CurrencyAmount == decimal.Decimal("1.23")

def test_CurrencyAmount_valid_float():
	c = CurrencyAmountModel(test_CurrencyAmount=1.23)
	assert c.test_CurrencyAmount == decimal.Decimal(1.23)


# ########### Date

class DateModel(BaseModel):
	test_Date: Date

def test_Date_valid_string():
	d = DateModel(test_Date="20240401")
	assert d.test_Date == "20240401"

def test_Date_invalid_string():
	with pytest.raises(Exception) as e_info:
		d = DateModel(test_Date="Hello")




# ########### Email

class EmailModel(BaseModel):
	test_Email: Email

def test_Email_valid():
	m = EmailModel(test_Email="test@example.com")
	assert m.test_Email == "test@example.com"

def test_Email_invalid_tld():
	with pytest.raises(Exception) as e_info:
		m = EmailModel(test_Email="test@example")

def test_Email_invalid_type():
	with pytest.raises(Exception) as e_info:
		m = EmailModel(test_Email=1234)


# ########### Enum

class EnumModel(BaseModel):
	test_Enum: Enum

def test_Enum_valid_integer():
	e = EnumModel(test_Enum=0)

def test_Enum_valid_string():
	e = EnumModel(test_Enum="1")

def test_Enum_invalid_negative():
	with pytest.raises(Exception) as e_info:
		m = EnumModel(test_Enum=-1)

def test_Enum_invalid_string():
	with pytest.raises(Exception) as e_info:
		m = EnumModel(test_Enum="Hello")


# ########### ID

class IDModel(BaseModel):
	test_ID: ID

def test_ID_valid_int():
	i = IDModel(test_ID=1234)
	assert i.test_ID == "1234"

def test_ID_valid_string():
	i = IDModel(test_ID="abcd")
	assert i.test_ID == "abcd"


# ########### LanguageCode

class LanguageCodeModel(BaseModel):
	test_LanguageCode: LanguageCode

def test_LanguageCode_valid_string():
	l = LanguageCodeModel(test_LanguageCode="en-US")
	assert l.test_LanguageCode == 'en-US'

def test_LanguageCode_invalid_string():
	with pytest.raises(Exception) as e_info:
		m = EnumModel(test_Enum="Hello")



# ########### Latitude

class LatitudeModel(BaseModel):
	test_Latitude: Latitude

def test_Latitude_valid_string():
	lat = LatitudeModel(test_Latitude="36.055681")
	assert lat.test_Latitude == decimal.Decimal("36.055681")

def test_Latitude_valid_float():
	lat = LatitudeModel(test_Latitude=36.055681)
	assert lat.test_Latitude ==  decimal.Decimal(36.055681)


def test_Latitude_invalid_negative():
	with pytest.raises(Exception) as e_info:
		lat = LatitudeModel(test_Latitude=-95.0)

def test_Latitude_invalid_positive():
	with pytest.raises(Exception) as e_info:
		lat = LatitudeModel(test_Latitude=95.0)


# ########### Longitude

class LongitudeModel(BaseModel):
	test_Longitude: Longitude

def test_Longitude_valid_string():
	lon = LongitudeModel(test_Longitude="-115.080784")
	assert lon.test_Longitude == decimal.Decimal("-115.080784")

def test_Longitude_valid_float():
	lon = LongitudeModel(test_Longitude=-115.080784)
	assert lon.test_Longitude == decimal.Decimal(-115.080784)

def test_Longitude_invalid_negative():
	with pytest.raises(Exception) as e_info:
		lat = LongitudeModel(test_Longitude=-185.0)

def test_Longitude_invalid_positive():
	with pytest.raises(Exception) as e_info:
		lat = LongitudeModel(test_Longitude=185.0)



# ########### Float

class FloatModel(BaseModel):
	test_Float: Float

def test_Float_valid_float():
	f = FloatModel(test_Float=1.23)
	assert f.test_Float == 1.23

def test_Float_valid_string():
	f = FloatModel(test_Float="1.23")
	assert f.test_Float == 1.23

def test_Float_invalid_string():
	with pytest.raises(Exception) as e_info:
		f = FloatModel(test_Float="Hello")




# ########### Integer

class IntegerModel(BaseModel):
	test_Integer: Integer

def test_Integer_valid_int():
	i = IntegerModel(test_Integer=1)
	assert i.test_Integer == 1

def test_Integer_valid_string():
	i = IntegerModel(test_Integer="1")
	assert i.test_Integer == 1

def test_Integer_invalid_string():
	with pytest.raises(Exception) as e_info:
		i = IntegerModel(test_Integer="Hello")



# ########### PhoneNumber

class PhoneNumberModel(BaseModel):
	test_PhoneNumber: PhoneNumber

def test_PhoneNumber_valid_us():
	p = PhoneNumberModel(test_PhoneNumber="+17025551212")
	assert p.test_PhoneNumber == "+17025551212"

def test_PhoneNumber_invalid_string():
	with pytest.raises(Exception) as e_info:
		p = PhoneNumberModel(test_PhoneNumber="Hello")


# ########### Time

class TimeModel(BaseModel):
	test_Time: Time

def test_Time_valid_today():
	t = TimeModel(test_Time="12:00:01")
	assert t.test_Time == "12:00:01"

def test_Time_valid_tomorrow():
	t = TimeModel(test_Time="24:01:00")
	assert t.test_Time == "24:01:00"

def test_Time_invalid_string():
	with pytest.raises(Exception) as e_info:
		t = TimeModel(test_Time="24:Hello")

def test_Time_invalid_int():
	with pytest.raises(Exception) as e_info:
		t = TimeModel(test_Time=123983438)



# ########### Text

class TextModel(BaseModel):
	test_Text: Text

def test_Text_valid_string():
	t = TextModel(test_Text="Hello")
	assert t.test_Text == "Hello"



# ########### Timezone

class TimezoneModel(BaseModel):
	test_Timezone: Timezone

def test_Timezone_valid_zone():
	t = TimezoneModel(test_Timezone="America/Los Angeles")
	assert t.test_Timezone == "America/Los Angeles"

def test_Timezone_invalid_zone():
	with pytest.raises(Exception) as e_info:
		p = TimezoneModel(test_Timezone="Hello")



# ########### Url

class UrlModel(BaseModel):
	test_Url: Url


def test_Url_valid_http():
	u = UrlModel(test_Url="http://example.com")
	assert u.test_Url == "http://example.com"

def test_Url_valid_https():
	u = UrlModel(test_Url="https://example.com")
	assert u.test_Url == "https://example.com"

def test_Url_invalid_path():
	with pytest.raises(Exception) as e_info:
		u = UrlModel(test_Url="/example.com")

def test_Url_invalid_string():
	with pytest.raises(Exception) as e_info:
		u = UrlModel(test_Url="hello")

def test_Url_invalid_integer():
	with pytest.raises(Exception) as e_info:
		u = UrlModel(test_Url=1234)
