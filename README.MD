# Valve Controller Flask Template
The Valve Controller Flask Template contains the framework for quickly building a full-stack application using your choice of
database (PostgreSQL, MySQL, SQLite3) along with secure login and Bootstrap (5) HTML components.
## New Raspberry Pi Configuration
`$sudo apt-get -y update`

`$sudo apt-get -y upgrade`

## SSH Configuration for New Installation
https://garywoodfine.com/setting-up-ssh-keys-for-github-access/

### Enable SSH on Raspberry Pi
`$sudo raspi-config`
1. Select 'Interface Options'
2. Select 'SSH'
3. Select 'Yes'
4. Select 'Ok'
5. Select 'Finish'

### Generate SSH Public/Private Key
`$cd ~`

`$mkdir .ssh`

`$chmod 0700 ~/.ssh`

`$cd ~/.ssh`

`$ssh-keygen -t rsa`

1. Hit enter to accept default settings for all prompts

`$mv id_rsa.pub authorized_keys`

`$ssh -T git@github.com`
1. Answer 'yes' to question about wanting to connect
2. This should add GitHub to ~/.ssh/known_hosts file
### Add SSH Key to PuTTY Configuration
Install PuTTY from https://www.putty.org/

Follow the instructions at the link below to add your **private key** generated above (id_rsa) to use in your PuTTY session.

https://docs.oracle.com/en/cloud/paas/goldengate-cloud/tutorial-change-private-key-format/
1. Launch the PuTYTGen program
2. Under 'Parameters', select 'RSA' and use 2048 for bits in generated key
3. Load your existing private key that you generated above (and saved locally)
4. After you've loaded your existing private key, save the new key as a .ppk file that can be loaded by PuTTY
5. Exit PuttyGen
6. Launch PuTTY
7. Configure settings for a new session
8. Under Connection -> SSH -> Auth, find and open the .ppk file you just saved
9. You should now be able to connect to your Raspberry Pi using SSH

### Add SSH Key to GitHib Account
Follow the instructions at the link below to add your **public key** to GitHub so that you can manage your Raspberry Pi software.

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
1. Log into your [GitHub](https://github.com) account
2. Select dropdown for your account
3. Select 'Settings'
4. Select 'SSH and GPG keys'
5. Select 'New SSH key'
6. Fill in the fields regarding the key (use id_rsa.pub key from previous step)
7. Select 'Add SSH key'

## Installing Python
`$sudo apt-get -y install python3 python3-venv python3-dev`

`$sudo apt-get -y install supervisor nginx git`

`$sudo pip install --upgrade pip`

## Install MySQL DB (Maria DB)
`$sudo apt install mariadb-server`

`$sudo mysql_secure_installation`
1. Answer 'N' to prompts regarding setting/changing root password
2. Answer 'Y' to all other prompts

## Make Database
`$sudo mysql -u root -p`

`>CREATE DATABASE database_name;`

`>CREATE USER 'database_user_name'@'localhost' IDENTIFIED BY 'database_user_password';`

`>GRANT ALL PRIVILEGES ON database_name.* TO 'database_user_name'@'localhost';`

`>ALTER USER database_user_name@localhost IDENTIFIED BY 'database_user_password'; # as necessary`

`>FLUSH PRIVILEGES;`

&copy; 2020-2023 Same Day Rules
