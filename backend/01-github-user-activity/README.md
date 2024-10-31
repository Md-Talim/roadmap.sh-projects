# GitHub Activity CLI

A simple command-line interface (CLI) application built in Go to fetch and display the recent activity of a specified GitHub user.
This project helped me practice working with APIs, handling JSON data, and building CLI applications.

## Features

- Fetch recent activity for a GitHub user.
- Display activity such as pushes, issues, stars, creates, deletes, forks, and pull requests.
- Handle errors gracefully, including invalid usernames.

## Requirements

- Go (version 1.16 or later)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/github-activity-cli.git
cd github-activity-cli
```

2. Build the application:

```bash
go build
```

3. This will create an executable file named `github-activity` (or `github-activity.exe` on Windows).

## Usage

Run the CLI by providing a GitHub username as an argument:

```bash
./github-activity <username>
```

### Example

To fetch and display the recent activity of the user `kamranahmedse`, run:

```bash
./github-activity kamranahmedse
```

### Output

The output will display recent activities such as:

```
Pushed 3 commits to kamranahmedse/developer-roadmap
Opened a new issue in kamranahmedse/developer-roadmap
Starred kamranahmedse/developer-roadmap
```

## Error Handling

If the provided username is invalid, the CLI will return an error message similar to:

```
Error: Not Found
Check the username or see documentation: https://docs.github.com/rest/activity/events#list-events-for-the-authenticated-user
```
