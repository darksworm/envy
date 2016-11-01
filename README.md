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
You can also use Envy to store your DB with set_db() and get_db()
