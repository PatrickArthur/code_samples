
#Traditional file reading and writing:
hash1=Hash.new
infile = File.open('/usr/home/pa/Text2.txt', "r")


while line = infile.gets  do
puts "line=#{line}"
	hash1["name"].line.split("|")
	hash1["number"].line.split("|")
end
infile.close


puts hash1["number"]