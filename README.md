# Path of Exile Item Tracker

One Paragraph of project description goes here


## Authors

* **Bryan Arretteig** - *Developer* - [GitHub](https://github.com/Arretteig) - [UAB GitLab] (https://gitlab.cis.uab.edu/medzo)
* **Craig Brewton** - *Developer* -  [UAB GitLab] (https://gitlab.cis.uab.edu/craigb96)
* **Tarra Kuhn** - *Developer* - [UAB GitLab] (https://gitlab.cis.uab.edu/tarrak)
* **Ayushi Patel** - *Developer* - [GitHub](https://github.com/ayushipatel27) - [UAB GitLab] (https://gitlab.cis.uab.edu/ayushi27)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
* In the terminal navigate to the project directory run command 'vagrant up'
* Vagrant will create a private key for you at 'PROJECT_DIRECTORY/.vagrant/machines/default/virtualbox/private_key'. You will need this key to log into the Virtual Box. If you are using Windows Putty then you will probably have PuttyGen installed. In PuttyGen hit the load button and find the private_key file. Once it is loaded save the private key file as a .ppk file in order to authenticate.
* SSH into the virtual machine with your private key and username: ubuntu
* You will need to set up the configuration for apache2. Navigate to the correct directory 'cd /etc/apache2/sites-available' and then create a new config file 'sudo touch pathofexileitemtracker.conf'. Edit the file with your favorite linux editor, for nano 'sudo nano pathofexileitemtracker.conf', put the following code below inside it:
```
<virtualhost *:80>
    ServerName pathofexileitemtracker
 
    WSGIDaemonProcess pathofexileitemtracker user=www-data group=www-data threads=5 home=/var/www/html/htdocs/
    WSGIScriptAlias / /var/www/html/htdocs/pathofexileitemtracker.wsgi
 
    <directory /var/www/html/htdocs>
        WSGIProcessGroup pathofexileitemtracker
        WSGIApplicationGroup %{GLOBAL}
        WSGIScriptReloading On
        AllowOverride All
        Require all granted
    </directory>
</virtualhost>
```
* Edit the host file 'sudo nano /etc/host' and add the line '127.0.0.1 pathofexileitemtracker'
* Tell Apache which configuration file to use commands 'sudo a2dissite 000-default.conf' to disable the default and then 'sudo a2ensite pathofexileitemtracker.conf' to enable the new configuration.
* To ensure the wsgi is enabled run the command 'sudo a2enmod wsgi' it should've already been enabled during vagrant setup.
* Restart Apache with command 'sudo service apache2 restart'
* If everything was properly set up you should now be able to see the project in your browser at http://localhost:8080 


## Contributing

Please read [CONTRIBUTING.md](https://gitlab.cis.uab.edu/medzo/PathOfExileItemTracker/blob/871952f0790b9604c77bea52bfab848fc3cf9d35/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.


## Built With

* Linux Ubuntu 
* Apache2
* MySQL
* Python Flask Web Framework


## Acknowledgments

* [Grinding Gear Games] (http://www.grindinggear.com/)
* [Path of Exile] (https://www.pathofexile.com/)