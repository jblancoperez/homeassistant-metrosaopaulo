
from homeassistant.helpers.entity import Entity
import logging
from datetime import timedelta
import voluptuous as vol


REQUIREMENTS=['metrosaopaulo==0.0.2']
_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(seconds=10)
ICON = 'mdi:train'
CONF_LINES='lines'

from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_LINES, 'line_filter'):
        vol.All(cv.ensure_list, vol.Length(min=1), [cv.string])
    
})








def setup_platform(hass, config, add_entities, discovery_info=None):
    """Setup the sensor platform."""
    lines = config.get(CONF_LINES)
    sensors = []
    for l in lines:
        sensors.append(MetroSPSensor(l))
    add_entities(sensors,True)


class MetroSPSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self,name):
        """Initialize the sensor."""
        from metrosaopaulo import metrosaopaulo
        self._state = None
        self._name = name
        self._metrosaopaulo = metrosaopaulo.MetroSaoPaulo()

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def icon(self):
        """Return the icon for the frontend."""
        return ICON

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        status = self._metrosaopaulo.get_metro_status().get(self._name, None)
        _LOGGER.info('Pegando dados para {} . Valor {}'.format(self._name,status))
        self._state = status
        

