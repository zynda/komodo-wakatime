
History
-------


3.0.6 (2017-05-24)
++++++++++++++++++

- Upgrade wakatime-cli to v8.0.2.
- Only treat proxy string as NTLM proxy after unable to connect with HTTPS and
  SOCKS proxy.
- Ability to disable SSL cert verification. wakatime/wakatime#90
- Disable line count stats for files larger than 2MB to improve performance.
- Config file not needed when passing api key via command line.
- Allow colons in [projectmap] config section. wakatime/wakatime#83
- When unable to detect language and debug mode turned on, log any tracebacks.
- Increase priority of F# and TypeScript languages.
- Add six library to satisfy missing dependency from ntlm-auth.


3.0.5 (2017-02-20)
++++++++++++++++++

- Upgrade wakatime-cli to v7.0.2.
- Support for SOCKS proxies.
- Support NTLM proxy format like domain\\user:pass.
- Allow boolean or list of regex patterns for hidefilenames config setting.
- New WAKATIME_HOME env variable for setting path to config and log files. #67
- New hostname setting in config file to set machine hostname. Hostname
  argument takes priority over hostname from config file.
- Support for Python 3.6.


3.0.4 (2016-05-26)
++++++++++++++++++

- Minor bugfix when prompting for api key at startup.


3.0.3 (2016-05-26)
++++++++++++++++++

- Make sure api key is valid format.


3.0.2 (2016-05-25)
++++++++++++++++++

- Add support for Komodo 10.
- Upgrade wakatime-cli to v6.0.3.
- Support for SOCKS proxies.
- Prevent popup on Mac when xcode-tools is not installed.
- Fix bug which prevented plugin from being sent with extra heartbeats.
- Increase default network timeout to 60 seconds when sending heartbeats to
  the api.
- Support regex patterns in projectmap config section for renaming projects.
- Upgrade pytz to v2016.3.
- Upgrade tzlocal to v1.2.2.
- Upgrade requests package to v2.9.1.
- Improve C# dependency detection.
- Log all unknown exceptions to wakatime.log file.
- Disable urllib3 SSL warning from every request.
- Detect dependencies from golang files.
- Use api.wakatime.com for sending heartbeats.
- Improve dependency detection.
- Send hostname in X-Machine-Name header.
- Upgrade argparse to v1.3.0.
- Move language translations to api server.
- Move extension rules to api server.
- Detect correct header file language based on presence of .cpp or .c files
  named the same as the .h file.
- Reuse SSL connection across multiple processes for improved performance.
- Added api_url config option and --apiurl cli argument for customizing api
  url.
- Capture warnings in log file.


3.0.1 (2015-04-05)
++++++++++++++++++

- refactor extension and fix bugs
- detect python binary from common locations for Windows
- alert if python not found


3.0.0 (2015-04-01)
++++++++++++++++++

- fix keypress listener
- add WakaTime menu item to change api key


2.0.4 (2015-04-01)
++++++++++++++++++

- only unbind previous event listener when view is not null


2.0.3 (2015-04-01)
++++++++++++++++++

- add missing file from wakatime package


2.0.2 (2015-04-01)
++++++++++++++++++

- fix prompt for API key
- upgrade external wakatime package to v4.0.6


2.0.1 (2015-03-26)
++++++++++++++++++

- support for Komodo 9
- upgrade external wakatime package to v4.0.4
- new options for excluding and including directories
- use requests library instead of urllib2, so api SSL cert is verified
- new proxy config file item for https proxy support
- detect frameworks from JavaScript and JSON files
- detect JavaScript frameworks from script tags in Html template files
- remove unused dependency, which is missing in some python environments
- ignore errors from malformed markup (too many closing tags)


2.0.0 (2014-12-23)
++++++++++++++++++

- upgrade external wakatime package to v3.0.1
- detect libraries and frameworks for C++, Java, .NET, PHP, and Python files


1.0.7 (2014-12-22)
++++++++++++++++++

- upgrade external wakatime package to v2.1.11
- fix bug in offline logging when no response from api


1.0.6 (2014-11-18)
++++++++++++++++++

- upgrade external wakatime package to v2.1.6
- fix list index error when detecting subversion project


1.0.5 (2014-11-12)
++++++++++++++++++

- upgrade external wakatime package to v2.1.4
- when Python was not compiled with https support, log an error to the log file


1.0.4 (2014-11-10)
++++++++++++++++++

- upgrade external wakatime package to v2.1.3
- correctly detect branch for subversion projects


1.0.3 (2014-09-30)
++++++++++++++++++

- upgrade external wakatime package to v2.1.1
- fix bug where binary file opened as utf-8


1.0.2 (2014-09-30)
++++++++++++++++++

- upgrade external wakatime package to v2.1.0
- python3 compatibility changes


1.0.1 (2014-07-25)
++++++++++++++++++

- upgrade external wakatime package to v2.0.5
- use unique logger namespace to prevent collisions in shared plugin environments
- option in .wakatime.cfg to obfuscate file names


1.0.0 (2014-06-23)
++++++++++++++++++

- Birth

