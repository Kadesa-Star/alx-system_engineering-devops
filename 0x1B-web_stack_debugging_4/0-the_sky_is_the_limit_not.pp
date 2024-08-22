# This Puppet manifest adjusts the max open files limit for Nginx and restarts the service.

# Increase the max open files limit for Nginx
file_line { 'increase-max-open-files-limit':
  path  => '/etc/default/nginx',
  line  => 'ulimit -n 10000',
  match => '^ulimit',
  notify => Service['nginx'],  # Ensure Nginx is restarted if this line is modified
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  subscribe => File_line['increase-max-open-files-limit'],  # Restart Nginx if the file line changes
}
