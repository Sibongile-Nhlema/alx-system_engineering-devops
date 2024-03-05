# 2-puppet_custom_http_response_header.pp

# Update package repositories
package { 'nginx':
  ensure => 'latest',
}

# Create index.html with "Hello World!"
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Define Nginx configuration with hostname
$nginx_config = @(EOL)
server {
    listen 80 default_server;
    server_name _;
    rewrite ^/redirect_me https://youtube.com/watch?v=3j66gHbyFF8 permanent;
}

server {
    listen 80 default_server;
    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
        internal;
    }

    # Add custom HTTP header with server hostname
    add_header X-Served-By $hostname;
}
EOL

file { '/etc/nginx/sites-available/default':
  content => $nginx_config,
  notify  => Exec['validate_nginx'],
}

# Enable the site by creating a symbolic link
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/default',
  notify  => Exec['validate_nginx'],
}

# Create 404.html with custom message
file { '/var/www/html/404.html':
  content => "C'est n'est pas une page",
}

# Validate Nginx configuration
exec { 'validate_nginx':
  command     => 'nginx -t',
  refreshonly => true,
}

# Restart Nginx if configuration is valid
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  subscribe  => Exec['validate_nginx'],
}

