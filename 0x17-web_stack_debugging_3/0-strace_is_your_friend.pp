# replace `phpp` file extensions with `php` in the WordPress file `wp-settings.php`

exec { 'fix-wordpress-phpp':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}
