file { '/home/ubuntu/.ssh/config':
  ensure  => present,
  mode    => '0600',
  source  => '/root/alx-system_engineering-devops/0x0B-ssh/client_config.erb',
}
