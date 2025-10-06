import csv
import sys
import getpass
import requests

# Ask the user for necessary inputs. The token is requested at runtime so
# it is not stored in source control.
GITHUB_TOKEN = getpass.getpass("Enter GitHub token (will not be stored): ")
if not GITHUB_TOKEN:
    print("ERROR: no GitHub token provided. Exiting.")
    sys.exit(1)
# for future use, owner, repo and csv file can also be requested at runtime
# but for now we hardcode them for speed while testing/failing repeatedly
REPO_OWNER = "illusio666"
REPO_NAME = "HackathonTest"
CSV_FILE = "test2.csv"

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}


def create_issue(title, body, labels, milestones, assignees):
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues'

    # Convert labels, milestones, and assignees to list format for GitHub API
    labels_list = ([label.strip() for label in labels.split(',')]
                   if labels else [])
    assignees_list = ([assignee.strip() for assignee in assignees.split(',')]
                      if assignees else [])
    milestones_list = (
        [milestone.strip() for milestone in milestones.split(',')]
        if milestones else []
    )

    data = {
        'title': title,
        'body': f"{body}\n\n**Milestone:** {milestones}",
        'labels': labels_list,
        'assignees': assignees_list,
        'milestones': milestones_list[0] if milestones_list else None
        # Only one milestone can be assigned
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f'✅ Created: {title} with labels: {labels_list}')
        print(f'   Assignees: {assignees_list}')
    else:
        print(f'❌ Failed: {title} | {response.status_code} - {response.text}')


def import_issues(CSV_FILE):
    with open(CSV_FILE, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            create_issue(row['title'], row['body'], row['labels'],
                         row['milestones'], row['assignees'])


if __name__ == '__main__':
    import_issues(CSV_FILE)
