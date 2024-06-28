# This manifest ensures that any process named killmenow is terminated

exec { 'kill_killmenow':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep killmenow',
}
