#!/usr/bin/env bash
# sets up ssh config file so that connection can be made without a password
file { '/etc/ssh/ssh_config':
ensure => present,
}
file_line { 'Turn off passwrd auth':
path  => '/etc/ssh/ssh_config',
line  => 'PasswordAuthentication no',
match => '^#PasswordAuthentication',
}
file_line { 'Declare identity file': 
path  => '/etc/ssh/ssh_config',
line  => 'IdentityFile ~/.ssh/school',
match => '^#IdentityFile',
} 
