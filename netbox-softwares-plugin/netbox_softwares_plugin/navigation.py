from netbox.plugins import PluginMenuItem, PluginMenu

'''menu_items = (
    PluginMenuItem(
        link='plugins:netbox_softwares_plugin:softwares_list',  # 
        link_text='My Link',         # Label in the menu
        buttons=(),                  # No buttons needed
        permissions=[],              # Leave blank for public access
    ),
)'''

list = PluginMenuItem(
        link='plugins:netbox_softwares_plugin:softwares_list',
        link_text='Softwares',
        buttons=(),
        permissions=[],
    )

menu = PluginMenu(
    label='Softwares',
    groups=(
        ('Installed Softwares',(list,)),
    ),
    icon_class='mdi mdi-developer-board'
)