
#Traditional file reading and writing:
hash1=Hash.new(Array.new)
infile = File.open('/usr/home/pa/Text2.txt', "r")


while line = infile.gets  do
puts "line=#{line}"
	hash1["name"].push line.split("|")[0]
	hash1["number"].push line.split("|")[1]
end
infile.close


puts hash1["number"]








