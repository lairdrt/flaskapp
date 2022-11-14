# Valve Controller Flask Template

The Valve Controller Flask Template contains the framework for quickly building a full-stack application using your choice of
database (PostgreSQL, MySQL, SQLite3) along with secure login and Bootstrap (5) HTML components.

## New Raspberry Pi Configuration

$sudo apt-get -y update
$sudo apt-get -y upgrade

## SSH Configuration

$sudo raspi-config
- Select Interface Options
- Select SSH
- Select Yes

$cd ~
$mkdir .ssh
$cd .ssh
$nano authorized_keys
ssh-rsa AAAAB3NzaC...

## Installing Python

$sudo apt-get -y install python3 python3-venv python3-dev
$sudo apt-get -y install supervisor nginx git
$sudo pip install --upgrade pip

&copy; 2020-2023 Same Day Rules