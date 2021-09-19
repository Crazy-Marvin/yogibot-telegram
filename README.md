[![Telegram Subway Bot](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)](https://t.me/SubwayBot)
[![GitHub Actions](https://github.com/Crazy-Marvin/yogibot-telegram/actions/workflows/ci.yml/badge.svg)](https://github.com/Crazy-Marvin/yogibot-telegram/actions/workflows/ci.yml)
![healthchecks.io](https://img.shields.io/endpoint?url=https%3A%2F%2Fhealthchecks.io%2Fbadge%2F396c7d03-faf7-4562-9f83-1194d0%2F31QvRDxH%2FSubway.shields)
[![License](https://img.shields.io/github/license/Crazy-Marvin/yogibot-telegram)](https://github.com/Crazy-Marvin/yogibot-telegram/blob/trunk/LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/Crazy-Marvin/yogibot-telegram.svg?style=flat)](https://github.com/Crazy-Marvin/yogibot-telegram/commits)
[![Releases](https://img.shields.io/github/downloads/Crazy-Marvin/yogibot-telegram/total.svg?style=flat)](https://github.com/Crazy-Marvin/yogibot-telegram/releases)
[![Latest tag](https://img.shields.io/github/tag/Crazy-Marvin/yogibot-telegram.svg?style=flat)](https://github.com/Crazy-Marvin/yogibot-telegram/tags)
[![Issues](https://img.shields.io/github/issues/Crazy-Marvin/yogibot-telegram.svg?style=flat)](https://github.com/Crazy-Marvin/yogibot-telegram/issues)
[![Pull requests](https://img.shields.io/github/issues-pr/Crazy-Marvin/yogibot-telegram.svg?style=flat)](https://github.com/Crazy-Marvin/yogibot-telegram/pulls)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/a9ec4ee98a93425ca8162b369adce3db)](https://www.codacy.com/gh/Crazy-Marvin/yogibot-telegram/dashboard?utm_source=github.com&utm_medium=referral&utm_content=Crazy-Marvin/yogibot-telegram&utm_campaign=Badge_Grade)
[![Dependabot](https://badgen.net/badge/icon/dependabot?icon=dependabot&label)](https://python.org/)
![Snyk Vulnerabilities for GitHub Repo](https://img.shields.io/snyk/vulnerabilities/github/Crazy-Marvin/yogibot-telegram)
[![Telegram Subway Bot](https://img.shields.io/badge/Python-yellow?logo=python)](https://t.me/YogiTelegramBot)

# Subway Telegram Bot

This [bot](http://t.me/YogiTelegramBot) shows you the Sub of the Day.

### Requirements

- Token from [@Botfather](https://telegram.me/botfather)
- SSL certificate (I recommend [Let's Encrypt](https://letsencrypt.org/))
- Webserver running [Python](https://www.python.org) (tested with [Apache](https://httpd.apache.org/) & [NGINX](https://www.nginx.com/) but others should work too)
- [Healthchecks](https://healthchecks.io/#php) URL (optional)
- Google Cloud service account credentials (JSON) for accessing Google Sheets API & Google Drive API

### Setup

- Create two Google Spreadsheets called YOGI BOT DATABASE and ANALYTICS
- Create a Google Forms form for feedback
- Create a Google Cloud project with access to the Google Sheets API & Google Drive API and download the JSON
- Give that service account editor rights for both spreadsheets
- Run the script

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.
More details may be found in the [CONTRIUBTING.md](https://github.com/Crazy-Marvin/yogibot-telegram/tree/trunk/.github/CONTRIBUTING.md).

### License

[MIT](https://choosealicense.com/licenses/mit/)
