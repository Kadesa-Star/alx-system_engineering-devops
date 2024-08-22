# Change the OS configuration so that it is possible to login with the
# holberton user and open a file without any error message.

exec {'OS security config':
  command => 'sed -i "s/^holberton hard nofile.*/holberton hard nofile 50000/" /etc/security/limits.conf && sed -i "s/^holberton soft nofile.*/holberton soft nofile 50000/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/',
  unless  => 'grep -q "^holberton hard nofile 50000" /etc/security/limits.conf && grep -q "^holberton soft nofile 50000" /etc/security/limits.conf',
}
