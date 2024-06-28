# This manifest ensures that Flask version 2.1.0 is installed using pip3


package {  'Flask':
   ensure    => '2.1.0',
   provider  => 'pip3',
}


package {  'Werkzeug':
  ensure   => '2.0.3',
  provider => 'pip3'
}
