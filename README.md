# EMBED SYSTEMS #

This embed systems main website.

## Setup/Configuation procedure: ###
* Install the project requirements using "pip install -r requirements.txt"
* Change "django.core.urlresolvers" to "django.urls" in the "venv/Lib/site-packages/subdomains/utils.py"
* Manually add 
"try:
    from django.utils.deprecation import MiddlewareMixin
except:
    MiddlewareMixin = object" to after "UNSET = object()" in 
    "venv\Lib\site-packages\subdomains\middleware.py"
    
* Manually pass "MiddlewareMixin" as argument to "class SubdomainMiddleware" 
instead of object.
* Manually add your desired domain to your system host file.
* Manually replace the domain you added to your host file with the default
domain "example.com" in the django_site table in your database.
* Manually change "from django.contrib.auth.models import User" to "from core.models import User" in 
"venv/Lib/site-packages/simple_sso/sso_client/client.py"
* Comment out "user.set_unusable_password()" in "venv/Lib/site-packages/simple_sso/sso_client/client.py"
* Comment out "self.register_admin()" in "venv/Lib/site-packages/simple_sso/sso_server/server.py"
* Indent "user.save()" in "venv/Lib/site-packages/simple_sso/sso_client/client.py" by one level.
* Configure your server to use the newly replaced domain. 

### Contributors ###

* Sunday Alexander

### Requirements: ###
This project requirements can be found in the requirements.txt file
which include but not limited to the following:

* asgiref==3.2.3
* Django==3.0.2
* mysqlclient==1.4.6
* pytz==2019.3
* sqlparse==0.3.0