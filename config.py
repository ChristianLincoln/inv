# Quick little module for reading config.ini which holds some data to get this submission up and running on a machine
import configparser 
config = configparser.ConfigParser()		
config.read("config.ini")