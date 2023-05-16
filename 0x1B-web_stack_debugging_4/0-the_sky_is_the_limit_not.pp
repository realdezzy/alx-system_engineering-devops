# Change limit

exec { 'Change limit':
  command => 'sed -i "s/15/100000/" /etc/defaults/nginx',
  path    => ['/usr/bin', '/bin',],
  returns => [0,1]
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  restart    => '/usr/sbin/service nginx restart',
  subscribe  => File['/etc/nginx/nginx.conf'],
}
