from netbox.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link='https://example.com',  # External or internal link
        link_text='My Link',         # Label in the menu
        buttons=[],                  # No buttons needed
        permissions=[],              # Leave blank for public access
        icon_class='mdi mdi-link',   # Material Design Icon (optional)
    ),
)
