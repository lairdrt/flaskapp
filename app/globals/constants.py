# App title
TITLE = 'Waterworks Valve Controller'

# Program version (major.minor)
VERSION = '0.10'

# Version release date
RELEASED = '11 November 2022'

# Max session token length (+7)
SESSION_TOKEN_LEN = 20

# File paths
BASE_DIR = '/home/webapp/vctrl/'
LOG_FILE_DIR = BASE_DIR + 'logs/'
LOG_FILE_NAME = LOG_FILE_DIR + 'vctrl.log'

# Flash message styles from bootstrap
FLASH_ERROR = 'alert-danger'
FLASH_INFO = 'alert-info'
FLASH_SUCCESS = 'alert-success'
FLASH_WARNING = 'alert-warning'

NONE_DISP = '...' # when object/field is None

# Default username
SYSADMIN_USERNAME = 'vctrladmin'

# Site/zone operational literals (map to select lists)
STATE_ONLINE = 1
STATE_OFFLINE = 2
STATE_DISP_ONLINE = 'Online'
STATE_DISP_OFFLINE = 'Offline'
STATE_SZ_CHOICES = [
    (STATE_ONLINE, STATE_DISP_ONLINE),
    (STATE_OFFLINE, STATE_DISP_OFFLINE)
]

# Valve operational literals (map to select lists)
STATE_ON = 1
STATE_OFF = 2
STATE_DISP_ON = 'On'
STATE_DISP_OFF = 'Off'
STATE_VL_CHOICES = [
    (STATE_ON, STATE_DISP_ON),
    (STATE_OFF, STATE_DISP_OFF)
]

# Unit designation database literals (map to select lists)
UNITS_US = 1
UNITS_SI = 2
UNITS_DISP_US = 'U.S. Customary System (USCS)'
UNITS_DISP_SI = 'International System of Units (SI)'
UNITS_CHOICES = [
    (UNITS_US, UNITS_DISP_US),
    (UNITS_SI, UNITS_DISP_SI)
]

# User field literals
USER_NAME_LEN_MIN = 6
USER_NAME_LEN_MAX = 16
USER_PWD_LEN_MIN = 8
USER_PWD_LEN_MAX = 16

# Size of a UNICODE char using format: &#x0000
UNICODE_CHAR_LEN = 7

# Geocoordinate locater service constants (map to select lists)
GEOLOC_NONE = 0
GEOLOC_MAPQUEST = 1
GEOLOC_NOMINATIM = 2
GEOLOC_DISP_MAPQUEST = 'MapQuest'
GEOLOC_DISP_NOMINATIM = 'Nominatim'
GEOLOC_CHOICES = [
    (GEOLOC_NONE, 'None'),
    (GEOLOC_MAPQUEST, GEOLOC_DISP_MAPQUEST),
    (GEOLOC_NOMINATIM, GEOLOC_DISP_NOMINATIM)
]
GEOLOC_MAPQUEST_URL = 'http://www.mapquestapi.com/geocoding/v1/address'
GEOLOC_MAPQUEST_KEY = 'VKbGkSYtx67R924gWK2hExvfpX1FZKdJ'
GEOLOC_NOMINATIM_URL = 'https://nominatim.openstreetmap.org/search'
GEOLOC_NOMINATIM_KEY = ''
GEOLOC_ACCESS_KEY_LEN = 64

# Location elevation service constants (map to select lists)
ELEVATION_NONE = 0
ELEVATION_JAWGMAPS = 1
ELEVATION_MAPQUEST = 2
ELEVATION_OPENTOPO = 3
ELEVATION_DISP_JAWGMAPS = 'Jawg Maps'
ELEVATION_DISP_MAPQUEST = 'MapQuest'
ELEVATION_DISP_OPENTOPO = 'Open Topo Data'
ELEVATION_CHOICES = [
    (ELEVATION_NONE, 'None'),
    (ELEVATION_JAWGMAPS, ELEVATION_DISP_JAWGMAPS),
    (ELEVATION_MAPQUEST, ELEVATION_DISP_MAPQUEST),
    (ELEVATION_OPENTOPO, ELEVATION_DISP_OPENTOPO)
]
# https://api.jawg.io/elevations?locations=32.806128,-117.027267&access-token=aXrk9xQcu82pm6BhM0GA5Ax77Rv9QachEKzpjm97dQe13tyAP0Hvmw9ZF0hzQJvs
# 226.40039m
ELEVATION_JAWGMAPS_URL = 'https://api.jawg.io/elevations'
ELEVATION_JAWGMAPS_KEY = 'aXrk9xQcu82pm6BhM0GA5Ax77Rv9QachEKzpjm97dQe13tyAP0Hvmw9ZF0hzQJvs'
# http://open.mapquestapi.com/elevation/v1/profile?latLngCollection=32.805990,-117.027700&key=VKbGkSYtx67R924gWK2hExvfpX1FZKdJ
# 222m
ELEVATION_MAPQUEST_URL = 'http://open.mapquestapi.com/elevation/v1/profile'
ELEVATION_MAPQUEST_KEY = 'VKbGkSYtx67R924gWK2hExvfpX1FZKdJ'
# https://api.opentopodata.org/v1/aster30m?locations=32.806128,-117.027267
# 220m
# https://api.opentopodata.org/v1/etopo1?locations=32.806128,-117.027267
# 234m
ELEVATION_OPENTOPODATA_URL = 'https://api.opentopodata.org/v1/aster30m'
ELEVATION_OPENTOPODATA_KEY = ''
ELEVATION_ACCESS_KEY_LEN = 64

