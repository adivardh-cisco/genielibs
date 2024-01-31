import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.mdns.configure import configure_mdns_remote_cache_max_limit


class TestConfigureMdnsRemoteCacheMaxLimit(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          T4-9500-SVL2:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: c9500
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['T4-9500-SVL2']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_mdns_remote_cache_max_limit(self):
        result = configure_mdns_remote_cache_max_limit(self.device, 1000)
        expected_output = None
        self.assertEqual(result, expected_output)
