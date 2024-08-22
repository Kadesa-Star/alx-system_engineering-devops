# This Puppet manifest increases the hard and soft file limits for the holberton user
# to prevent "Too many open files" errors.

# Increase hard file limit for Holberton user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton hard nofile/s/^[0-9]*$/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin',
  unless  => 'grep -q "^holberton hard nofile 50000" /etc/security/limits.conf',
}

# Increase soft file limit for Holberton user
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton soft nofile/s/^[0-9]*$/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin',
  unless  => 'grep -q "^holberton soft nofile 50000" /etc/security/limits.conf',
}
