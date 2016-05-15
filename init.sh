sudo rm -r /etc/mysql/my.cnf
sudo ln -sf /home/box/web/etc/my.cnf  /etc/mysql/my.cnf
sudo /etc/init.d/mysql start

mysql -uroot -e "CREATE DATABASE qa"
mysql -uroot -e "CREATE USER 'qauser'@'localhost' IDENTIFIED BY 'qapass';
				 GRANT ALL ON qa.* TO 'qauser'@'localhost';"

sudo python /home/box/web/ask/manage.py syncdb


sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/qa.py /etc/gunicorn.d/qa.py
sudo /etc/init.d/gunicorn restart