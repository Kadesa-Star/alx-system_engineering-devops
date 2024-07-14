# Configure a new Ubuntu server with Nginx using Puppet

# Update the system's package list
exec { 'update_system':
  command => '/usr/bin/apt-get update',
}

# Install the Nginx package
package { 'nginx':
  ensure   => installed,
  require  => Exec['update_system'],
}

# Create an index.html file with "Hello World!" content
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Add a redirection rule to the Nginx configuration for /redirect_me
exec { 'add_redirect':
  command  => 'sed -i "24i\\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
