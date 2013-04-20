Glass House
==========

A way to control an Indigo / Insteon smart home from Google Glass

Indigo is a great piece of OS X software that can control and manage an Insteon smart home.


This is a little side project that I am putting together in anticipation
of Glass.  I am a glass explorer, wohoo!

The Trello Board im using is at https://trello.com/b/1PHYs7Fk
The Talk Presentation is at #todo


Install Instructions for Indigo User:
    1. install indigo plugin in indigo 5+
    2. go to xglasshouse.appspot.com and signup
        a. it will ask for the dns to your indigo install
        b. it will ask you to authorize it to use mirror api and user info

Install Instructions for setting up your own appspot.
    1. create an appid
    2. create a project under the google api console at https://code.google.com/apis/console
        a. under "API Access", create a Client ID for web applications
    3.

Install Instructions for local dev environtment:
    1. pip install -r requirements_dev.txt

    To deploy to appengine:
        appcfg.py update appengine

    To iterate on the plugin:
        ./build_plugin.sh
        reload plugin in indigo


Requirements:

    Anyone wanting to use this will require the following:

    1. An Insteon setup, controlling it with Indigo.
    2. A static IP/DNS or dyndns on your home network and port forwarding
        to indigo, port 443 if you setup ngninx with ssl, otherwise port 5000
        to use the indigo plugin webserver directly.
        note: This plugin runs its own server.  For now it doesnt use the built in
        cherrypy server that is on indigo.  I wasn't able to find a clean way to
        add endpoints to it and also use the indigo api.

    3. Installing the GlassHouse Indigo plugin
        a. in the preferences, you will set your Glass House API Token

    4. A google account
        a. glasshouse will ask you to login to google and authorize glasshouse.



Architecture:

    Glass Tier:
    The Google Glass Mirror API.  Glasshouse will create and subscribe to
    a few cards that show house status information such as:  Motion, Doors open
    or closed, recent activity log, home variables like weather, water sensors,
    etc.

    Still to be understood... how to add items for voice commands on Glass...
    I would like to be able to take a command such as "OK Glass, are the garage
    doors shut?", or "OK Glass, shut the main garage door."


    Application Tier:
    I will create an appengine app that you can go to and authorize it to access
    your google glass via the Mirror API.  It will ask you for information like:
    house name, house ip/dns.   It will then retrieve a list of devices, actions
    and variables. Then a screen to allow you to choose your notification
    preferences for those things.  The app will give you a secret token the
    "Glass House API Token" to put into the House Tier's indigo plugin.

    I'll use https://github.com/kamalgill/flask-appengine-template

    # Development environment pip requirements file
    # Install via 'pip install -r requirements_dev.txt'

    PIL
    jinja2
    simplejson

    House Tier:
    This would be the indigo plugin which is just a flask dev server running
    on an indigo plugin process. I will run nginx in front of it for ssl and
    just map to the dev server port.
    This tier will have a set of RESTful endpoints, have some type of database
    like sqlite to track preferences for push notifications, and be able to send
    rest calls on certain events.


