#!/usr/bin/env ruby
log = ARGV[0]
sender = log[/from:([^\]]+)/i,1]
receiver = log[/to:([^\]]+)/i,1]
flag = log[/flags:([^\]]+)/i,1]
puts "#{sender},#{receiver},#{flag}"
