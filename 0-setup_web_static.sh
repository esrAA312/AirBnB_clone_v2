#!/usr/bin/env bash
# sets up web servers 
sudo apt-get update 
sudo apt-get upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
cat << EOF | tee /data/web_static/releases/test/index.html
<html>
<head>
</head>
<body>
Holberton School
</body>
</html>
EOF

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/
cat << EOF > /etc/nginx/sites-enabled/default
server {
	listen 80 default_server;
	server_name _;
	location / {
		proxy_pass http://localhost:5000;
		proxy_set_header Host \$host;
		proxy_set_header X-Real-IP \$remote_addr;
		proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Proto \$scheme;
	}
	location /hbnb_static {
		alias /data/web_static/current/;
	}
}
EOF
sudo service nginx restart
