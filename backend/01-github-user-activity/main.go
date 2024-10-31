package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
)

type Event struct {
	Type string `json:"type"`
	Repo struct {
		Name string `json:"name"`
	} `json:"repo"`
	Payload struct {
		Commits []struct {
			Message string `json:"message"`
		} `json:"commits"`
		RefType string `json:"ref_type"` // For CreateEvent and DeleteEvent
		Action  string `json:"action"`   // For PullRequestEvent
		Forkee  struct {
			FullName string `json:"full_name"` // For ForkEvent
		} `json:"forkee"`
	} `json:"payload"`
}

func fetchUserActivity(username string) []Event {
	url := fmt.Sprintf("https://api.github.com/users/%s/events", username)

	resp, err := http.Get(url)
	if err != nil {
		log.Fatal("Failed to fetch data: ", err)
	}

	defer resp.Body.Close()

	// Handle 404 status, means user not found
	if uint(resp.StatusCode) == http.StatusNotFound {
		log.Fatalf("User not found: %d\nCheck the username and try again.", resp.StatusCode)
	}

	// Handle other non-200 status codes
	if resp.StatusCode != http.StatusOK {
		log.Fatalf("Failed to fetch data: %d", resp.StatusCode)
	}

	var events []Event
	if err := json.NewDecoder(resp.Body).Decode(&events); err != nil {
		log.Fatal("Failed to decode JSON:", err)
	}

	return events
}

func displayActivity(events []Event) {
	if len(events) == 0 {
		fmt.Println("No recent activity found.")
		return
	}

	for _, event := range events {
		repository := event.Repo.Name
		message := ""

		switch event.Type {
		case "PushEvent":
			message = fmt.Sprintf("Pushed %d commits to %s\n", len(event.Payload.Commits), repository)
		case "IssuesEvent":
			message = fmt.Sprintf("Opened a new issue in %s\n", repository)
		case "WatchEvent":
			message = fmt.Sprintf("Starred %s\n", repository)
		case "CreateEvent":
			message = fmt.Sprintf("Created %s in %s\n", event.Payload.RefType, repository)
		case "DeleteEvent":
			message = fmt.Sprintf("Deleted %s in %s\n", event.Payload.RefType, repository)
		case "ForkEvent":
			message = fmt.Sprintf("Forked %s to %s\n", repository, event.Payload.Forkee.FullName)
		case "PullRequestEvent":
			action := event.Payload.Action
			message = fmt.Sprintf("Pull request %s in %s\n", action, repository)
		default:
			message = fmt.Sprintf("Other activity in %s: %s\n", repository, event.Type)
		}

		fmt.Printf("- %s", message)
	}

}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: github-activity <username>")
		os.Exit(1)
	}

	username := os.Args[1]
	events := fetchUserActivity(username)
	displayActivity(events)
}
