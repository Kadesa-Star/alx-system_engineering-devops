# This manifest corrects the permissions of the WordPress directory
file { '/var/www/html/wordpress':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

service { 'apache2':
  ensure => running,
}