# Weather service constants (map to select lists)
WEATHER_NONE = 0
WEATHER_CLIMACELL = 1
WEATHER_OPEN_WEATHER_MAP = 2
WEATHER_VISUAL_CROSSING = 3
WEATHER_DISP_CLIMACELL = 'Clima Cell'
WEATHER_DISP_OPEN_WEATHER_MAP = 'Open Weather Map'
WEATHER_DISP_VISUAL_CROSSING = 'Visual Crossing'
WEATHER_CHOICES = [
    (WEATHER_NONE, 'None'),
    (WEATHER_CLIMACELL, WEATHER_DISP_CLIMACELL),
    (WEATHER_OPEN_WEATHER_MAP, WEATHER_DISP_OPEN_WEATHER_MAP),
    (WEATHER_VISUAL_CROSSING, WEATHER_DISP_VISUAL_CROSSING)
]
WEATHER_CLIMACELL_URL_CURRENT = 'https://data.climacell.co/v4/timelines'
WEATHER_CLIMACELL_URL_HISTORY = 'https://api.climacell.co/v3/weather/historical/station'
WEATHER_CLIMACELL_V3_KEY = 'ej7bp8PZGcI48hnszTCv5KbrSMVSGx9f'
WEATHER_CLIMACELL_V4_KEY = 'ZPc92ILTxCzOdLzjWmzopJuionwv3y36'
WEATHER_OPEN_WEATHER_MAP_URL_CURRENT = 'https://api.openweathermap.org/data/2.5/onecall'
WEATHER_OPEN_WEATHER_MAP_URL_HISTORY = 'https://api.openweathermap.org/data/2.5/onecall/timemachine'
WEATHER_OPEN_WEATHER_MAP_KEY = '224a233f82f672f032b9b50ad321813e'
WEATHER_VISUAL_CROSSING_URL_CURRENT = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline'
WEATHER_VISUAL_CROSSING_URL_HISTORY = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline'
WEATHER_VISUAL_CROSSING_KEY = 'BQXEG7LH2CS7U8XZZNXVR3KFQ'
WEATHER_ACCESS_KEY_LEN = 64
WEATHER_UNKNOWN = 'Unknown'
WEATHER_UNKNOWN_ICON = 'far fa-eclipse'

# Unit lables in US and SI units
VOL_DISP_US = 'Gallons'
VOL_DISP_SI = 'Liters'

VOL_DISP_US_SING = 'gallon'
VOL_DISP_SI_SING = 'liter'

VOL_DISP_US_SHORT = 'g'
VOL_DISP_SI_SHORT = 'l'

VOL_DISP_US_PRECIP = 'in'
VOL_DISP_SI_PRECIP = 'mm'

FLOW_DISP_US = 'gpm'
FLOW_DISP_SI = 'lpm'

TEMP_DISP_US = '\u2109'
TEMP_DISP_SI = '\u2103'

SPEED_DISP_US = 'mph'
SPEED_DISP_SI = 'kph'
DIRECTION_DISP_ALL = '\u00b0'

PRESSURE_DISP_US = 'inHg'
PRESSURE_DISP_SI = 'mmHg'

RH_DISP_US = '%'
RH_DISP_SI = '%'

# Conversion factors (to four sigfig)
DEG_F_DEG_C = 0.5555
DEG_C_DEG_F = 1.800
GAL_LITER = 3.785
INCH_MM = 25.40
FT_M = 0.3048
MPH_KPH = 1.609
INHG_MMHG = 25.40
HPA_INHG = 0.02953

