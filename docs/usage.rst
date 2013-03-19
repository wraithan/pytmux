Usage
=====

pytmux tries to keep to the `principle of least astonishment`_, much like
Python. If a command or configuration option is immediately obvious, please open
an issue and we can talk about how to improve the situation.

Commands
--------

list
~~~~

To list all of the available configs use::

  pytmux list

edit
~~~~

To create or edit a config, use::

  pytmux edit <name>

If you would like use a config as the base for a new config::

  pytmux edit <name> --copy <other_name>

run
~~~

To start or switch to a session use::

  pytmux run

doctor
~~~~~~

If you are having trouble with one of your configs, use::

  pytmux doctor

Configuration
-------------

Lets start with a base configuration, then we can walk through what each part
means.

.. code-block:: javascript

   {
       "name": "example",
       "directory": "~/devel/example",
       "windows": [
           {
               "name": "editor",
               "command": "emacs"
           },
           {
               "name": "some shell"
           },
           {
               "command": "tail -f some.log"
           },
           {}
       ]
   }

The first property is ``name`` which is the name of the session. This should be
a short descriptive name of the what you'll be using the session for. You'll
want to make sure it is unique so can run it and not conflict with other running
sessions.

Next you have the ``directory`` property which is what directory to use for
starting each window. It is optional, if it isn't provided then the current
directory that pytmux is run from is used.

After that you have ``windows`` which is the list of windows you want
instantiated. Both of the properties (``name`` and ``command``) are optional. If
you specify a ``name`` it will name the window that, without a ``name`` you'll
get a window named using ``automatic-rename`` in tmux (which uses lets the
program set the title). If you specify a ``command`` then that will be run in
the window using ``send-keys``, without the ``command`` it will open your
default shell. Without either, you'll get a default shell, in a window that uses
``automatic-rename``.

.. _`principle of least astonishment`: http://en.wikipedia.org/wiki/Principle_of_least_astonishment
