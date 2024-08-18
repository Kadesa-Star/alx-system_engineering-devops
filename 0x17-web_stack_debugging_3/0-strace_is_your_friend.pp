# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.
exec { 'fix-wordpress':
  command     => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path        => '/usr/local/bin/:/bin/',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'],
  notify      => Service['apache2'],
}

# Ensure Apache service is running
service { 'apache2':
  ensure     => running,
  enable     => true,
  require    => Exec['fix-wordpress'],
}
