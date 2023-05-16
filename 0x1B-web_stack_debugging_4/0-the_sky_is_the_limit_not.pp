# Change limit

exec { 'Change limit':
  command => 'sed -i "s/15/100000/" /etc/default/nginx',
  path    => ['/usr/bin', '/bin',],
  returns => [0,1]
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  restart    => '/usr/sbin/service nginx restart',
  subscribe  => Exec['Change limit'],
}
