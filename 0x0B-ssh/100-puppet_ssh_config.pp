# Puppet script to configure SSH client settings for passwordless authentication

# Ensure that PasswordAuthentication is set to 'no' in the SSH client configuration
file_line { 'Turn off passwd auth':
  ensure => 'present',                  # Ensure the line exists in the file
  path   => '/etc/ssh/ssh_config',      # Path to the SSH client configuration file
  line   => 'PasswordAuthentication no', # Line to add or modify in the file
}

# Ensure that IdentityFile is set to '~/.ssh/holberton' in the SSH client configuration
file_line { 'Declare identity file':
  ensure => 'present',                  # Ensure the line exists in the file
  path   => '/etc/ssh/ssh_config',      # Path to the SSH client configuration file
  line   => 'IdentityFile ~/.ssh/holberton', # Line to add or modify in the file
}
