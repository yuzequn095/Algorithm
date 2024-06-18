import json
import os

DATA_FILE = 'leetcode_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    else:
        return {'id_to_tags': {}, 'tag_to_ids': {}}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def query_tags_by_id(problem_id):
    data = load_data()
    return data['id_to_tags'].get(problem_id, 'Problem ID not found')

def query_ids_by_tag(tag):
    data = load_data()
    return data['tag_to_ids'].get(tag, 'Tag not found')

def add_problem(problem_id, tags):
    data = load_data()
    
    # Add to id_to_tags map
    data['id_to_tags'][problem_id] = tags
    
    # Add to tag_to_ids map
    for tag in tags:
        if tag not in data['tag_to_ids']:
            data['tag_to_ids'][tag] = []
        data['tag_to_ids'][tag].append(problem_id)
    
    save_data(data)
    print(f'Problem {problem_id} with tags {tags} has been added.')

def main():
    while True:
        print("\nLeetCode Algorithm Management System")
        print("1. Query tags by problem ID")
        print("2. Query problem IDs by tag")
        print("3. Add a problem with tags")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            problem_id = input("Enter problem ID: ")
            print(f'Tags: {query_tags_by_id(problem_id)}')

        elif choice == '2':
            tag = input("Enter tag: ")
            print(f'Problem IDs: {query_ids_by_tag(tag)}')

        elif choice == '3':
            problem_id = input("Enter problem ID: ")
            tags = input("Enter tags (comma-separated): ").split(',')
            add_problem(problem_id, tags)

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
