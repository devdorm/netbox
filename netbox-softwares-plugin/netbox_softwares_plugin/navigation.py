from netbox.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_softwares_plugin:softwares_list',  # 
        link_text='My Link',         # Label in the menu
        buttons=[],                  # No buttons needed
        permissions=[],              # Leave blank for public access
    ),
)
