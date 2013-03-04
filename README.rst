pytmux
======

This is a simple wrapper around tmux to allow you to define a session in a JSON
file. This is to avoid having to do all the setup of making the session with a
name, opening the windows with the right names and commands, and doing so in a
consistent manner. Also, if the session already exists, it will just open it
for you.

Usage
-----

To start a new configuration or edit an existing one::

  pytmux edit <config>

To run it::

  pytmux run <config>

To list all configs::

  pytmux list

Configs
-------

JSON will be used for configs::

  {
      "name": "sample",
      "windows": [
          {
              "name": "dev server",
              "command": "./manage.py runserver"
          }, {
              "name": "some shell"
          }, {
              "command": "emacs"
          }, {}
      ]
  }

Will open a tmux session named ``sample`` with 4 windows open. The first will
be named ``dev server`` and will have ``./manage.py runserver`` running in
it. The second will be a window named ``some shell`` which will have the system
default shell running in it. The third will default to using
``automatic-rename`` and will have ``emacs`` running in it. The final will be a
window with ``automatic-rename`` and the system default shell.

Why
---

Honestly, I don't want to build this, but none of the currently existing tmux
wrappers seem interested in supporting not naming windows and letting tmux do
its ``automatic-rename`` thing. Also they use YAML and I prefer JSON.

Prior Art
---------

There are a couple that exist already but don't make me happy.

- `tmuxinator <https://github.com/aziz/tmuxinator>`_
- `teamocil <https://github.com/remiprev/teamocil>`_
