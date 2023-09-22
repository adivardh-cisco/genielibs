import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.platform.execute import execute_archive_tar


class TestExecuteArchiveTar(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          GD_F12:
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
        self.device = self.testbed.devices['GD_F12']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_execute_archive_tar(self):
        result = execute_archive_tar(self.device, 'usb_files_9.tar', 'create', 'bootflash:', 'tracelogs', 'usb0:', 'test', 120)
        expected_output = ('archiving dmesg (66264 bytes)\r\n'
 'archiving timestamp (10 bytes)\r\n'
 'archiving shutdown_cc0_20230913134955.log (705 bytes)\r\n'
 'archiving shutdown_fp0_20230913134955.log (633 bytes)\r\n'
 'archiving utf_R0-0.5887_6674.20230914055716.bin.gz (808254 bytes)\r\n'
 'archiving utf_R0-0.5887_6675.20230914055725.bin.gz (806594 bytes)\r\n'
 'archiving utf_R0-0.5887_6676.20230914055734.bin.gz (808838 bytes)\r\n'
 'archiving utf_R0-0.5887_6677.20230914055743.bin.gz (807858 bytes)\r\n'
 'archiving utf_R0-0.5887_6678.20230914055752.bin.gz (807057 bytes)\r\n'
 'archiving utf_R0-0.5887_6679.20230914055801.bin.gz (809544 bytes)\r\n'
 'archiving utf_R0-0.5887_6680.20230914055809.bin.gz (807218 bytes)\r\n'
 'archiving utf_R0-0.5887_6681.20230914055818.bin.gz (807444 bytes)\r\n'
 'archiving utf_R0-0.5887_6682.20230914055827.bin.gz (808464 bytes)\r\n'
 'archiving utf_R0-0.5887_6683.20230914055836.bin.gz (808658 bytes)\r\n'
 'archiving utf_R0-0.5887_6684.20230914055845.bin.gz (807272 bytes)\r\n'
 'archiving utf_R0-0.5887_6673.20230914055707.bin.gz (808002 bytes)\r\n'
 'archiving utf_R0-0.5887_6685.20230914055854.bin.gz (807831 bytes)\r\n'
 'archiving utf_R0-0.5887_6686.20230914055903.bin.gz (813608 bytes)\r\n'
 'archiving utf_R0-0.5887_6687.20230914055912.bin.gz (811137 bytes)\r\n'
 'archiving shutdown_cc0_20230914055927.log (705 bytes)\r\n'
 'archiving utf_R0-0.5900_0.20230914062758.bin.gz (1328995 bytes)\r\n'
 'archiving utf_R0-0.5900_1.20230914070052.bin.gz (825329 bytes)\r\n'
 'archiving utf_R0-0.5900_2.20230914070058.bin.gz (811558 bytes)\r\n'
 'archiving utf_R0-0.5900_3.20230914070104.bin.gz (809314 bytes)\r\n'
 'archiving utf_R0-0.5900_4.20230914070110.bin.gz (796014 bytes)\r\n'
 'archiving utf_R0-0.5900_5.20230914070116.bin.gz (805042 bytes)\r\n'
 'archiving utf_R0-0.5900_6.20230914070122.bin.gz (803377 bytes)\r\n'
 'archiving utf_R0-0.5900_7.20230914070128.bin.gz (797514 bytes)\r\n'
 'archiving utf_R0-0.5900_8.20230914070134.bin.gz (801024 bytes)\r\n'
 'archiving utf_R0-0.5900_9.20230914070140.bin.gz (799539 bytes)\r\n'
 'archiving shutdown_cc0_20230914070149.log (705 bytes)\r\n'
 'archiving utf_R0-0.5887_6672.20230914055658.bin.gz (809280 bytes)\r\n'
 'archiving system_shell_R0-0.25305_0.20230913205802.bin (755 bytes)\r\n'
 'archiving memmon_log_20230913_203413_IST_1694617453.tar.gz (18388 bytes)\r\n'
 'archiving system_shell_R0-0.6208_0.20230913215854.bin (5505 bytes)\r\n'
 'archiving btman_pman_0-0.20392_1.20230913140409.bin.gz (1320 bytes)\r\n'
 'archiving pvp_0-0.18819_0.20230913140407.bin.gz (5490 bytes)\r\n'
 'archiving emd_0-0.19421_0.20230913140408.bin.gz (47061 bytes)\r\n'
 'archiving ezman_0-0.19639_0.20230913140408.bin.gz (4441 bytes)\r\n'
 'archiving cmcc_0-0.20291_0.20230913140409.bin.gz (6194 bytes)\r\n'
 'archiving cmcc_pman_0-0.20284_1.20230914055927.bin.gz (993 bytes)\r\n'
 'archiving IOSCC_0-0.21260_0.20230913140412.bin.gz (7344 bytes)\r\n'
 'archiving IOSCC_0-1.21579_0.20230913140412.bin.gz (6372 bytes)\r\n'
 'archiving IOSCC_0-2.21957_0.20230913140412.bin.gz (7140 bytes)\r\n'
 'archiving hman_0-0.20183_2.20230914014418.bin.gz (45974 bytes)\r\n'
 'archiving mcpcc_lc_ms_pman_0-2.21950_4.20230913165052.bin.gz (1413 bytes)\r\n'
 'archiving btman_0-0.20398_4.20230914025408.bin.gz (67666 bytes)\r\n'
 'archiving shutdown_fp0_20230914055928.log (633 bytes)\r\n'
 'archiving pvp_F0-0.16962_0.20230913140402.bin.gz (5602 bytes)\r\n'
 'archiving shutdown_rp0_20230913134956.log (1461 bytes)\r\n'
 'archiving ezman_pman_0-0.19632_1.20230914055927.bin.gz (988 bytes)\r\n'
 'archiving emd_pman_0-0.19413_1.20230914055927.bin.gz (968 bytes)\r\n'
 'archiving hman_pman_0-0.20176_1.20230914055927.bin.gz (965 bytes)\r\n'
 'archiving mcpcc_lc_ms_pman_0-1.21572_4.20230914055927.bin.gz (838 bytes)\r\n'
 'archiving mcpcc_lc_ms_pman_0-0.21244_6.20230914055927.bin.gz (519 bytes)\r\n'
 'archiving shutdown_fp0_20230914070149.log (633 bytes)\r\n'
 'archiving cpp_driver_pman_F0-0.17636_1.20230913140403.bin.gz (1173 bytes)\r\n'
 'archiving service_mgr_F0-0.17129_0.20230913140402.bin.gz (5731 bytes)\r\n'
 'archiving cpp_cdm_F0-0.17435_0.20230913140403.bin.gz (3190 bytes)\r\n'
 'archiving cpp_ha_top_level_server_pman_F0-0.17532_1.20230913140403.bin.gz '
 '(1185 bytes)\r\n'
 'archiving cpp_ha_F0-0.17539_0.20230913140403.bin.gz (12085 bytes)\r\n'
 'archiving cpp_cp_svr_pman_F0-0.17843_1.20230914055927.bin.gz (1451 bytes)\r\n'
 'archiving cpp_driver_F0-0.17644_0.20230913140403.bin.gz (4000 bytes)\r\n'
 'archiving cpp_sp_F0-0.17746_0.20230913140403.bin.gz (4451 bytes)\r\n'
 'archiving emd_F0-0.17953_0.20230913140403.bin.gz (47659 bytes)\r\n'
 'archiving cpp_stats_F0-0.17333_0.20230913140404.bin.gz (3955 bytes)\r\n'
 'archiving cman_fp_F0-0.18385_0.20230913140404.bin.gz (3996 bytes)\r\n'
 'archiving btman_pman_F0-0.18481_1.20230913140404.bin.gz (1319 bytes)\r\n'
 'archiving cpp_cp_F0-0.17849_0.20230913140405.bin.gz (18978 bytes)\r\n'
 'archiving fman_fp_F0-0.18091_0.20230913140406.bin.gz (12477 bytes)\r\n'
 'archiving hman_F0-0.18284_2.20230914014413.bin.gz (46015 bytes)\r\n'
 'archiving btman_F0-0.18488_4.20230914025458.bin.gz (67406 bytes)\r\n'
 'archiving pvp_0-0.18967_0.20230914062806.bin.gz (5457 bytes)\r\n'
 'archiving fman_fp_image_pman_F0-0.18071_1.20230914055927.bin.gz (1397 '
 'bytes)\r\n'
 'archiving cpp_sp_svr_pman_F0-0.17739_1.20230914055927.bin.gz (1333 bytes)\r\n'
 'archiving emd_pman_F0-0.17946_1.20230914055927.bin.gz (964 bytes)\r\n'
 'archiving cman_fp_pman_F0-0.18378_1.20230914055927.bin.gz (995 bytes)\r\n'
 'archiving cpp_cdm_svr_pman_F0-0.17429_1.20230914055927.bin.gz (1072 '
 'bytes)\r\n'
 'archiving shutdown_cc0_20230913140009.log (705 bytes)\r\n'
 'archiving cpp_stats_svr_pman_F0-0.17326_1.20230914055927.bin.gz (1071 '
 'bytes)\r\n'
 'archiving service_mgr_pman_F0-0.17120_1.20230914055927.bin.gz (1021 '
 'bytes)\r\n'
 'archiving hman_pman_F0-0.18274_1.20230914055928.bin.gz (960 bytes)\r\n'
 'archiving shutdown_rp0_20230914055929.log (1461 bytes)\r\n'
 'archiving repm_pman_R0-0.4730_0.20230913140333.bin.gz (2564 bytes)\r\n'
 'archiving psvp_R0-0.3137_0.20230913140329.bin.gz (1882 bytes)\r\n'
 'archiving cli_agent_pman_R0-0.4958_0.20230913140333.bin.gz (3112 bytes)\r\n'
 'archiving autodns_pman_R0-0.4258_0.20230913140332.bin.gz (2590 bytes)\r\n'
 'archiving kernel_ftrace_log_R0-0.11650_0.20230913140352.bin.gz (1750 '
 'bytes)\r\n'
 'archiving plogd_pman_R0-0.5506_0.20230913140334.bin.gz (2569 bytes)\r\n'
 'archiving smand_pman_R0-0.5766_1.20230913140335.bin.gz (1120 bytes)\r\n'
 'archiving btman_pman_R0-0.5880_1.20230913140335.bin.gz (1205 bytes)\r\n'
 'archiving oom_R0-0.6485_0.20230913140337.bin.gz (635 bytes)\r\n'
 'archiving iptbl_R0-0.7268_0.20230913140341.bin.gz (630 bytes)\r\n'
 'archiving binos_R0-0.7482_0.20230913140341.bin.gz (835 bytes)\r\n'
 'archiving selinux_smu_R0-0.11591_0.20230913140352.bin.gz (745 bytes)\r\n'
 'archiving emd_0-0.19570_0.20230914062807.bin.gz (5385 bytes)\r\n'
 'archiving inst_rollback_timer_R0-0.11775_0.20230913140352.bin.gz (650 '
 'bytes)\r\n'
 'archiving cmand_R0-0.3562_0.20230913140352.bin.gz (17628 bytes)\r\n'
 'archiving cck_qat_R0-0.3680_0.20230913140353.bin.gz (3173 bytes)\r\n'
 'archiving sec_key_agent_R0-0.4021_0.20230913140354.bin.gz (4369 bytes)\r\n'
 'archiving ofa_R0-0.4145_0.20230913140354.bin.gz (2213 bytes)\r\n'
 'archiving pistisd_R0-0.13440_0.20230913140354.bin.gz (13849 bytes)\r\n'
 'archiving autodns_R0-0.4266_0.20230913140354.bin.gz (1087 bytes)\r\n'
 'archiving tamd_proc_R0-0.4379_0.20230913140355.bin.gz (2431 bytes)\r\n'
 'archiving tams_proc_R0-0.4494_0.20230913140355.bin.gz (2842 bytes)\r\n'
 'archiving tam_svcs_esg_cfg_R0-0.4607_0.20230913140355.bin.gz (2075 bytes)\r\n'
 'archiving lman_R0-0.14229_0.20230913140355.bin.gz (3679 bytes)\r\n'
 'archiving repm_R0-0.4737_0.20230913140356.bin.gz (4991 bytes)\r\n'
 'archiving dbm_R0-0.4851_0.20230913140356.bin.gz (14140 bytes)\r\n'
 'archiving cli_agent_R0-0.4964_0.20230913140356.bin.gz (6241 bytes)\r\n'
 'archiving smd_R0-0.5079_0.20230913140356.bin.gz (19358 bytes)\r\n'
 'archiving emd_R0-0.5242_0.20230913140356.bin.gz (12230 bytes)\r\n'
 'archiving fman_rp_R0-0.5375_0.20230913140357.bin.gz (7865 bytes)\r\n'
 'archiving psd_R0-0.5632_0.20230913140357.bin.gz (3909 bytes)\r\n'
 'archiving periodic_sh_pman_R0-0.15611_0.20230913140358.bin.gz (3701 '
 'bytes)\r\n'
 'archiving pvp_R0-0.3202_1.20230913140358.bin.gz (11508 bytes)\r\n'
 'archiving sort_files_by_inode_sh_pman_R0-0.15756_0.20230913140358.bin.gz '
 '(5883 bytes)\r\n'
 'archiving smand_R0-0.5773_1.20230913140409.bin.gz (30825 bytes)\r\n'
 'archiving shutdown_journal_rp0_20230913134959.log (18563 bytes)\r\n'
 'archiving reflector_R0-0.6983_3.20230913140410.bin.gz (615 bytes)\r\n'
 'archiving ezman_0-0.19789_0.20230914062807.bin.gz (4434 bytes)\r\n'
 'archiving hman_0-0.20342_0.20230914062808.bin.gz (10468 bytes)\r\n'
 'archiving paed_pman_R0-0.25470_0.20230913140453.bin.gz (5571 bytes)\r\n'
 'archiving IOSRP_R0-0.3451_5.20230913152041.bin.gz (16689 bytes)\r\n'
 'archiving droputil_R0-0.6842_114.20230913165053.bin.gz (781 bytes)\r\n'
 'archiving hman_pman_R0-0.6015_1.20230913220116.bin.gz (1087 bytes)\r\n'
 'archiving hman_R0-0.6021_2.20230914013408.bin.gz (49332 bytes)\r\n'
 'archiving paed_R0-0.27267_3.20230914031512.bin.gz (27907 bytes)\r\n'
 'archiving plogd_R0-0.5512_5.20230914040510.bin.gz (1851 bytes)\r\n'
 'archiving service_mgr_R0-0.3798_132.20230914055256.bin.gz (46328 bytes)\r\n'
 'archiving btman_R0-0.5887_55.20230914055659.bin.gz (11405 bytes)\r\n'
 'archiving utf_R0-0.5887_6688.20230914055921.bin.gz (559536 bytes)\r\n'
 'archiving install_mgr_R0-0.12656_133649.20230914055926.bin.gz (31347 '
 'bytes)\r\n'
 'archiving nginx_pman_R0-0.26376_5.20230914055927.bin.gz (474 bytes)\r\n'
 'archiving lman_pman_R0-0.14221_1.20230914055927.bin.gz (993 bytes)\r\n'
 'archiving auto_upgrade_client_sh_pman_R0-0.15319_3.20230914055927.bin.gz '
 '(564 bytes)\r\n'
 'archiving install_mgr_pman_R0-0.12649_1.20230914055927.bin.gz (1017 '
 'bytes)\r\n'
 'archiving psd_pman_R0-0.5625_1.20230914055927.bin.gz (978 bytes)\r\n'
 'archiving emd_pman_R0-0.5236_1.20230914055927.bin.gz (934 bytes)\r\n'
 'archiving fman_rp_pman_R0-0.5365_1.20230914055927.bin.gz (961 bytes)\r\n'
 'archiving sessmgrd_pman_R0-0.5072_1.20230914055927.bin.gz (949 bytes)\r\n'
 'archiving ofa_pman_R0-0.4139_1.20230914055927.bin.gz (929 bytes)\r\n'
 'archiving keyman_pman_R0-0.4015_1.20230914055927.bin.gz (944 bytes)\r\n'
 'archiving service_mgr_pman_R0-0.3791_1.20230914055927.bin.gz (970 bytes)\r\n'
 'archiving dbm_pman_R0-0.4844_1.20230914055927.bin.gz (926 bytes)\r\n'
 'archiving cck_qat_pman_R0-0.3673_1.20230914055927.bin.gz (951 bytes)\r\n'
 'archiving pistisd_pman_R0-0.13432_1.20230914055928.bin.gz (1024 bytes)\r\n'
 'archiving tam_svcs_esg_cfg_pman_R0-0.4601_1.20230914055929.bin.gz (991 '
 'bytes)\r\n'
 'archiving tamd_proc_pman_R0-0.4372_1.20230914055929.bin.gz (997 bytes)\r\n'
 'archiving tams_proc_pman_R0-0.4487_1.20230914055929.bin.gz (942 bytes)\r\n'
 'archiving shutdown_journal_rp0_20230914055932.log (18000 bytes)\r\n'
 'archiving shutdown_cc0_20230914060728.log (705 bytes)\r\n'
 'archiving cyaninit_R0-0.6053_0.20230914060312.bin.gz (1885 bytes)\r\n'
 'archiving shutdown_fp0_20230914060729.log (633 bytes)\r\n'
 'archiving pvp_F0-0.17513_0.20230914060339.bin.gz (5573 bytes)\r\n'
 'archiving pvp_0-0.19246_0.20230914060344.bin.gz (5452 bytes)\r\n'
 'archiving emd_0-0.19845_0.20230914060344.bin.gz (3797 bytes)\r\n'
 'archiving ezman_0-0.20062_0.20230914060345.bin.gz (4447 bytes)\r\n'
 'archiving hman_0-0.20604_0.20230914060346.bin.gz (3249 bytes)\r\n'
 'archiving cmcc_0-0.20712_0.20230914060346.bin.gz (6194 bytes)\r\n'
 'archiving btman_pman_0-0.20813_1.20230914060346.bin.gz (1262 bytes)\r\n'
 'archiving shutdown_fp0_20230913140010.log (633 bytes)\r\n'
 'archiving btman_0-0.20819_0.20230914060346.bin.gz (8292 bytes)\r\n'
 'archiving IOSCC_0-1.22004_0.20230914060348.bin.gz (6304 bytes)\r\n'
 'archiving IOSCC_0-0.21671_0.20230914060348.bin.gz (7040 bytes)\r\n'
 'archiving IOSCC_0-2.22337_0.20230914060349.bin.gz (7230 bytes)\r\n'
 'archiving mcpcc_lc_ms_pman_0-2.22330_4.20230914060402.bin.gz (1572 bytes)\r\n'
 'archiving ezman_pman_0-0.20055_1.20230914060728.bin.gz (997 bytes)\r\n'
 'archiving emd_pman_0-0.19836_1.20230914060728.bin.gz (969 bytes)\r\n'
 'archiving hman_pman_0-0.20597_1.20230914060728.bin.gz (971 bytes)\r\n'
 'archiving cmcc_pman_0-0.20705_1.20230914060728.bin.gz (991 bytes)\r\n'
 'archiving mcpcc_lc_ms_pman_0-1.21997_4.20230914060728.bin.gz (841 bytes)\r\n'
 'archiving mcpcc_lc_ms_pman_0-0.21660_6.20230914060728.bin.gz (392 bytes)\r\n'
 'archiving cmcc_0-0.20450_0.20230914062808.bin.gz (6312 bytes)\r\n'
 'archiving cpp_driver_pman_F0-0.18183_1.20230914060340.bin.gz (1162 bytes)\r\n'
 'archiving service_mgr_F0-0.17676_0.20230914060339.bin.gz (5745 bytes)\r\n'
 'archiving cpp_cdm_F0-0.17983_0.20230914060340.bin.gz (3174 bytes)\r\n'
 'archiving cpp_ha_top_level_server_pman_F0-0.18079_1.20230914060340.bin.gz '
 '(1191 bytes)\r\n'
 'archiving cpp_ha_F0-0.18086_0.20230914060340.bin.gz (4951 bytes)\r\n'
 'archiving cpp_sp_svr_pman_F0-0.18286_1.20230914060728.bin.gz (1331 bytes)\r\n'
 'archiving cpp_driver_F0-0.18192_0.20230914060340.bin.gz (3912 bytes)\r\n'
 'archiving cpp_sp_F0-0.18293_0.20230914060340.bin.gz (4356 bytes)\r\n'
 'archiving emd_F0-0.18499_0.20230914060340.bin.gz (4303 bytes)\r\n'
 'archiving hman_F0-0.18705_0.20230914060341.bin.gz (3244 bytes)\r\n'
 'archiving cman_fp_F0-0.18809_0.20230914060341.bin.gz (3999 bytes)\r\n'
 'archiving cpp_stats_F0-0.17879_0.20230914060341.bin.gz (3973 bytes)\r\n'
 'archiving btman_pman_F0-0.18905_1.20230914060341.bin.gz (1260 bytes)\r\n'
 'archiving btman_F0-0.18912_0.20230914060341.bin.gz (8060 bytes)\r\n'
 'archiving shutdown_rp0_20230913140011.log (1461 bytes)\r\n'
 'archiving cpp_cp_F0-0.18396_0.20230914060342.bin.gz (18947 bytes)\r\n'
 'archiving fman_fp_F0-0.18605_0.20230914060343.bin.gz (11699 bytes)\r\n'
 'archiving memmon_log_20230914_080612_UTC_1694678772.tar.gz (31076 bytes)\r\n'
 'archiving fman_fp_image_pman_F0-0.18595_1.20230914060728.bin.gz (1395 '
 'bytes)\r\n'
 'archiving cpp_cp_svr_pman_F0-0.18389_1.20230914060728.bin.gz (1449 bytes)\r\n'
 'archiving cpp_cdm_svr_pman_F0-0.17976_1.20230914060728.bin.gz (1075 '
 'bytes)\r\n'
 'archiving cpp_stats_svr_pman_F0-0.17873_1.20230914060728.bin.gz (1062 '
 'bytes)\r\n'
 'archiving service_mgr_pman_F0-0.17667_1.20230914060728.bin.gz (1022 '
 'bytes)\r\n'
 'archiving emd_pman_F0-0.18492_1.20230914060728.bin.gz (962 bytes)\r\n'
 'archiving cman_fp_pman_F0-0.18802_1.20230914060728.bin.gz (989 bytes)\r\n'
 'archiving hman_pman_F0-0.18698_1.20230914060729.bin.gz (966 bytes)\r\n'
 'archiving shutdown_rp0_20230914060730.log (1461 bytes)\r\n'
 'archiving repm_pman_R0-0.4687_0.20230914060309.bin.gz (2562 bytes)\r\n'
 'archiving psvp_R0-0.3094_0.20230914060306.bin.gz (1894 bytes)\r\n'
 'archiving cli_agent_pman_R0-0.4915_0.20230914060310.bin.gz (3114 bytes)\r\n'
 'archiving autodns_pman_R0-0.4215_0.20230914060309.bin.gz (2579 bytes)\r\n'
 'archiving kernel_ftrace_log_R0-0.11709_0.20230914060328.bin.gz (1747 '
 'bytes)\r\n'
 'archiving plogd_pman_R0-0.5460_0.20230914060311.bin.gz (2567 bytes)\r\n'
 'archiving smand_pman_R0-0.5720_1.20230914060311.bin.gz (1110 bytes)\r\n'
 'archiving btman_pman_R0-0.5840_1.20230914060312.bin.gz (1141 bytes)\r\n'
 'archiving oom_R0-0.6430_0.20230914060314.bin.gz (632 bytes)\r\n'
 'archiving iptbl_R0-0.7206_0.20230914060318.bin.gz (631 bytes)\r\n'
 'archiving binos_R0-0.7416_0.20230914060318.bin.gz (835 bytes)\r\n'
 'archiving selinux_smu_R0-0.11683_0.20230914060328.bin.gz (747 bytes)\r\n'
 'archiving inst_rollback_timer_R0-0.11851_0.20230914060329.bin.gz (651 '
 'bytes)\r\n'
 'archiving IOSRP_R0-0.3408_0.20230914060329.bin.gz (105630 bytes)\r\n'
 'archiving cmand_R0-0.3520_0.20230914060329.bin.gz (15570 bytes)\r\n'
 'archiving psd_R0-0.5586_0.20230914060330.bin.gz (7050 bytes)\r\n'
 'archiving vman_R0-0.12577_0.20230914060330.bin.gz (5405 bytes)\r\n'
 'archiving smd_R0-0.5045_0.20230914060330.bin.gz (19397 bytes)\r\n'
 'archiving service_mgr_R0-0.3754_0.20230914060331.bin.gz (25715 bytes)\r\n'
 'archiving repm_R0-0.4694_0.20230914060331.bin.gz (4983 bytes)\r\n'
 'archiving pistisd_R0-0.13914_0.20230914060331.bin.gz (13759 bytes)\r\n'
 'archiving plogd_R0-0.5466_3.20230914060331.bin.gz (6638 bytes)\r\n'
 'archiving ofa_R0-0.4103_0.20230914060332.bin.gz (2217 bytes)\r\n'
 'archiving lman_R0-0.14270_0.20230914060332.bin.gz (3612 bytes)\r\n'
 'archiving sec_key_agent_R0-0.3979_0.20230914060332.bin.gz (4128 bytes)\r\n'
 'archiving install_mgr_R0-0.14697_0.20230914060333.bin.gz (28907 bytes)\r\n'
 'archiving hman_R0-0.6012_0.20230914060333.bin.gz (4977 bytes)\r\n'
 'archiving fman_rp_R0-0.5331_0.20230914060333.bin.gz (7661 bytes)\r\n'
 'archiving emd_R0-0.5206_0.20230914060333.bin.gz (12131 bytes)\r\n'
 'archiving shutdown_cc0_20230914062350.log (705 bytes)\r\n'
 'archiving dbm_R0-0.4808_0.20230914060333.bin.gz (13709 bytes)\r\n'
 'archiving cli_agent_R0-0.4921_0.20230914060334.bin.gz (6420 bytes)\r\n'
 'archiving cck_qat_R0-0.3637_0.20230914060334.bin.gz (3064 bytes)\r\n'
 'archiving btman_R0-0.5849_0.20230914060334.bin.gz (12583 bytes)\r\n'
 'archiving utf_R0-0.5849_0.20230914060334.bin.gz (619129 bytes)\r\n'
 'archiving tams_proc_R0-0.4451_0.20230914060334.bin.gz (2846 bytes)\r\n'
 'archiving tamd_proc_R0-0.4336_0.20230914060335.bin.gz (2424 bytes)\r\n'
 'archiving periodic_sh_pman_R0-0.16295_0.20230914060335.bin.gz (3727 '
 'bytes)\r\n'
 'archiving sort_files_by_inode_sh_pman_R0-0.16000_0.20230914060335.bin.gz '
 '(3600 bytes)\r\n'
 'archiving tam_svcs_esg_cfg_R0-0.4564_0.20230914060335.bin.gz (2090 bytes)\r\n'
 'archiving autodns_R0-0.4222_0.20230914060336.bin.gz (1063 bytes)\r\n'
 'archiving pvp_R0-0.3159_1.20230914060336.bin.gz (5077 bytes)\r\n'
 'archiving smand_R0-0.5726_1.20230914060342.bin.gz (21806 bytes)\r\n'
 'archiving reflector_R0-0.6937_3.20230914060347.bin.gz (615 bytes)\r\n'
 'archiving btman_pman_0-0.20551_1.20230914062808.bin.gz (1324 bytes)\r\n'
 'archiving btman_0-0.20557_0.20230914062808.bin.gz (20155 bytes)\r\n'
 'archiving hman_pman_R0-0.6003_1.20230914060648.bin.gz (1079 bytes)\r\n'
 'archiving droputil_R0-0.6796_11.20230914060713.bin.gz (642 bytes)\r\n'
 'archiving linux_iosd_image_pman_R0-0.3369_2.20230914060723.bin.gz (1438 '
 'bytes)\r\n'
 'archiving cmand_pman_R0-0.3513_1.20230914060727.bin.gz (957 bytes)\r\n'
 'archiving install_mgr_pman_R0-0.14691_1.20230914060728.bin.gz (1013 '
 'bytes)\r\n'
 'archiving auto_upgrade_client_sh_pman_R0-0.16934_3.20230914060728.bin.gz '
 '(567 bytes)\r\n'
 'archiving nginx_pman_R0-0.23114_5.20230914060728.bin.gz (508 bytes)\r\n'
 'archiving lman_pman_R0-0.14263_1.20230914060728.bin.gz (991 bytes)\r\n'
 'archiving psd_pman_R0-0.5579_1.20230914060728.bin.gz (989 bytes)\r\n'
 'archiving ofa_pman_R0-0.4096_1.20230914060728.bin.gz (931 bytes)\r\n'
 'archiving emd_pman_R0-0.5199_1.20230914060728.bin.gz (932 bytes)\r\n'
 'archiving keyman_pman_R0-0.3972_1.20230914060728.bin.gz (942 bytes)\r\n'
 'archiving service_mgr_pman_R0-0.3748_1.20230914060728.bin.gz (981 bytes)\r\n'
 'archiving fman_rp_pman_R0-0.5319_1.20230914060728.bin.gz (961 bytes)\r\n'
 'archiving sessmgrd_pman_R0-0.5032_1.20230914060728.bin.gz (954 bytes)\r\n'
 'archiving dbm_pman_R0-0.4801_1.20230914060728.bin.gz (930 bytes)\r\n'
 'archiving vman_pman_R0-0.12570_1.20230914060728.bin.gz (1075 bytes)\r\n'
 'archiving cck_qat_pman_R0-0.3630_1.20230914060729.bin.gz (943 bytes)\r\n'
 'archiving pistisd_pman_R0-0.13907_1.20230914060730.bin.gz (1022 bytes)\r\n'
 'archiving tam_svcs_esg_cfg_pman_R0-0.4558_1.20230914060730.bin.gz (993 '
 'bytes)\r\n'
 'archiving tamd_proc_pman_R0-0.4329_1.20230914060730.bin.gz (1007 bytes)\r\n'
 'archiving tams_proc_pman_R0-0.4444_1.20230914060730.bin.gz (943 bytes)\r\n'
 'archiving shutdown_journal_rp0_20230914060732.log (211918 bytes)\r\n'
 'archiving pvp_0-0.18855_0.20230914061143.bin.gz (5467 bytes)\r\n'
 'archiving cyaninit_R0-0.6098_0.20230914061112.bin.gz (1885 bytes)\r\n'
 'archiving btman_pman_0-0.20439_1.20230914061146.bin.gz (1320 bytes)\r\n'
 'archiving emd_0-0.19461_0.20230914061144.bin.gz (4287 bytes)\r\n'
 'archiving ezman_0-0.19677_0.20230914061145.bin.gz (4432 bytes)\r\n'
 'archiving hman_0-0.20230_0.20230914061145.bin.gz (7165 bytes)\r\n'
 'archiving cmcc_0-0.20338_0.20230914061145.bin.gz (6206 bytes)\r\n'
 'archiving shutdown_fp0_20230914062351.log (633 bytes)\r\n'
 'archiving shutdown_journal_rp0_20230913140013.log (210690 bytes)\r\n'
 'archiving btman_0-0.20445_0.20230914061146.bin.gz (12065 bytes)\r\n'
 'archiving IOSCC_0-0.21293_0.20230914061148.bin.gz (7302 bytes)\r\n'
 'archiving IOSCC_0-1.21617_0.20230914061148.bin.gz (6338 bytes)\r\n'
 'archiving IOSCC_0-2.21994_0.20230914061148.bin.gz (7134 bytes)\r\n'
 'archiving create_utm_luid_file_db_0-0.25976_0.20230914061646.bin.gz (1740 '
 'bytes)\r\n'
 'archiving mcpcc_lc_ms_pman_0-2.21987_4.20230914062232.bin.gz (1420 bytes)\r\n'
 'archiving emd_pman_0-0.19451_1.20230914062350.bin.gz (971 bytes)\r\n'
 'archiving hman_pman_0-0.20223_1.20230914062350.bin.gz (968 bytes)\r\n'
 'archiving ezman_pman_0-0.19670_1.20230914062350.bin.gz (988 bytes)\r\n'
 'archiving cmcc_pman_0-0.20331_1.20230914062350.bin.gz (990 bytes)\r\n'
 'archiving mcpcc_lc_ms_pman_0-0.21282_6.20230914062350.bin.gz (551 bytes)\r\n'
 'archiving mcpcc_lc_ms_pman_0-1.21610_4.20230914062350.bin.gz (839 bytes)\r\n'
 'archiving cpp_cdm_F0-0.17599_0.20230914061139.bin.gz (3169 bytes)\r\n'
 'archiving pvp_F0-0.17123_0.20230914061138.bin.gz (5598 bytes)\r\n'
 'archiving cpp_driver_pman_F0-0.17797_1.20230914061139.bin.gz (1163 bytes)\r\n'
 'archiving service_mgr_F0-0.17290_0.20230914061139.bin.gz (5725 bytes)\r\n'
 'archiving cpp_ha_F0-0.17700_0.20230914061139.bin.gz (5080 bytes)\r\n'
 'archiving cpp_ha_top_level_server_pman_F0-0.17693_1.20230914061139.bin.gz '
 '(1190 bytes)\r\n'
 'archiving cpp_cp_svr_pman_F0-0.18003_1.20230914062350.bin.gz (1447 bytes)\r\n'
 'archiving cpp_driver_F0-0.17804_0.20230914061140.bin.gz (3904 bytes)\r\n'
 'archiving cpp_sp_F0-0.17907_0.20230914061140.bin.gz (4361 bytes)\r\n'
 'archiving emd_F0-0.18115_0.20230914061140.bin.gz (4808 bytes)\r\n'
 'archiving hman_F0-0.18320_0.20230914061140.bin.gz (7283 bytes)\r\n'
 'archiving cman_fp_F0-0.18424_0.20230914061141.bin.gz (3990 bytes)\r\n'
 'archiving cpp_stats_F0-0.17494_0.20230914061141.bin.gz (3957 bytes)\r\n'
 'archiving btman_pman_F0-0.18519_1.20230914061141.bin.gz (1319 bytes)\r\n'
 'archiving btman_F0-0.18526_0.20230914061141.bin.gz (11742 bytes)\r\n'
 'archiving cpp_cp_F0-0.18010_0.20230914061142.bin.gz (18997 bytes)\r\n'
 'archiving fman_fp_F0-0.18224_0.20230914061142.bin.gz (11692 bytes)\r\n'
 'archiving shutdown_rp0_20230914062352.log (1461 bytes)\r\n'
 'archiving create_utm_luid_file_db_F0-0.25846_0.20230914061641.bin.gz (1744 '
 'bytes)\r\n'
 'archiving fman_fp_image_pman_F0-0.18210_1.20230914062350.bin.gz (1393 '
 'bytes)\r\n'
 'archiving cpp_sp_svr_pman_F0-0.17900_1.20230914062350.bin.gz (1330 bytes)\r\n'
 'archiving cpp_cdm_svr_pman_F0-0.17590_1.20230914062350.bin.gz (1068 '
 'bytes)\r\n'
 'archiving cpp_stats_svr_pman_F0-0.17487_1.20230914062350.bin.gz (1057 '
 'bytes)\r\n'
 'archiving cman_fp_pman_F0-0.18416_1.20230914062350.bin.gz (996 bytes)\r\n'
 'archiving service_mgr_pman_F0-0.17281_1.20230914062350.bin.gz (1022 '
 'bytes)\r\n'
 'archiving emd_pman_F0-0.18107_1.20230914062350.bin.gz (963 bytes)\r\n'
 'archiving hman_pman_F0-0.18313_1.20230914062351.bin.gz (965 bytes)\r\n'
 'archiving btman_rotate_immediate_R0-0.31039_0.20230914062351.bin.gz (4673 '
 'bytes)\r\n'
 'archiving repm_pman_R0-0.4731_0.20230914061109.bin.gz (2554 bytes)\r\n'
 'archiving psvp_R0-0.3138_0.20230914061106.bin.gz (1891 bytes)\r\n'
 'archiving cli_agent_pman_R0-0.4959_0.20230914061110.bin.gz (3111 bytes)\r\n'
 'archiving autodns_pman_R0-0.4259_0.20230914061108.bin.gz (2579 bytes)\r\n'
 'archiving kernel_ftrace_log_R0-0.11767_0.20230914061128.bin.gz (1749 '
 'bytes)\r\n'
 'archiving plogd_pman_R0-0.5505_0.20230914061110.bin.gz (2568 bytes)\r\n'
 'archiving smand_pman_R0-0.5765_1.20230914061111.bin.gz (1119 bytes)\r\n'
 'archiving btman_pman_R0-0.5879_1.20230914061111.bin.gz (1207 bytes)\r\n'
 'archiving oom_R0-0.6466_0.20230914061114.bin.gz (634 bytes)\r\n'
 'archiving iptbl_R0-0.7246_0.20230914061117.bin.gz (630 bytes)\r\n'
 'archiving binos_R0-0.7464_0.20230914061118.bin.gz (836 bytes)\r\n'
 'archiving selinux_smu_R0-0.11722_0.20230914061128.bin.gz (743 bytes)\r\n'
 'archiving create_utm_luid_file_db_R0-0.25446_0.20230914061635.bin.gz (1749 '
 'bytes)\r\n'
 'archiving inst_rollback_timer_R0-0.11895_0.20230914061128.bin.gz (648 '
 'bytes)\r\n'
 'archiving cmand_R0-0.3563_0.20230914061129.bin.gz (15839 bytes)\r\n'
 'archiving cck_qat_R0-0.3680_0.20230914061129.bin.gz (3175 bytes)\r\n'
 'archiving install_mgr_R0-0.12781_0.20230914061130.bin.gz (30355 bytes)\r\n'
 'archiving sec_key_agent_R0-0.4023_0.20230914061130.bin.gz (4127 bytes)\r\n'
 'archiving IOSRP_R0-0.3455_1.20230914061130.bin.gz (29247 bytes)\r\n'
 'archiving ofa_R0-0.4147_0.20230914061130.bin.gz (2216 bytes)\r\n'
 'archiving pistisd_R0-0.13565_0.20230914061131.bin.gz (13856 bytes)\r\n'
 'archiving autodns_R0-0.4266_0.20230914061131.bin.gz (1064 bytes)\r\n'
 'archiving tamd_proc_R0-0.4380_0.20230914061131.bin.gz (2432 bytes)\r\n'
 'archiving tams_proc_R0-0.4495_0.20230914061131.bin.gz (2838 bytes)\r\n'
 'archiving tam_svcs_esg_cfg_R0-0.4608_0.20230914061131.bin.gz (2073 bytes)\r\n'
 'archiving lman_R0-0.14354_0.20230914061132.bin.gz (3614 bytes)\r\n'
 'archiving repm_R0-0.4738_0.20230914061132.bin.gz (4999 bytes)\r\n'
 'archiving dbm_R0-0.4852_0.20230914061132.bin.gz (15084 bytes)\r\n'
 'archiving cli_agent_R0-0.4966_0.20230914061133.bin.gz (6250 bytes)\r\n'
 'archiving smd_R0-0.5080_0.20230914061133.bin.gz (19501 bytes)\r\n'
 'archiving emd_R0-0.5244_0.20230914061133.bin.gz (12276 bytes)\r\n'
 'archiving fman_rp_R0-0.5373_0.20230914061133.bin.gz (7769 bytes)\r\n'
 'archiving plogd_R0-0.5511_3.20230914061134.bin.gz (5987 bytes)\r\n'
 'archiving psd_R0-0.5630_0.20230914061134.bin.gz (3865 bytes)\r\n'
 'archiving periodic_sh_pman_R0-0.15726_0.20230914061134.bin.gz (3727 '
 'bytes)\r\n'
 'archiving btman_R0-0.5884_0.20230914061135.bin.gz (17024 bytes)\r\n'
 'archiving sort_files_by_inode_sh_pman_R0-0.15881_0.20230914061134.bin.gz '
 '(3591 bytes)\r\n'
 'archiving utf_R0-0.5884_0.20230914061135.bin.gz (739964 bytes)\r\n'
 'archiving hman_R0-0.6035_0.20230914061135.bin.gz (9082 bytes)\r\n'
 'archiving pvp_R0-0.3203_1.20230914061135.bin.gz (4862 bytes)\r\n'
 'archiving smand_R0-0.5771_1.20230914061145.bin.gz (22086 bytes)\r\n'
 'archiving reflector_R0-0.6982_3.20230914061146.bin.gz (615 bytes)\r\n'
 'archiving IOSCC_0-1.21729_0.20230914062811.bin.gz (6354 bytes)\r\n'
 'archiving IOSCC_0-0.21406_0.20230914062811.bin.gz (7325 bytes)\r\n'
 'archiving hman_pman_R0-0.6029_1.20230914061847.bin.gz (1082 bytes)\r\n'
 'archiving paed_R0-0.25973_0.20230914061645.bin.gz (15666 bytes)\r\n'
 'archiving install_mgr_pman_R0-0.12774_1.20230914062350.bin.gz (1020 '
 'bytes)\r\n'
 'archiving service_mgr_R0-0.3799_1.20230914062109.bin.gz (16322 bytes)\r\n'
 'archiving droputil_R0-0.6841_22.20230914062345.bin.gz (385 bytes)\r\n'
 'archiving linux_iosd_image_pman_R0-0.3413_2.20230914062345.bin.gz (1438 '
 'bytes)\r\n'
 'archiving cmand_pman_R0-0.3557_1.20230914062349.bin.gz (960 bytes)\r\n'
 'archiving nginx_pman_R0-0.23147_5.20230914062350.bin.gz (440 bytes)\r\n'
 'archiving auto_upgrade_client_sh_pman_R0-0.15444_3.20230914062350.bin.gz '
 '(566 bytes)\r\n'
 'archiving lman_pman_R0-0.14347_1.20230914062350.bin.gz (980 bytes)\r\n'
 'archiving keyman_pman_R0-0.4016_1.20230914062350.bin.gz (946 bytes)\r\n'
 'archiving psd_pman_R0-0.5624_1.20230914062350.bin.gz (977 bytes)\r\n'
 'archiving emd_pman_R0-0.5237_1.20230914062350.bin.gz (933 bytes)\r\n'
 'archiving ofa_pman_R0-0.4140_1.20230914062350.bin.gz (936 bytes)\r\n'
 'archiving tam_svcs_esg_cfg_pman_R0-0.4602_1.20230914062352.bin.gz (991 '
 'bytes)\r\n'
 'archiving service_mgr_pman_R0-0.3792_1.20230914062350.bin.gz (967 bytes)\r\n'
 'archiving fman_rp_pman_R0-0.5364_1.20230914062350.bin.gz (959 bytes)\r\n'
 'archiving sessmgrd_pman_R0-0.5073_1.20230914062350.bin.gz (954 bytes)\r\n'
 'archiving dbm_pman_R0-0.4845_1.20230914062350.bin.gz (930 bytes)\r\n'
 'archiving cck_qat_pman_R0-0.3674_1.20230914062351.bin.gz (946 bytes)\r\n'
 'archiving pistisd_pman_R0-0.13558_1.20230914062351.bin.gz (1020 bytes)\r\n'
 'archiving shutdown_journal_rp0_20230914062354.log (18825 bytes)\r\n'
 'archiving tamd_proc_pman_R0-0.4373_1.20230914062352.bin.gz (1008 bytes)\r\n'
 'archiving tams_proc_pman_R0-0.4488_1.20230914062352.bin.gz (946 bytes)\r\n'
 'archiving IOSCC_0-2.22107_0.20230914062811.bin.gz (7120 bytes)\r\n'
 'archiving btman_rotate_immediate_R0-0.31141_0.20230914062352.bin.gz (8050 '
 'bytes)\r\n'
 'archiving cyaninit_R0-0.6091_0.20230914062734.bin.gz (1889 bytes)\r\n'
 'archiving mcpcc_lc_ms_pman_0-2.22100_4.20230914070019.bin.gz (1382 bytes)\r\n'
 'archiving create_utm_luid_file_db_0-0.26684_0.20230914063308.bin.gz (1744 '
 'bytes)\r\n'
 'archiving ezman_pman_0-0.19782_1.20230914070149.bin.gz (1000 bytes)\r\n'
 'archiving emd_pman_0-0.19563_1.20230914070149.bin.gz (973 bytes)\r\n'
 'archiving hman_pman_0-0.20335_1.20230914070149.bin.gz (965 bytes)\r\n'
 'archiving cmcc_pman_0-0.20443_1.20230914070149.bin.gz (994 bytes)\r\n'
 'archiving mcpcc_lc_ms_pman_0-1.21722_4.20230914070149.bin.gz (842 bytes)\r\n'
 'archiving mcpcc_lc_ms_pman_0-0.21394_6.20230914070149.bin.gz (553 bytes)\r\n'
 'archiving cpp_ha_top_level_server_pman_F0-0.17805_1.20230914062802.bin.gz '
 '(1189 bytes)\r\n'
 'archiving btman_rotate_immediate_R0-0.20024_0.20230914070149.bin.gz (3819 '
 'bytes)\r\n'
 'archiving pvp_F0-0.17235_0.20230914062801.bin.gz (5590 bytes)\r\n'
 'archiving service_mgr_F0-0.17402_0.20230914062801.bin.gz (5735 bytes)\r\n'
 'archiving cpp_driver_F0-0.17918_0.20230914062802.bin.gz (3918 bytes)\r\n'
 'archiving cpp_cdm_F0-0.17708_0.20230914062802.bin.gz (3168 bytes)\r\n'
 'archiving cpp_ha_F0-0.17812_0.20230914062802.bin.gz (5216 bytes)\r\n'
 'archiving fman_fp_image_pman_F0-0.18322_1.20230914070149.bin.gz (1392 '
 'bytes)\r\n'
 'archiving cpp_driver_pman_F0-0.17909_1.20230914062802.bin.gz (1169 bytes)\r\n'
 'archiving cpp_sp_F0-0.18018_0.20230914062802.bin.gz (4367 bytes)\r\n'
 'archiving emd_F0-0.18225_0.20230914062803.bin.gz (5913 bytes)\r\n'
 'archiving hman_F0-0.18432_0.20230914062803.bin.gz (10525 bytes)\r\n'
 'archiving cman_fp_F0-0.18535_0.20230914062803.bin.gz (3988 bytes)\r\n'
 'archiving cpp_stats_F0-0.17606_0.20230914062803.bin.gz (3966 bytes)\r\n'
 'archiving btman_pman_F0-0.18631_1.20230914062804.bin.gz (1320 bytes)\r\n'
 'archiving btman_F0-0.18638_0.20230914062804.bin.gz (19814 bytes)\r\n'
 'archiving cpp_cp_F0-0.18122_0.20230914062804.bin.gz (18907 bytes)\r\n'
 'archiving fman_fp_F0-0.18334_0.20230914062805.bin.gz (11708 bytes)\r\n'
 'archiving shutdown_rp0_20230914070150.log (1461 bytes)\r\n'
 'archiving create_utm_luid_file_db_F0-0.26554_0.20230914063304.bin.gz (1746 '
 'bytes)\r\n'
 'archiving cpp_sp_svr_pman_F0-0.18012_1.20230914070149.bin.gz (1331 bytes)\r\n'
 'archiving emd_pman_F0-0.18218_1.20230914070149.bin.gz (968 bytes)\r\n'
 'archiving cpp_cp_svr_pman_F0-0.18115_1.20230914070149.bin.gz (1451 bytes)\r\n'
 'archiving cpp_cdm_svr_pman_F0-0.17702_1.20230914070149.bin.gz (1068 '
 'bytes)\r\n'
 'archiving cpp_stats_svr_pman_F0-0.17599_1.20230914070149.bin.gz (1075 '
 'bytes)\r\n'
 'archiving cman_fp_pman_F0-0.18528_1.20230914070149.bin.gz (992 bytes)\r\n'
 'archiving service_mgr_pman_F0-0.17393_1.20230914070149.bin.gz (1025 '
 'bytes)\r\n'
 'archiving hman_pman_F0-0.18425_1.20230914070149.bin.gz (968 bytes)\r\n'
 'archiving btman_rotate_immediate_R0-0.20143_0.20230914070150.bin.gz (4678 '
 'bytes)\r\n'
 'archiving repm_pman_R0-0.4726_0.20230914062732.bin.gz (2572 bytes)\r\n'
 'archiving psvp_R0-0.3133_0.20230914062728.bin.gz (1890 bytes)\r\n'
 'archiving cli_agent_pman_R0-0.4954_0.20230914062732.bin.gz (3116 bytes)\r\n'
 'archiving autodns_pman_R0-0.4254_0.20230914062731.bin.gz (2588 bytes)\r\n'
 'archiving kernel_ftrace_log_R0-0.11760_0.20230914062751.bin.gz (1749 '
 'bytes)\r\n'
 'archiving plogd_pman_R0-0.5498_0.20230914062733.bin.gz (2563 bytes)\r\n'
 'archiving smand_pman_R0-0.5758_1.20230914062734.bin.gz (1120 bytes)\r\n'
 'archiving btman_pman_R0-0.5881_1.20230914062734.bin.gz (1209 bytes)\r\n'
 'archiving oom_R0-0.6464_0.20230914062736.bin.gz (634 bytes)\r\n'
 'archiving iptbl_R0-0.7244_0.20230914062740.bin.gz (628 bytes)\r\n'
 'archiving binos_R0-0.7473_0.20230914062740.bin.gz (836 bytes)\r\n'
 'archiving selinux_smu_R0-0.11718_0.20230914062751.bin.gz (745 bytes)\r\n'
 'archiving create_utm_luid_file_db_R0-0.26153_0.20230914063258.bin.gz (1751 '
 'bytes)\r\n'
 'archiving inst_rollback_timer_R0-0.11892_0.20230914062751.bin.gz (649 '
 'bytes)\r\n'
 'archiving cmand_R0-0.3558_0.20230914062752.bin.gz (17187 bytes)\r\n'
 'archiving cck_qat_R0-0.3676_0.20230914062752.bin.gz (3178 bytes)\r\n'
 'archiving sec_key_agent_R0-0.4018_0.20230914062753.bin.gz (4323 bytes)\r\n'
 'archiving IOSRP_R0-0.3442_1.20230914062753.bin.gz (35313 bytes)\r\n'
 'archiving ofa_R0-0.4142_0.20230914062753.bin.gz (2215 bytes)\r\n'
 'archiving pistisd_R0-0.13558_0.20230914062753.bin.gz (13863 bytes)\r\n'
 'archiving autodns_R0-0.4261_0.20230914062754.bin.gz (1081 bytes)\r\n'
 'archiving tamd_proc_R0-0.4375_0.20230914062754.bin.gz (2427 bytes)\r\n'
 'archiving tams_proc_R0-0.4490_0.20230914062754.bin.gz (2817 bytes)\r\n'
 'archiving tam_svcs_esg_cfg_R0-0.4603_0.20230914062754.bin.gz (2074 bytes)\r\n'
 'archiving lman_R0-0.14347_0.20230914062755.bin.gz (3664 bytes)\r\n'
 'archiving repm_R0-0.4733_0.20230914062755.bin.gz (4991 bytes)\r\n'
 'archiving dbm_R0-0.4846_0.20230914062755.bin.gz (15057 bytes)\r\n'
 'archiving cli_agent_R0-0.4962_0.20230914062755.bin.gz (6256 bytes)\r\n'
 'archiving smd_R0-0.5109_0.20230914062756.bin.gz (19790 bytes)\r\n'
 'archiving emd_R0-0.5244_0.20230914062756.bin.gz (12271 bytes)\r\n'
 'archiving fman_rp_R0-0.5369_0.20230914062756.bin.gz (7767 bytes)\r\n'
 'archiving plogd_R0-0.5504_3.20230914062756.bin.gz (6653 bytes)\r\n'
 'archiving psd_R0-0.5625_0.20230914062756.bin.gz (3865 bytes)\r\n'
 'archiving periodic_sh_pman_R0-0.15726_0.20230914062757.bin.gz (3732 '
 'bytes)\r\n'
 'archiving btman_R0-0.5900_0.20230914062758.bin.gz (30865 bytes)\r\n'
 'archiving sort_files_by_inode_sh_pman_R0-0.15874_0.20230914062757.bin.gz '
 '(3591 bytes)\r\n'
 'archiving hman_R0-0.6064_0.20230914062758.bin.gz (12489 bytes)\r\n'
 'archiving pvp_R0-0.3198_1.20230914062758.bin.gz (9191 bytes)\r\n'
 'archiving smand_R0-0.5764_1.20230914062808.bin.gz (22140 bytes)\r\n'
 'archiving reflector_R0-0.6975_3.20230914062809.bin.gz (619 bytes)\r\n'
 'archiving IOSRP_R0-1.15254_0.20230914070049.bin.gz (56456 bytes)\r\n'
 'archiving paed_R0-0.26681_0.20230914063308.bin.gz (15670 bytes)\r\n'
 'archiving install_mgr_R0-0.12774_200.20230914070148.bin.gz (31421 bytes)\r\n'
 'archiving service_mgr_R0-0.3793_3.20230914065643.bin.gz (29565 bytes)\r\n'
 'archiving psd_R0-1.16970_0.20230914070050.bin.gz (2974 bytes)\r\n'
 'archiving fman_rp_R0-1.16831_0.20230914070050.bin.gz (6843 bytes)\r\n'
 'archiving droputil_R0-0.6834_47.20230914070138.bin.gz (495 bytes)\r\n'
 'archiving utf_R0-0.5900_10.20230914070146.bin.gz (329775 bytes)\r\n'
 'archiving cmand_pman_R0-0.3552_1.20230914070148.bin.gz (959 bytes)\r\n'
 'archiving linux_iosd_image_pman_R0-0.3408_3.20230914070148.bin.gz (1087 '
 'bytes)\r\n'
 'archiving shutdown_journal_rp0_20230914070153.log (20467 bytes)\r\n'
 'archiving auto_upgrade_client_sh_pman_R0-0.15437_3.20230914070148.bin.gz '
 '(568 bytes)\r\n'
 'archiving nginx_pman_R0-0.23378_5.20230914070148.bin.gz (440 bytes)\r\n'
 'archiving install_mgr_pman_R0-0.12767_1.20230914070148.bin.gz (1025 '
 'bytes)\r\n'
 'archiving psd_pman_R0-0.5617_1.20230914070148.bin.gz (988 bytes)\r\n'
 'archiving lman_pman_R0-0.14340_1.20230914070148.bin.gz (978 bytes)\r\n'
 'archiving emd_pman_R0-0.5237_1.20230914070148.bin.gz (936 bytes)\r\n'
 'archiving keyman_pman_R0-0.4011_1.20230914070149.bin.gz (947 bytes)\r\n'
 'archiving ofa_pman_R0-0.4135_1.20230914070149.bin.gz (931 bytes)\r\n'
 'archiving fman_rp_pman_R0-0.5357_1.20230914070149.bin.gz (960 bytes)\r\n'
 'archiving service_mgr_pman_R0-0.3787_1.20230914070149.bin.gz (971 bytes)\r\n'
 'archiving sessmgrd_pman_R0-0.5102_1.20230914070149.bin.gz (949 bytes)\r\n'
 'archiving dbm_pman_R0-0.4840_1.20230914070149.bin.gz (929 bytes)\r\n'
 'archiving cck_qat_pman_R0-0.3669_1.20230914070149.bin.gz (946 bytes)\r\n'
 'archiving pistisd_pman_R0-0.13551_1.20230914070150.bin.gz (1026 bytes)\r\n'
 'archiving tam_svcs_esg_cfg_pman_R0-0.4597_1.20230914070150.bin.gz (1001 '
 'bytes)\r\n'
 'archiving tamd_proc_pman_R0-0.4368_1.20230914070150.bin.gz (993 bytes)\r\n'
 'archiving tams_proc_pman_R0-0.4483_1.20230914070150.bin.gz (940 bytes)\r\n'
 'archiving hman_pman_R0-0.6058_1.20230914070150.bin.gz (974 bytes)\r\n'
 'archiving btman_rotate_immediate_R0-0.20245_0.20230914070151.bin.gz (9098 '
 'bytes)\r\n'
 'archiving cyaninit_R0-0.6101_0.20230914070532.bin.gz (1888 bytes)')
        self.assertEqual(result, expected_output)