# Unit conversion functions
def cvt_degF_degC(degF):
    try:
        return (float(degF)-32.0)*DEG_F_DEG_C
    except:
        return 0.0

def cvt_degC_degF(degC):
    try:
        return (float(degC)*DEG_C_DEG_F)+32.0
    except:
        return 0.0

def cvt_gal_liter(gal):
    try:
        return float(gal)*GAL_LITER
    except:
        return 0.0

def cvt_liter_gal(liter):
    try:
        return float(liter)/GAL_LITER
    except:
        return 0.0

def cvt_inch_mm(inch):
    try:
        return float(inch)*INCH_MM
    except:
        return 0.0

def cvt_mm_inch(mm):
    try:
        return float(mm)/INCH_MM
    except:
        return 0.0

def cvt_ft_m(feet):
    try:
        return float(feet)*FT_M
    except:
        return 0.0

def cvt_m_ft(meter):
    try:
        return float(meter)/FT_M
    except:
        return 0.0

def cvt_mph_kph(mph):
    try:
        return float(mph)*MPH_KPH
    except:
        return 0.0

def cvt_kph_mph(kph):
    try:
        return float(kph)/MPH_KPH
    except:
        return 0.0

def cvt_inhg_mmhg(inhg):
    try:
        return float(inhg)*INHG_MMHG
    except:
        return 0.0

def cvt_mmhg_inhg(mmhg):
    try:
        return float(mmhg)/INHG_MMHG
    except:
        return 0.0

def cvt_hpa_inhg(hpa):
    try:
        return float(hpa)*HPA_INHG
    except:
        return 0.0

ROSE = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
def cvt_deg_rose(deg):
    try:
        ix = round(deg / 22.5)
        return ROSE[ix % 16]
    except:
        return NONE_DISP

# Convert US units to SI units
def cvt_rainfall_from_us(level, units):
    if units == UNITS_US:
        return level
    elif units == UNITS_SI:
        return cvt_inch_mm(level)
    else:
        return 0.0

def cvt_snowfall_from_us(level, units):
    if units == UNITS_US:
        return level
    elif units == UNITS_SI:
        return cvt_inch_mm(level)
    else:
        return 0.0

def cvt_temp_from_us(level, units):
    if units == UNITS_US:
        return level
    elif units == UNITS_SI:
        return cvt_degF_degC(level)
    else:
        return 0.0

def cvt_windspeed_from_us(level, units):
    if units == UNITS_US:
        return level
    elif units == UNITS_SI:
        return cvt_mph_kph(level)
    else:
        return 0.0

def cvt_rainfall_to_us(level, units):
    if units == UNITS_US:
        return level
    elif units == UNITS_SI:
        return cvt_mm_inch(level)
    else:
        return 0.0

def cvt_snowfall_to_us(level, units):
    if units == UNITS_US:
        return level
    elif units == UNITS_SI:
        return cvt_mm_inch(level)
    else:
        return 0.0

def cvt_temp_to_us(level, units):
    if units == UNITS_US:
        return level
    elif units == UNITS_SI:
        return cvt_degC_degF(level)
    else:
        return 0.0

def cvt_windspeed_to_us(level, units):
    if units == UNITS_US:
        return level
    elif units == UNITS_SI:
        return cvt_kph_mph(level)
    else:
        return 0.0

# Logged error message number bases
MSG_ALEXA_BASE =     1000
MSG_AUTH_BASE =      2000
MSG_DATABASE_BASE =  3000
MSG_DEVICES_BASE =   4000
MSG_DEVMGR_BASE =    5000
MSG_ERRORS_BASE =    6000
MSG_GLOBALS_BASE =   7000 
MSG_HELP_BASE =      8000
MSG_INIT_BASE =      9000
MSG_INSTANCE_BASE =  10000
MSG_LOG_BASE =       11000
MSG_MAIN_BASE =      12000
MSG_PROGRAMS_BASE =  13000
MSG_SCHEDULE_BASE =  14000
MSG_SETTINGS_BASE =  15000
MSG_SITE_BASE =      16000
MSG_STATIC_BASE =    17000
MSG_TASKS_BASE =     18000
MSG_TEMPLATES_BASE = 19000
MSG_TOOLS_BASE =     20000
MSG_USAGE_BASE =     21000
MSG_UTIL_BASE =      22000
MSG_VALVES_BASE =    23000
MSG_ZONES_BASE =     24000