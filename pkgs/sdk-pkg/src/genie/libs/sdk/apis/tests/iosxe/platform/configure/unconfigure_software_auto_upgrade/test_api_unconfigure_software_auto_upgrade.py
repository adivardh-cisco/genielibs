import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.platform.configure import unconfigure_software_auto_upgrade


class TestUnconfigureSoftwareAutoUpgrade(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          Switch1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: c9200
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['Switch1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_unconfigure_software_auto_upgrade(self):
        result = unconfigure_software_auto_upgrade(self.device, 'enable', '')
        expected_output = None
        self.assertEqual(result, expected_output)
