
### Steps required to setup a functioning webserver with a file named comp370_hw2.txt being served from the www root:

Run:
> sudo apt update<br>
> sudo apt install apache2

navigate out of ubuntu user directory with:
> cd ../..

Open port 8008 on Lightsail by adding new rule to firewall with Application: Custom, Protocol: TCP, and unrestricted access.

Add the line "Listen 8008" to /etc/apache2/ports.conf

Add the following to /etc/apache2/sites-available/000-default.conf:
> &lt;VirtualHost *:8008><br>
> &nbsp;&nbsp;&nbsp;&nbsp;DocumentRoot /var/www/html <br>
> &nbsp;&nbsp;&nbsp;&nbsp;ErrorLog ${APACHE_LOG_DIR}/error.log<br>
> &nbsp;&nbsp;&nbsp;&nbsp;CustomLog ${APACHE_LOG_DIR}/access.log combined<br>
> &lt;/VirtualHost>


create /var/www/html/comp370_hw2.txt with some text.

run the following to apply new configuration:
> sudo systemctl restart apache2

View site at http://15.222.11.150:8008/comp370_hw2.txt

