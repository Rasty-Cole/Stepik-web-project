sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
cd /home/box/web/ask
gunicorn -b 0.0.0.0:8000 ask.wsgi
