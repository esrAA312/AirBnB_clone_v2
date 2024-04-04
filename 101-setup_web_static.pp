# 101-setup_web_static.pp

# Update package lists
exec { 'apt-get-update':
	command => 'apt-get update',
		path    => '/usr/bin',
}

# Upgrade installed packages
exec { 'apt-get-upgrade':
	command => 'apt-get upgrade -y',
		path    => '/usr/bin',
		require => Exec['apt-get-update'],
}

# Install Nginx
package { 'nginx':
	ensure  => installed,
		require => Exec['apt-get-upgrade'],
}

# Create directories
file { '/data/web_static/releases/test/':
	ensure => directory,
	       owner  => 'ubuntu',
	       group  => 'ubuntu',
	       mode   => '0755',
}

file { '/data/web_static/shared/':
	ensure => directory,
	       owner  => 'ubuntu',
	       group  => 'ubuntu',
	       mode   => '0755',
}

# Create index.html
file { '/data/web_static/releases/test/index.html':
	ensure  => file,
		content => '<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n</html>\n',
		owner   => 'ubuntu',
		group   => 'ubuntu',
		mode    => '0644',
}

# Create symbolic link
file { '/data/web_static/current':
	ensure  => link,
		target  => '/data/web_static/releases/test',
		owner   => 'ubuntu',
		group   => 'ubuntu',
}

# Configure Nginx
file { '/etc/nginx/sites-enabled/default':
	ensure  => file,
		content => "server {\n\tlisten 80 default_server;\n\tserver_name _;\n\tlocation / {\n\t\tproxy_pass http://localhost:5000;\n\t\tproxy_set_header Host \$host;\n\t\tproxy_set_header X-Real-IP \$remote_addr;\n\t\tproxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;\n\t\tproxy_set_header X-Forwarded-Proto \$scheme;\n\t}\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n}\n",
		owner   => 'root',
		group   => 'root',
		mode    => '0644',
		require => Package['nginx'],
		notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
	ensure  => running,
		enable  => true,
		require => File['/etc/nginx/sites-enabled/default'],
}
