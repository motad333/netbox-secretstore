from extras.plugins import PluginConfig
from django.utils.translation import gettext_lazy as _

class NetBoxSecretStore(PluginConfig):
    name = 'netbox_secretstore'
    verbose_name = _('Netbox Secret Store')
    description = _('A Secret Storage for NetBox')
    version = '1.0.8'
    author = 'NetBox Maintainers'
    author_email = ''
    base_url = 'netbox_secretstore'
    min_version = '3.0.0'
    required_settings = []
    caching_config = {
        '*': {
            'ops': 'all'
        }
    }
    default_settings = {
        'public_key_size': 2048
    }


config = NetBoxSecretStore
