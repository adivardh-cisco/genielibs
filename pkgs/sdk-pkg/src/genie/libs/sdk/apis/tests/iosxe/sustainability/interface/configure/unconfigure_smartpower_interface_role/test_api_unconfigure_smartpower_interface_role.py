import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.sustainability.interface.configure import unconfigure_smartpower_interface_role


class TestUnconfigureSmartpowerInterfaceRole(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          9300L:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: c9300
            type: c9300
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['9300L']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_unconfigure_smartpower_interface_role(self):
        result = unconfigure_smartpower_interface_role(self.device, 'Gi1/0/13', 'critical')
        expected_output = None
        self.assertEqual(result, expected_output)
