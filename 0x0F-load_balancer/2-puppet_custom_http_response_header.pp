# Puppet manifest to configure custom HTTP header in Nginx

# Update package lists
exec { 'update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
}

# Ensure Nginx is installed
package { 'nginx':
  ensure => 'installed',
}

# Configure custom HTTP header in Nginx
file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => 'add_header X-Served-By "${hostname}";',
  match => 'http {',
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File_line['http_header'],
}
