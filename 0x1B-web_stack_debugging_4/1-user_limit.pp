# Increase the file limit for the user: Holberton 

# increase the hard limit to 50000
exec { 'update_hard_limit':
  command => '/bin/sed -i "/^holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin',
}

# increase the soft limit to 5000
exec { 'update_soft_limit':
  command => '/bin/sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin',
}
