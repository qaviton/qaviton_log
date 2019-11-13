# Qaviton Log
![logo](https://www.qaviton.com/wp-content/uploads/logo-svg.svg)  
[![version](https://img.shields.io/pypi/v/qaviton_log.svg)](https://pypi.python.org/pypi)
[![license](https://img.shields.io/pypi/l/qaviton_log.svg)](https://pypi.python.org/pypi)
[![open issues](https://img.shields.io/github/issues/qaviton/qaviton_log)](https://github/issues-raw/qaviton/qaviton_log)
[![downloads](https://img.shields.io/pypi/dm/qaviton_log.svg)](https://pypi.python.org/pypi)
![code size](https://img.shields.io/github/languages/code-size/qaviton/qaviton_log)
-------------------------  
  
Qaviton Log  
Its a simple wrapper to the logging module.  
With easy API of logging to a file or to the console.     
  
## Usage  
```python
from qaviton_log import Logger

log = Logger(file='log')
log.info('hi')
log.warning('bye')
```  