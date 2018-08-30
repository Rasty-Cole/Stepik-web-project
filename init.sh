sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE dbqa"
mysql -uroot -e "'dandi'@'localhost' IDENTIFIED BY 'dandi'"
cd /home/box/web/ask
gunicorn -b 0.0.0.0:8000 ask.wsgi
