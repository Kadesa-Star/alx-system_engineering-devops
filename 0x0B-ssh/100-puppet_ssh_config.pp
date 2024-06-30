# Ensure SSH client configuration file exists
file { '/home/ubuntu/.ssh/config':
  ensure  => present,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
  content => "\
# SSH client configuration managed by Puppet

Host *
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
",
}
