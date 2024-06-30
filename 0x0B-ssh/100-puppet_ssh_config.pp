# Puppet script to configure SSH client settings in /etc/ssh/ssh_config

file_line { 'Turn off passwd auth and declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => [
    '    PasswordAuthentication no',
    '    IdentityFile ~/.ssh/school',
  ],
}
