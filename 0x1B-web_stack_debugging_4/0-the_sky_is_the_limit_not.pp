# This Puppet manifest adjusts the max open files limit for Nginx and restarts the service.

# Increase the max open files limit and restart Nginx
exec { 'modify-max-open-files-limit':
  command => 'sed -i "s/15/10000/" /etc/default/nginx',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  notify  => Service['nginx'],  # Ensure Nginx is restarted if this command changes the configuration
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  subscribe => Exec['modify-max-open-files-limit'],  # Restart Nginx if the configuration is changed
}
