import warnings
from ConfigParser import RawConfigParser

class IniParser(RawConfigParser):
    """RawConfigParser modified to have return a default value if something
    doesn't exist rather than throwing a NoSectionError.
    """

    def get(self, section, name, default=None):
        if self.has_option(section, name):
            return RawConfigParser.get(self, section, name)
        else:
            if default is None or self.has_section(section):
                warnings.warn('Configuration missing: %s.%s, defaulting to %s\n' % (section, name, default))
            return default
    
    def getlist(self, section, name):
        result = self.get(section, name)
        if not result:
            return []
        
        # parse a comma-separated string into a list of strings
        result = result.replace(' ', '')
        result = result.split(',')
        return result
        
    def getboolean(self, section, option, default=None):
        result = self.get(section, option, default)
        if type(result) is bool: 
            return result
        elif result.lower() in ('0', 'no', 'false'):
            return False
        elif result.lower() in ('1', 'yes', 'true'):
            return True
        else:
            warnings.warn('Configuration value %s.%s is not a boolean\n' % (section, name))
            return default

    def getint(self, section, option, default=None):
        result = self.get(section, option, default)
        try:
            return int(result)
        except ValueError:
            warnings.warn('Configuration value %s.%s is not an integer\n' % (section, name))
            return default
