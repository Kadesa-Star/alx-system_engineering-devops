# 2-puppet_custom_http_response_header.pp
# This Puppet manifest automates configuration of Nginx to include a custom HTTP header 'X-Served-By' with the server's hostname

# Update package list
exec { 'update':
  command => '/usr/bin/apt-get update',
  path    => ['/usr/bin', '/usr/sbin'],
}

# Ensure nginx package is present
package { 'nginx':
  ensure => present,
  require => Exec['update'],
}

# Add custom HTTP header to nginx configuration
file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => '^http {',
  line  => "http {\n    add_header X-Served-By \"${hostname}\";",
  require => Package['nginx'],
}

# Restart nginx service to apply changes
exec { 'run':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => File_line['http_header'],
  path        => ['/usr/bin', '/usr/sbin'],
}
