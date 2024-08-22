# This Puppet manifest increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'increase-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin'],
  notify  => Service['nginx'], # Ensure Nginx is restarted if this changes
}

# Restart Nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
  subscribe => Exec['increase-nginx-ulimit'], # Restart if the file is changed
}
