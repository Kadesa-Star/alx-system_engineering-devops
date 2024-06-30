# Puppet script to create SSH config file

# Ensure the ~/.ssh directory exists with correct permissions
file { '/home/ubuntu/.ssh':
  ensure  => 'directory',
  mode    => '0700',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create or update the SSH config file
file { '/home/ubuntu/.ssh/config':
  ensure  => 'file',
  mode    => '0600',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => template('alx-system_engineering-devops/0x0B-ssh/client_config.erb'),
}

# Ensure SSH client configuration settings are applied
file_line { 'Turn off passwd auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}
