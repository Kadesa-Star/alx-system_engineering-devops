#!/usr/bin/env ruby
# Method to extract sender, receiver, and flags from log entry
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
