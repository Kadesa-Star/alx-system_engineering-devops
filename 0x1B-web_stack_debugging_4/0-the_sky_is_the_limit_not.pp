# This Puppet manifest fixes Nginx to accept and serve more requests by modifying the max open files limit and restarting the Nginx service.

# Increase the max open files limit for Nginx and restart the service
exec { 'modify-max-open-files-limit':
  command => 'sed -i "s/15/10000/" /etc/default/nginx && service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
  unless  => 'grep "10000" /etc/default/nginx',  # Check if the line is already set to 10000
}
