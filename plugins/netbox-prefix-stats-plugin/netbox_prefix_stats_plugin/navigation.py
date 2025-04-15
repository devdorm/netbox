from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

plugin_buttons = [
    PluginMenuButton(
        link="plugins:netbox_prefix_stats_plugin:prefixstats_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_prefix_stats_plugin:prefixstats_list",
        link_text="prefix stats",
        buttons=plugin_buttons,
    ),
)
