# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.domain import Domain
from twilio.rest.bulkexports.v1 import V1


class Bulkexports(Domain):

    def __init__(self, twilio):
        """
        Initialize the Bulkexports Domain

        :returns: Domain for Bulkexports
        :rtype: twilio.rest.bulkexports.Bulkexports
        """
        super(Bulkexports, self).__init__(twilio)

        self.base_url = 'https://bulkexports.twilio.com'

        # Versions
        self._v1 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of bulkexports
        :rtype: twilio.rest.bulkexports.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def exports(self):
        """
        :rtype: twilio.rest.bulkexports.v1.export.ExportList
        """
        return self.v1.exports

    @property
    def export_configuration(self):
        """
        :rtype: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationList
        """
        return self.v1.export_configuration

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Bulkexports>'