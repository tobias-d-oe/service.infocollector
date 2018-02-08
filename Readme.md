Service Infocollector
=====================
This Service Addon collects Info Variables and creates a container for use within a list control.

There are different rules which can be configured to define if a Item should be added to the list or not.

For this the following possibilities can be choosen:
Without compare
- issetpic (if there is any content in the INFO Variable)
- isunsetpic (if no content is in the INFO Variable)
With compare
- gepic (greater or equal comparativ)
- gpic (greater comparativ)
- lepic (less or equal comparativ)
- lpic (less comparativ)
- ispic (is comparativ)

An example configuration can be found in the folder integration.
This configuration file should be present in the addon directory of your userdata folder.
As example for Linux Systems "~/.kodi/userdata/addon_data/service.infocollector/infovars.json".

Also you can have f.e. "gepic" and "lpic" within one statement so if a value is greater or equal comparativ it shows pic1 and if less comparativ it shows pic2.


