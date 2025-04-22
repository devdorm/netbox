from netbox.plugins import PluginMenuItem, PluginMenu

'''menu_items = (
    PluginMenuItem(
        link='plugins:netbox_softwares_plugin:softwares_list',  # 
        link_text='My Link',         # Label in the menu
        buttons=(),                  # No buttons needed
        permissions=[],              # Leave blank for public access
    ),
)'''

item1 = PluginMenuItem(
        link='plugins:netbox_softwares_plugin:softwares_list',  # 
        link_text='My Link',         # Label in the menu
        buttons=(),                  # No buttons needed
        permissions=[],              # Leave blank for public access
    )
item2 = PluginMenuItem(
        link='plugins:netbox_softwares_plugin:softwares_list',  # 
        link_text='My Link',         # Label in the menu
        buttons=(),                  # No buttons needed
        permissions=[],              # Leave blank for public access
    )

menu = PluginMenu(
    label='Softwares',
    groups=(
        ('My Link',(item1, item2)),
    ),
    icon_class='mdi mdi-apps-box'
)