############################################################################################
#Program: maniptxt.rb                                                                      #
#Author: Patrick Jason Arthur                                                              #
#Date Last Modified: 5/6/13                                                                #
#Purpose: This program takes an input file containing names and numbers, it checks each    #
#entry, for entries with the first name Bob it then checks the phone number to verify that #
#it is in the fomrat (xxx)yyy-zzzz, if it is it writes a message to that output file that  #
#the user has a valid number if it is not a message stating the user has an invalid number #
#will be written. All entries not starting with the name Bob will not be put in the output #
#file                                                                                      #
############################################################################################
class UserObject
	def readdata(inf)
		infile = File.open(inf, "r")
		hash=Hash.new {|h,k| h[k] = Array.new }
		
		#Fill your hash of arrays with data from the file
		while line = infile.gets  do
			hash["name"].push line.split("|") [0]
			hash["number"].push line.split("|") [1]
		end
		infile.close
		return hash
	end
	
	def writedata(outf,hsh)
		outfile = File.open(outf,"w")
		
		#Run through the array and run our checks and write to appropriate files
		for index in (0...hsh["name"].length)
			if ( hsh["name"][index] =~ /[B|b]ob (.*)/ )
				if ( hsh["number"][index] =~ /^\([1-9]{1}[0-9]{2}\)[0-9]{1}[1-9]{2}\-[0-9]{4}/ )
					outfile.write("#{hsh["name"][index]} has a valid number\n")
				else
					outfile.write("#{hsh["name"][index]} does not have a valid number\n")
				end
			end
		end
		outfile.close
	end
end

user=UserObject.new
h=user.readdata("/usr/home/pa/Text2.txt")
user.writedata("/usr/home/pa/Text3.txt",h)






	
	


















