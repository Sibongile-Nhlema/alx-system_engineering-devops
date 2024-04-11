# Puppet manifest for Apache troubleshooting and configuration

# Install Apache2 package
package { 'apache2':
  ensure => installed,
}

# Ensure Apache service is running and enabled
service { 'apache2':
  ensure => 'running',
  enable => true,
}

# Define a custom function to check Apache service status
exec { 'check_apache_status':
  command => 'service apache2 status',
  logoutput => true,
  notify => Service['apache2'],  # Notify Apache service if status check is performed
}

# Define a custom function to edit the 000-default.conf file
file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => present,
  content => template('my_module/000-default.conf.erb'),
  require => Package['apache2'],  # Ensure Apache package is installed before modifying config
  notify  => Service['apache2'],  # Notify Apache service after config file changes
}

# Ensure the PHP extension is properly configured 
file { '/var/www/html/wp-config.php':
  ensure  => present,
  content => template('my_module/wp-config.php.erb'),
  notify  => Service['apache2'],  # Notify Apache service after config file changes
}

# Restart Apache service if configuration files have changed
exec { 'restart_apache':
  command => 'service apache2 restart',
  refreshonly => true,
  subscribe => File['/etc/apache2/sites-available/000-default.conf', '/var/www/html/wp-config.php'],
}
