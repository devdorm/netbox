"""Top-level package for NetBox prefix stats Plugin."""

__author__ = "DevDorm.cc"
__email__ = "johhni.games@gmail.com"
__version__ = "0.1.0"

from netbox.plugins import PluginConfig

class PrefixStatsConfig(PluginConfig):
    name = "netbox_prefix_stats_plugin"
    verbose_name = "NetBox prefix stats Plugin"
    description = "NetBox plugin for prefix stats."
    version = __version__
    author = __author__
    author_email = __email__
    license = "MIT"
    url = "https://github.com/johhniv/netbox_prefix_stats_plugin"
    base_url = "netbox_prefix_stats_plugin"

config = PrefixStatsConfig
