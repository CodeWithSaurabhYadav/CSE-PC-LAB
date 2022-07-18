# This is only required for deb based operating system.
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get update
sudo apt-get install mysql-client-core-5.7 -y
sudo apt-get install mariadb-client-core-10.1 -y
sudo apt-get install mysql-server -y
sudo systemctl start mysql.service
