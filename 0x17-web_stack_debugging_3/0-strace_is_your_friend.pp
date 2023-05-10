# Debug wordpress
exec { 'debug wordpress config':
  environment => ['FILE=/var/www/html/wp-settings.php',
                  'ERR=phpp',
                  'CORRECT=php'],
  command     => 'sudo sed -i "s/$ERR/$CORRECT/" $FILE',
  path        => ['/usr/bin', '/bin'],
  returns     => [0, 1]
}
