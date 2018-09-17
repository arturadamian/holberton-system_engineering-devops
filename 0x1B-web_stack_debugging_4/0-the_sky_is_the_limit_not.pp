# increasing the user's limit
exec {'setting up a config file':
  command => '/bin/sed -i "s/ULIMIT=\"-n 20\"/ULIMIT=\"-n 2000\"/g"\
  /etc/default/nginx && service nginx restart'
}