# rename string_extend.rb

class Strings

# Ruby has a capitalize method below
# capitalizes the first letter of a string
# in order to capitalize the first letter of every
# word we havbe to write
    def titleize
        self.split(' ').collect {|word| word.capitalize}.join(" ")
    end
end
