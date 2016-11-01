# Envy
Python3 .env reader (config files, similar to those used in Laravel)

Place your .env file next your script that is used to invoke the python interpreter 

**Default section is set to 'SETTINGS'**

__.env format__
```
[SETTINGS]
foo=bar
[FooBar]
bar=foo
```
__Usage__
```
Envy.get('foo')  # returns 'bar'
Envy.get('bar', 'FooBar')  # returns 'foo'
```
You can also use Envy to store your DB with set_db(func, args) where 
`func` is the function or method used to connect to your database and 
`args` the are arguments that will be passed to `func`, this way the
database connection will only be initialized once get_db() is called.
