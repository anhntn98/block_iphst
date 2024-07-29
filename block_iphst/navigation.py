from netbox.plugins import PluginMenuButton, PluginMenuItem

bl_items = PluginMenuItem(
        link='plugins:block_iphst:BlockIp',
        link_text='Block IP HST',
        staff_only=True
    )
menu_items=[bl_items]
