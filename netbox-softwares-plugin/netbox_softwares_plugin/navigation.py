from extras.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
from utilities.choices import ButtonColorChoices

plugin_buttons = [
    PluginMenuButton(
        link="plugins:netbox_softwares_plugin:softwares_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

# Plugin submenu items

item1 = (
    PluginMenuItem(
        link="plugins:netbox_softwares_plugin:softwares_list",
        link_text="Softwares",
    ),
)

# Plugin submenu

menu = PluginMenu(
    label="Softwares",
    groups=(
        ("Foo", (item1,)),
    ),
    icon_class="mdi mdi-apps-box"
)
