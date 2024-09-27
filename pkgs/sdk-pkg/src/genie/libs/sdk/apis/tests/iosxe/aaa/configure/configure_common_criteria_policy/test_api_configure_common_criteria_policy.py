import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.aaa.configure import configure_common_criteria_policy

class TestConfigureCommonCriteriaPolicy(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          Router:
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
        self.device = self.testbed.devices['Router']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_common_criteria_policy(self):
        result = configure_common_criteria_policy(self.device, 'ABCD', None, None, None, None, None, None, 1, None, None, None, False, None)
        expected_output = None
        self.assertEqual(result, expected_output)

class TestConfigureCommonCriteriaPolicyBase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          Router:
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
        self.device = self.testbed.devices['Router']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_common_criteria_policy(self):
        result = configure_common_criteria_policy(self.device, 'ABCD', None, None, None, None, None, None, 1, None, None, None, False, None)
        expected_output = None
        self.assertEqual(result, expected_output)
