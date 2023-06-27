import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.multicast.configure import configure_mld_version
from genie.libs.sdk.apis.iosxe.interface.configure import configure_monitor_erspan_source_interface


class TestConfigureMldVersion(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
            n08HA:
                connections:
                defaults:
                    class: unicon.Unicon
                a:
                    command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                    protocol: unknown
                os: iosxe
                platform: c9500
                type: c9500
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['n08HA']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_mld_version(self):
        result = configure_mld_version(self.device, 202, 2)
        expected_output = None
        self.assertEqual(result, expected_output)

class TestConfigureMonitorErspanSourceInterface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          T2-9500-RA_SDG:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: c9500
            type: c9500
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['T2-9500-RA_SDG']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_monitor_erspan_source_interface(self):
        result = configure_monitor_erspan_source_interface(self.device, '1', 'te1/0/2', 'rx')
        expected_output = None
        self.assertEqual(result, expected_output)
