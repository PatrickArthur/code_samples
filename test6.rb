filename = '/usr/home/pa/Text2.txt'

prompt = "> "
txt = File.open(filename)

puts "Here's your file: #{filename}"
puts txt.read()

puts txt
print prompt
