# This manifest ensures that Flask version 2.1.0 is installed using pip3


package {  'puppet-lint':
   ensure    => '2.1.1',
   provider  => 'gem',
}
