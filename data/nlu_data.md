<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/rasa-starter-pack/704 --> 

## intent:goodbye <!--- The label of the intent --> 
- Bye 			<!--- Training examples for intent 'bye'--> 
- Goodbye
- See you later
- Bye bot
- Goodbye friend
- bye
- bye for now
- catch you later
- gotta go
- See you
- goodnight
- have a nice day
- i'm off
- see you later alligator
- we'll speak soon

## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot

## intent:thanks
- Thanks
- Thank you
- Thank you so much
- Thanks bot
- Thanks for that
- cheers
- cheers bro
- ok thanks!
- perfect thank you
- thanks a bunch for everything
- thanks for the help
- thanks a lot
- amazing, thanks
- cool, thanks
- cool thank you

## intent:affirm
- yes
- yes sure
- absolutely
- for sure
- yes yes yes
- definitely


## intent:name
- My name is [Juste](name)  <!--- Square brackets contain the value of entity while the text in parentheses is a a label of the entity --> 
- I am [Josh](name)
- I'm [Lucy](name)
- People call me [Greg](name)
- It's [David](name)
- Usually people call me [Amy](name)
- My name is [John](name)
- You can call me [Sam](name)
- Please call me [Linda](name)
- Name name is [Tom](name)
- I am [Richard](name)
- I'm [Tracy](name)
- Call me [Sally](name)
- I am [Philipp](name)
- I am [Charlie](name)
- I am [Charlie](name)
- I am [Ben](name)
- Call me [Susan](name)
- [Lucy](name)
- [Peter](name)
- [Mark](name)
- [Joseph](name)
- [Tan](name)
- [Pete](name)
- [Elon](name)
- [Penny](name)
- name is [Andrew](name)
- I [Lora](name)
- [Stan](name) is my name
- [Susan](name) is the name
- [Ross](name) is my first name
- [Bing](name) is my last name
- Few call me as [Angelina](name)
- Some call me [Julia](name)
- Everyone calls me [Laura](name)
- I am [Ganesh](name)
- My name is [Mike](name)
- just call me [Monika](name)
- Few call [Dan](name)
- You can always call me [Suraj](name)
- Some will call me [Andrew](name)
- My name is [Ajay](name)
- I call [Ding](name)
- I'm [Partia](name)
- Please call me [Leo](name)
- name is [Pari](name)
- name [Sanjay](name)


## intent:joke
- Can you tell me a joke?
- I would like to hear a joke
- Tell me a joke
- A joke please
- Tell me a joke please
- I would like to hear a joke
- I would loke to hear a joke, please
- Can you tell jokes?
- Please tell me a joke
- I need to hear a joke

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- i'm looking for a place in the [north](location) of town
- show me [chinese](cuisine) restaurants
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot
- search for restaurants
- anywhere in the [west](location)
- anywhere near [18328](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [29432](location)


## intent: order
- what is my [sale](table:order) in [last month](attribute:transaction_time)
- what is my [last month](attribute:transaction_time) [sale](table:order)
- what is my [current month](attribute:transaction_time) [sale](table:order)
- [current week](attribute:transaction_time) [sale](table:order)
- my [current month](attribute:transaction_time) [sale](table:order)
- What is [sales](table:order) in [last one week](attribute:transaction_time)
- What is [sales](table:order) in [last one day](attribute:transaction_time)
- What is [sales](table:order) in [last one month](attribute:transaction_time)
- what is my [previous month](attribute:transaction_time) [sales](table:order) 

## lookup: table
./data/table/table.txt

## lookup: attribute
./data/table/attribute.txt

## lookup: select_function
./data/table/function.txt


## intent: order_details
- What are [top](select_function:rank_top) performing [products](table:order_detail.product_id)
- What [products](table:order_detail) are selling slow
- What are [top](select_function:rank_top) performing [product](table:order_detail) by stores
- most selling [product](table:order_detail)
- what are newly added [products](table:order_detail)
- which [product](table:order_detail) are [most](select_function:rank_top) sold
- most demanding [product](table:order_detail)
- [products](table:order_detail) sold most
- tell me [most](select_function:rank_top) sold [products](table:order_detail)
- what are the [products](table:order_detail) sold this week


## intent: customer
- tell me those [customers](table:customer) who bought [nokia 6](attribute:name)
- who bought something yesterday
- [customers](table:customer) who shop for more than [50000](attribute:price)


## intent: product
- [products](table:product) added this month
- [products](table:product) cost more than 50000
- what are the [categories](attribute:category) of [products](table:product) we have
- total [products](table:product) we have
- how many [hp](attribute:name) [laptop](attribute:type) are in stock
- how many [electronics](attribute:category) gadgets we have
- types of [mobiles](attribute:type) we have
- what are the total no of [lappy](attribute:type) we have

