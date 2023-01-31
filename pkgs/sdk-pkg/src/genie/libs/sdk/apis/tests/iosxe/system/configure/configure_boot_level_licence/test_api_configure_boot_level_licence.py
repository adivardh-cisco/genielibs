import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.system.configure import configure_boot_level_licence


class TestConfigureBootLevelLicence(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          BB_ASR1006-X:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: iosxe
            type: iosxe
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['BB_ASR1006-X']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_boot_level_licence(self):
        result = configure_boot_level_licence(self.device, False, False, False, True, False, False, True)
        expected_output = None
        self.assertEqual(result, expected_output)
