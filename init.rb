# need to rename init.rb

APP_ROOT = File.dirname(__FILE__)

# require "#{APP_Root}/lib/guide"
# require File.join(APP_ROOT,'lib','guide')

$:.unshift(File.join(APP_ROOT, 'lib'))
require 'guide'

guide = Guide.new
guide.launch!