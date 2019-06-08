puts "hens", 5+6%3
cars = 100
puts "there are #{cars} cars"
myname = 'vartika'
puts "i am #{myname}"
puts "*"*10
puts "i am %s" % myname
puts " i have to print %s %d" % [myname, cars]
plsprint = "kuchtohprintkardo"
puts plsprint
puts plsprint + '#'*5
print plsprint 
puts plsprint
formatter = "%s %s %s"
puts formatter % [1,22,3]
puts <<PARAGRAPH
hehe 
boo PARAGRAPH

i m dead
PARAGRAPH
puts "it prints the string", myname

#input = gets.chomp()#gives space automatically
#puts input
#require 'open-uri'

#open("http://www.ruby-lang.org/en") do |f|
  #  f.each_line {|line| p line}
  #  puts f.base_uri
 #   puts f.content_type

#end
first, second, third = ARGV
puts "the script is called: #{$0}"
puts " the variables are: #{first} #{second} #{third}"

#user = ARGV.first
#likes = STDIN.gets.chomp()
#the default gets method tries to treat the first one
#as a file and read from that. To read from the user’s 
#input (i.e., stdin) in such a situation, you have to 
#use it STDIN.gets explicitly
def addargs(arg1, arg2)
    puts "args: #{arg1}#{arg2}"
end
addargs(myname,cars)
#ex15 ex20 ex25 ex35 ex37
if 0<1
    puts"true"
elsif 1<0
    puts "false"
else
    puts "what to say"
end
the_count = [1,2,3,4,5]
for number in the_count
    puts "this is : #{number}"
end
#now using a block
the_count.each do |number|
    puts "a number is : #{number}"
end

elements = []
for i in(5..10)
    puts "add #{i} to the list"
    elements.push(i)
end
for i in elements
    puts "elements are: #{i}"
end 

i = 0
numbers = []
while i<6
    puts "at the top i is : #{i}"
    numbers.push(i)
    i = i+1
end

numbers.push(i+5)
puts numbers[1]
puts numbers[-1]
puts numbers.pop()
puts numbers.join(' ')
puts numbers.values_at(3,5).join('#')

# include? method

dictionaries = {'name' => 'vartika', :age => 15}
puts dictionaries['name']
puts dictionaries[:age]