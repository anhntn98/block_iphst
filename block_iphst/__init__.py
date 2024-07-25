from netbox.plugins import PluginConfig


class BlockIpHstConfig(PluginConfig):
    name = 'block_iphst'
    verbose_name = ' Block IP zone HST'
    description = ''
    version = '0.2.6'


config = BlockIpHstConfig
