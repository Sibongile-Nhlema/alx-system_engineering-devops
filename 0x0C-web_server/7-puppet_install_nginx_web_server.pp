# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Configure Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Set up Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80;
    server_name _;
    
    location / {
        return 301 /redirect_me;
    }

    location /redirect_me {
        return 301 /;
    }

    location = / {
        return 200 'Hello World!';
    }
}
",
  notify  => Service['nginx'],
}

# Enable the site by creating a symbolic link
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}


