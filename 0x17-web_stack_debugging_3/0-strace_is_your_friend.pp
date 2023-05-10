#Create index.html file
file {'/var/www/html/index.html':
        ensure  => file,
        mode    => '0644',
        content => 'Hello World'
}

# Restart apache
exec {'Apache restart':
        command => 'sudo service apache2 restart',
        path    => ['/usr/bin', '/usr/sbin',],
}
