# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
      listen 80;
      server_name localhost;

      error_page 404 /404.html

      location / {
        root   /var/www/html;
        index  index.html;
        echo 'Hello World!';
      }

      location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
      }
    }
  ",
}

#Create 404 file
file { '/var/www/html/404.html' :
  ensure  => file,
  content => "Ceci n'est pas une page"
}

# Create index file
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!"
}
# Enable Nginx site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

