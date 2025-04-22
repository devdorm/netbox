from netbox.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link='',  # External or internal link
        link_text='My Link',         # Label in the menu
        buttons=[],                  # No buttons needed
        permissions=[],              # Leave blank for public access
    ),
)
