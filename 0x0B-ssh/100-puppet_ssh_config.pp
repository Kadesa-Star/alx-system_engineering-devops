# Puppet script to create ssh config file
include stdlib

file_line { 'Turn off passwd auth and declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => [
    '    PasswordAuthentication no',
    '    IdentityFile ~/.ssh/school',
  ],
}
