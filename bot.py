#!/usr/bin/env python3

from client import Client
from configparser import ConfigParser
import os

Config = ConfigParser()
Config.read(os.path.dirname(os.path.realpath(__file__)) + '/params.ini')

cli = Client(Config.get('Main', 'token'), Config.get('Main', 'prefix'))