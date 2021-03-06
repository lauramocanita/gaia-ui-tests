# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from gaiatest.apps.base import Base


class System(Base):

    # status bar
    _status_bar_locator = ('id', 'statusbar')
    _status_bar_notification_locator = ('id', 'statusbar-notification')

    _notification_toaster_locator = ('id', 'notification-toaster')

    def wait_for_status_bar_displayed(self):
        self.wait_for_element_displayed(*self._status_bar_locator)

    def wait_for_notification_toaster_displayed(self):
        # TODO Re-enable this when Bug 861874
        # self.wait_for_element_displayed(*self._notification_toaster_locator)
        self.wait_for_condition(lambda m: m.find_element(*self._notification_toaster_locator).location['y'] == 0)

    def wait_for_notification_toaster_not_displayed(self):
        # TODO Re-enable this when Bug 861874
        # self.wait_for_element_not_displayed(*self._notification_toaster_locator)
        self.wait_for_condition(lambda m: m.find_element(*self._notification_toaster_locator).location['y'] == -50)

    def open_utility_tray(self):
        # TODO Use actions for this
        self.marionette.execute_script("window.wrappedJSObject.UtilityTray.show()")

        from gaiatest.apps.system.regions.utility_tray import UtilityTray
        return UtilityTray(self.marionette)
