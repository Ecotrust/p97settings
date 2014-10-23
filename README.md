# p97settings

This module adds ini-based configuration features to django, and provides production deployment configuration. 

## IniParser

The IniParser is a slightly modified version of the RawConfigParser that does not raise exceptions if a section is asked for that's not needed. 

### Example usage in a django settings.py file

settings.py: 

    # bottom
    CONFIG_INI = os.path.normpath(os.path.join(BASE_DIR), 'config.ini')

    config = IniParser()
    config.read(CONFIG_INI)

    # Recommended settings (and required for production)
    SECRET_KEY = config.get('APP', 'SECRET_KEY', default='set secret key')
    DEBUG = config.getboolean('APP', 'DEBUG', True)
    TEMPLATE_DEBUG = config.getboolean('APP', 'TEMPLATE_DEBUG', True)
    ALLOWED_HOSTS = config.getlist('APP', 'ALLOWED_HOSTS')
    STATIC_ROOT = config.get('APP', 'STATIC_ROOT', None')

    # Other settings
    ...


In Development (i.e., locally with DEBUG=True), the settings required for production default to sensible development settings. 

With no config file, warnings are printed for each option that's asked for and not present. 

In production, run `python manage.py generate_secret`, which will auto-generate a config file with a secret, and then the remaining settings (i.e., DEBUG=False) are added manually (once).
