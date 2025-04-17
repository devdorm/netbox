### Plugin metadata

# Raw plugin name; should match the source directory name, e.g. "netbox_example_plugin"
__plugin_name__ = "netbox_test_plugin"

# Human-friendly plugin name, e.g. "NetBox Example Plugin"
__plugin_verbose_name__ = "NetBox Test Plugin"

# Semantic version of the plugin, e.g. "1.0.0"
__plugin_version__ = "0.1.0"

# Short description of what the plugin does
__plugin_description__ = "NetBox plugin for testing."

# Plugin author's name or organization, e.g. "Your Name" or "Company Inc."
__plugin_author__ = "DevDorm.cc"

# Contact email address for the plugin author
__plugin_author_email__ = "noreply@devdorm.cc"

# URL base path for the plugin; defaults to plugin name if not specified
__plugin_base_url__ = "netbox_test_plugin"

# List of required user-defined configuration settings, e.g. ["MY_SETTING"]
__plugin_required_settings__ = []

# Dictionary of default configuration values, e.g. {"MY_SETTING": "default_value"}
__plugin_default_settings__ = {}

# List of additional Django apps to load, e.g. ["myplugin.django_app"]
__plugin_django_apps__ = []

# Minimum supported NetBox version, e.g. "3.6.0"
__plugin_min_version__ = ""

# Maximum supported NetBox version, e.g. "3.7.99"
__plugin_max_version__ = ""

# List of additional middleware classes to load, e.g. ["myplugin.middleware.CustomMiddleware"]
__plugin_middleware__ = []

# List of background task queues to create, e.g. ["software_updates"]
__plugin_queues__ = []

# List of event handlers to add to the EVENTS_PIPELINE, e.g. ["myplugin.handlers.handle_software_event"]
__plugin_events_pipeline__ = []

# Dotted path to search index classes, e.g. "myplugin.search_indexes"
__plugin_search_extensions__ = "search.indexes"

# Dotted path to data backend classes, e.g. "myplugin.backends"
__plugin_data_backends__ = "data_backends.backends"

# Dotted path to template extension classes, e.g. "myplugin.template_extensions"
__plugin_template_extensions__ = "template_content.template_extensions"

# Dotted path to menu items for the UI navigation, e.g. "myplugin.navigation.menu_items"
__plugin_menu_items__ = "navigation.menu_items"

# Dotted path to the GraphQL schema (if any), e.g. "myplugin.graphql.schema"
__plugin_graphql_schema__ = "graphql.schema"

# Dotted path to the user preferences dictionary, e.g. "myplugin.preferences"
__plugin_user_preferences__ = "preferences.preferences"

from netbox.plugins import PluginConfig


class testConfig(PluginConfig):
    """Plugin configuration for NetBox Softwares Plugin."""
    name = __plugin_name__
    verbose_name = __plugin_verbose_name__
    version = __plugin_version__
    description = __plugin_description__
    author = __plugin_author__
    author_email = __plugin_author_email__
    base_url = __plugin_base_url__

    # Optional settings
    #required_settings = __plugin_required_settings__
    #default_settings = __plugin_default_settings__
    #django_apps = __plugin_django_apps__
    #middleware = __plugin_middleware__
    #queues = __plugin_queues__
    #events_pipeline = __plugin_events_pipeline__
    #search_extensions = __plugin_search_extensions__
    #data_backends = __plugin_data_backends__
    #template_extensions = __plugin_template_extensions__
    #menu_items = __plugin_menu_items__
    #graphql_schema = __plugin_graphql_schema__
    #user_preferences = __plugin_user_preferences__

    # Optional version constraints (can be filled in if needed)
    #min_version = __plugin_min_version__
    #max_version = __plugin_max_version__

config = testConfig
