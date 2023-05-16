# Change limits

exec { 'Change hard limit':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 5000/" /etc/security/limits.conf',
  onlyif  => 'test -e /etc/security/limits.conf',
  path    => ['/usr/bin', '/bin',],
  returns => [0, 1]
}

exec { 'Change soft limit':
  command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 400/" /etc/security/limits.conf',
  onlyif  => 'test -e /etc/security/limits.conf',
  path    => ['/usr/bin', '/bin',],
  returns => [0, 1],
}
