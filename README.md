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
* SSH into the virtual machine with your private key and username: ubuntu
* Edit the host file 'sudo nano /etc/host' and add the line '127.0.0.1 pathofexileitemtracker'
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
