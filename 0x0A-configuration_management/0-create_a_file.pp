# Using Puppet, create a file in /tmp.
File { '/tmp/school':
mode    => '0744',
owner   => www-data,
group   => www-data,
content => 'I love Puppet'
}