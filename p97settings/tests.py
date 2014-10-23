"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import StringIO
from django.test import TestCase
from p97settings.ini_parser import IniParser

class TestIniParser(TestCase):
    def setUp(self):
        somelist = ['a', 'b', 'c', 1, 2, 3]
        somelist_txt = ', '.join(str(s) for s in somelist)
        
        self.ini_params = dict(
            SOMEBOOL=True,
            SOMEINT=3,
            SOMELIST=somelist_txt,
            SOMEPATH='/path/to/somewhere',
            SOMETHING='Another setting'
        )
        ini = """[APP]
SOMEBOOL = {SOMEBOOL}
SOMEINT = {SOMEINT}
SOMELIST = {SOMELIST}
SOMETHING = {SOMETHING}
SOMEPATH = {SOMEPATH}
        """
        ini = ini.format(**self.ini_params)
        io = StringIO.StringIO()
        io.write(ini)
        io.seek(0)
        self.ini = IniParser()
        self.ini.readfp(io)
    
    def test_non_existent(self):
        result = self.ini.get('APP', 'non-existent')
        self.assertIsNone(result)
        result = self.ini.get('no-section', 'non-existent')
        self.assertIsNone(result)

    def test_get(self):
        result = self.ini.get('APP', 'SOMEPATH')
        self.assertEqual(result, self.ini_params['SOMEPATH'])
    
    def test_getdefault(self):
        result = self.ini.get('nope', 'nothing', 'Poodle')
        self.assertEqual(result, 'Poodle')
    
    def test_getlist(self):
        result = self.ini.get('APP', 'SOMELIST')
        self.assertEqual(len(result), len(self.ini_params['SOMELIST']))
        for thing in result: 
            self.assertTrue(type(thing) is str)
    
    def test_getboolean(self):
        result = self.ini.getboolean('APP', 'SOMEBOOL')
        self.assertTrue(type(result) is bool)
    
    def test_getboolean_default(self):
        result = self.ini.getboolean('nope', 'nothing', True)
        self.assertTrue(type(result) is bool)
    
    def test_getint(self):
        result = self.ini.getint('APP', 'SOMEINT')
        self.assertTrue(type(result) is int)
        self.assertEqual(result, self.ini_params['SOMEINT'])

    def test_getint_default(self):
        result = self.ini.get('no-section', 'non-existent', 5)
        self.assertEqual(result, 5)

