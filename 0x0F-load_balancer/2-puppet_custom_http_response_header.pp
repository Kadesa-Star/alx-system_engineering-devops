# 2-puppet_custom_http_response_header.pp
# This Puppet manifest configures Nginx to include a custom HTTP header 'X-Served-By' with the hostname of the server

node default {
  
  # Ensure the package 'nginx' is installed
  package { 'nginx':
    ensure => installed,
  }

  # Ensure the Nginx service is running and enabled at boot
  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }

  # Manage the Nginx configuration file to include the custom HTTP header
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }
}

# Create the template file 'default.erb'
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
  ensure  => file,
  content => @(EOF)
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;
    root /var/www/html;

    # Add custom HTTP header
    add_header X-Served-By <%= @hostname %>;

    index index.html index.htm index.nginx-debian.html;
    location / {
        try_files $uri $uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=xJJsoquu70o;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}
  | EOF
  require => File['/etc/nginx/sites-available/default'],
}
