import sys

# ensure all application code is in the python load path    
sys.path.append('/var/www/html/')

from app import app as application

# Supposedly, when there is code change, use the touch command in Linux to 
# reload code without restarting Apache. e.g.
# touch  app.wsgi

# Reality, put a space at the end of one of the comment lines, re-save this file
# The "WSGIScriptReloading On" in the configuration will reload this .wsgi file
# and will cause the python code refresh with the changes

