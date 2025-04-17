"""Top-level package for NetBox test Plugin."""

__author__ = """johhniv"""
__email__ = "johhni.games@gmail.com"
__version__ = "0.1.0"


from netbox.plugins import PluginConfig


class testConfig(PluginConfig):
    name = "netbox_test_plugin"
    verbose_name = "NetBox test Plugin"
    description = "NetBox plugin for test."
    version = "version"
    base_url = "netbox_test_plugin"


config = testConfig

from .template_content import template_extensions
