from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

bl_items = PluginMenuItem(
        link='plugins:block_iphst:BlockIp',
        link_text='Block IP HST',
        staff_only=True
    )
menu_items=[bl_items]
