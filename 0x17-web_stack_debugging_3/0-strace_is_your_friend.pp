# Puppet manifest to fix `phpp` extensions to `php` in the WordPress file `wp-settings.php`

$wordpress_file = '/var/www/html/wp-settings.php'

# Use `sed` command to replace `.phpp` with `.php` in the WordPress file
exec { 'fix-wordpress-phpp':
  command     => "sed -i 's/\\.phpp$/.php/' ${wordpress_file}",
  path        => '/bin:/usr/bin',
  onlyif      => "grep -q '\\.phpp$' ${wordpress_file}",
}
