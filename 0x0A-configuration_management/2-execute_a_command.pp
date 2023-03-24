#Kill a process
exec { 'kill' :
  command => '/usr/bin/pkill killmenow',
  user    => 'root'
}
