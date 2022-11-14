# Valve Controller Flask Template

The Valve Controller Flask Template contains the framework for quickly building a full-stack application using your choice of
database (PostgreSQL, MySQL, SQLite3) along with secure login and Bootstrap (5) HTML components.

## New Raspberry Pi Configuration

`$sudo apt-get -y update`
`$sudo apt-get -y upgrade`

## SSH Configuration

`$sudo raspi-config`
- Select Interface Options
- Select SSH
- Select Yes

`$cd ~`
`$mkdir .ssh`
`$cd .ssh`
`$nano authorized_keys`
- Copy your public key here

## Installing Python

`$sudo apt-get -y install python3 python3-venv python3-dev`
`$sudo apt-get -y install supervisor nginx git`
`$sudo pip install --upgrade pip`

## Install MySQL DB (Maria DB):

`$sudo apt install mariadb-server`
`$sudo mysql_secure_installation`
- Answer "N" to prompts regarding setting/changing root password
- Answer “Y” to all other prompts

## Make Database
`$sudo mysql -u root -p`
`>CREATE DATABASE database_name;`
`>CREATE USER 'database_user_name'@'localhost' IDENTIFIED BY 'database_user_password';`
`>GRANT ALL PRIVILEGES ON database_name.* TO 'database_user_name'@'localhost';`
`>ALTER USER database_user_name@localhost IDENTIFIED BY 'database_user_password'; # as necessary`
`>FLUSH PRIVILEGES;`

## More to do

&copy; 2020-2023 Same Day Rules