# Fixing the failing requests issue on our web server - Ulimit config

# update the ulimit values to accomodate the requests (soft - 1024, hard - 4096)
exec { 'fix--ulimit--to--hard--limit':
  command => '/bin/sed -i "s/15/4096/g" /etc/default/nginx',
  path    => '/usr/local/bin:/bin/',
}

#restart nginx
exec { 'restart-nginx':
  command => '/etc/init.d/nginx restart',
  path    => 'etc/init.d/',
}
