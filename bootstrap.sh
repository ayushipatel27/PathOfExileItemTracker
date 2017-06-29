#!/usr/bin/env bash

# adapted and extended from        https://www.dev-metal.com/super-simple-vagrant-lamp-stack-bootstrap-installable-one-command/

# Use single quotes instead of double quotes to make it work with special-character passwords
PASSWORD='pwd12345'
PROJECTFOLDER='htdocs'

# create project folder
sudo mkdir  "/var/www/html/${PROJECTFOLDER}"

export DEBIAN_FRONTEND=noninteractive

# update / upgrade 
sudo apt-get update
sudo apt-get -y upgrade

# install python in case wasn't installed on the box
sudo apt-get -y install python3 ipython3 curl

# To have python runs with python3
sudo ln -s /usr/bin/python3 /usr/bin/python

# installing Pip, the recommended package installer for Python:
sudo apt-get -y install python3-pip
sudo -H pip3 install --upgrade pip

# install apache2 web server
sudo apt-get install -y apache2

# install Flask
sudo apt-get -y install python3-flask 

# install and enable mod_wsgi for running Python 3 with Apache
sudo apt-get -y install libapache2-mod-wsgi-py3

# install database server, mysql, and give an initial password to installer. 
# Best is to change password afterward so that the new password will not be viewable 
# in a text file like this one.
sudo debconf-set-selections <<< "mysql-server mysql-server/root_password password $PASSWORD"
sudo debconf-set-selections <<< "mysql-server mysql-server/root_password_again password $PASSWORD"
sudo apt-get -y install mysql-server

# set up basice security practices:
# sudo mysql_secure_installation <<EOF
# 
# $PASSWORD
# n
# y
# y
# y
# y
# EOF

# install a simple way to connect Python with MySQL
sudo pip3 install pymysql
sudo apt-get -qqy install python3-sqlalchemy
sudo pip3 install flask-sqlalchemy

# setup hosts file
# VHOST=$(cat <<EOF
# <VirtualHost *:80>
#     DocumentRoot "/var/www/html/${PROJECTFOLDER}"
#     <Directory "/var/www/html/${PROJECTFOLDER}">
#         AllowOverride All
#         Require all granted
#     </Directory>
# </VirtualHost>
# EOF
# )
# echo "${VHOST}" > /etc/apache2/sites-available/000-default.conf

# setup hosts file
VHOST=$(cat <<EOF
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
EOF
)
echo "${VHOST}" > /etc/apache2/sites-available/pathofexileitemtracker.conf

# enable mod_rewrite
sudo a2enmod rewrite

#ensure apache2 ENV vars are set for the session
source /etc/apache2/envvars

# restart apache
sudo service apache2 restart

#ensure apache2 ENV vars are set for the session
#source /etc/apache2/envvars

# install git 
sudo apt-get -y install git

# enable mod_wsgi
sudo a2enmod wsgi
