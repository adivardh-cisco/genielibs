import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.aaa.configure import configure_username


class TestConfigureUsername(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          Switch-9300:
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
        self.device = self.testbed.devices['Switch-9300']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_username(self):
        result = configure_username(self.device, 'test', 'lab', '1')
        expected_output = None
        self.assertEqual(result, expected_output)

class TestConfigureUsernameSecret(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          yang-infra-c8kv-3:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: vwlc
            type: wlc
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['yang-infra-c8kv-3']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_username(self):
        result = configure_username(self.device, 'USER', '', 0, 15, 'VIEW', 'common-criteria-policy', 'POLICY', 'test')
        expected_output = None
        self.assertEqual(result, expected_output)
