# Path of Exile Item Tracker

Path of Exile is an online Action RPG. The game is designed around players slaying monsters and collecting items. People find items playing the game and often trade them in a strong online item economy.

This app makes trading easier, allowing users to concentrate on playing the game while the app watches the trade market for them.
* Items in public stashes are sellable for various amounts
* We're creating a watch list for currency items and tracking their exchange rates and possibly more down the line.
* Users will be able to create profiles to track specific items and have the option to be notified when an item is being traded at a low price.



## Authors

* **Bryan Arretteig** - *Developer* - [GitHub](https://github.com/Arretteig) - [UAB GitLab] (https://gitlab.cis.uab.edu/medzo)
* **Craig Brewton** - *Developer* -  [UAB GitLab] (https://gitlab.cis.uab.edu/craigb96)
* **Tarra Kuhn** - *Developer* - [GitHub](https://github.com/tarrak) - [UAB GitLab] (https://gitlab.cis.uab.edu/tarrak)
* **Ayushi Patel** - *Developer* - [GitHub](https://github.com/ayushipatel27) - [UAB GitLab] (https://gitlab.cis.uab.edu/ayushi27)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
* In the terminal navigate to the project directory run command 'vagrant up'
* On Windows Vagrant will create a private key for you at 'PROJECT_DIRECTORY/.vagrant/machines/default/virtualbox/private_key'. You will need this key to log into the Virtual Box. If you are using Windows Putty then you will probably have PuttyGen installed. In PuttyGen hit the load button and find the private_key file. Once it is loaded save the private key file as a .ppk file in order to authenticate.
* Create a configdb.txt file just like the ones from previous class projects with the database name 'stash'
* SSH into the virtual machine with your private key and username: ubuntu
* Open mysql and run the command 'source /var/www/html/sprocs/setupdb.sql' and then exit mysql
* Navigate to the director /var/www/html/ and start the parser with 'python stashwatch.py'
* If everything was properly set up you should now be able to see the project in your browser at http://localhost:8080
* NOTE: When running stashwatch for the very first time the program will attempt to get the latest path of exile api id from another site. If your connection is refued to this site then you will get an error and stashwatch wont work. The solution to this seems to be either to wait and try again, redeploy your virtual machine, or as a last resort manually run a procedure to insert an older api id to look at in the json_stashes table. To do this open mysql and type 'use stash;' then "CALL update_json_id('77560891-81505961-76408727-88636703-82457809', '77560949-81506007-76408764-88636764-82457860')". 


## Built With

* Linux Ubuntu
* Apache2
* MySQL
* Python Flask Web Framework


## Acknowledgments

* [Grinding Gear Games] (http://www.grindinggear.com/)
* [Path of Exile] (https://www.pathofexile.com/)
