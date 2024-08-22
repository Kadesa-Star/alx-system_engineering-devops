# This Puppet manifest increases the max open files limit for Nginx and restarts the service.

# Increase the max open files limit for Nginx
exec { 'modify-max-open-files-limit':
  command => 'sed -i "s/15/10000/" /etc/default/nginx',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  notify  => Service['nginx'],  # Restart Nginx if this command modifies the file
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  subscribe => Exec['modify-max-open-files-limit'],  # Restart if the file is modified
}
