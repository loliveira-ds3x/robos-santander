from logging.config import dictConfig
import logging
import ast

def Logging_method ():
    file = open('/home/ds3x/robos-santander/Logs/LOGGING_CONFIG','r')
    contents = file.read()
    #dictionary = ast.literal_eval(contents)
    dictConfig(contents)