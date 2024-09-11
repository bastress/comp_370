
### Steps required to setup a functioning database that is accessible from the public internet:

Install MariaDB package:
> sudo apt install mariadb-server

Run the following to configure MariaDB security settings (choose to remove anonymous users, disable remote root logins, and remove the test database.):
> sudo mysql_secure_installation

In the file "/etc/mysql/mariadb.conf.d/50-server.cnf" change bind-address to 0.0.0.0, and add the line "port = 6002" below the section [mysqld]. This configures MariaDB to listen on port 6002.

Restart MariaDB to apply changes by running:
> sudo systemctl restart mariadb

Under Networking on Lightsail instance, open port 6002 setting it to Custom application with TCP protocol. 

Log in to MariaDB with:
> sudo mysql -u root

From inside MariaDB Monitor, create new database with:
> CREATE DATABASE comp370_test;

Create the user "comp370" with password "$ungl@ss3s" by running:
> CREATE USER 'comp370'@'%' IDENTIFIED BY '$ungl@ss3s';

Open full access to database with:
> GRANT ALL PRIVILEGES ON comp370_test.* TO 'comp370'@'%';<br>
> FLUSH PRIVILEGES;

Exit monitor with:
> exit;

Test public access through DBeaver with the following settings:
- Host: Your Lightsail instance’s public IP (X.Y.Z.W).
- Port: 6002
- Database: comp370_test
- Username: comp370
- Password: $ungl@ss3s
