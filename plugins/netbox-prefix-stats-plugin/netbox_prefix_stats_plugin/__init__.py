"""Top-level package for NetBox prefix stats Plugin."""

__author__ = """johhniv"""
__email__ = "johhni.games@gmail.com"
__version__ = "0.1.0"


from netbox.plugins import PluginConfig


class prefixstatsConfig(PluginConfig):
    name = "netbox_prefix_stats_plugin"
    verbose_name = "NetBox prefix stats Plugin"
    description = "NetBox plugin for prefix stats."
    version = "version"
    base_url = "netbox_prefix_stats_plugin"


config = prefixstatsConfig
