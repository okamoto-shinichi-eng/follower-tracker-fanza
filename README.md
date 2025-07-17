# FANZA Games Follower Tracker

This project tracks the daily follower count of @fanzagames_jhg on X (formerly Twitter) via scraping.

## Features

- Uses Selenium to scrape follower count.
- Runs daily at 9:00 JST via GitHub Actions.
- Appends data to `logs/followers.csv`.

## Usage

1. Clone the repo.
2. Push to GitHub.
3. GitHub Actions will run automatically every day.
