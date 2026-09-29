# Name: Tsegawit Gebremedhin
# Date: September 28, 2026
# Assignment: Week 1 - PA2
# Purpose: This program uses Redis to create, retrieve, update, and
# delete sets in a Redis key-value database.

import redis

# Connect to the Redis database
r = redis.Redis(host='localhost', port=6379, db=0)


# Display the main menu
def main_menu():
    while True:
        print("\nType in a number and press enter to execute the menu option.")
        print("1. Query for set members")
        print("2. Add a new set")
        print("3. Update members of a set")
        print("4. Delete a set")
        print("5. Delete all data from the database")
        print("6. Exit the program")

        choice = input()

        # Retrieve members of a set
        if choice == "1":
            key = input("\nEnter the key of the set you wish to query:\n")
            members = r.smembers(key)
            print("\nSet members:")
            for member in members:
                print(member)

        # Create a new set
        elif choice == "2":
            key = input("\nEnter the key you wish to add:\n")
            count = int(input("\nEnter how many members will this set have:\n"))

            for i in range(count):
                member = input("\nEnter the next member value:\n")
                r.sadd(key, member)

            print("\nSet created successfully.")

        # Update members of a set
        elif choice == "3":
            key = input("\nEnter the key of the set you wish to update:\n")

            if not r.exists(key):
                print("\nThat set does not exist.")
                continue

            while True:
                print("\nPlease type in a number and press enter to execute the menu option")
                print("1. Add new member")
                print("2. Remove member")
                print("3. Remove all members")
                print("4. Exit Update Menu")

                update_choice = input()

                if update_choice == "1":
                    member = input("\nEnter the new member value:\n")
                    r.sadd(key, member)
                    print("\nMember added.")

                elif update_choice == "2":
                    member = input("\nEnter the member value to remove:\n")
                    r.srem(key, member)
                    print("\nMember removed.")

                elif update_choice == "3":
                    members = r.smembers(key)
                    print("\nRemoving all set members...")

                    for member in members:
                        print("Removing Member:", member, "...")
                        r.srem(key, member)

                    print("\nThe cardinality of the set is now:")
                    print(r.scard(key))

                elif update_choice == "4":
                    break

                else:
                    print("\nInvalid option. Please try again.")

        # Delete a specific set
        elif choice == "4":
            key = input("\nEnter the key of the set you wish to delete:\n")
            r.delete(key)
            print("\nSet deleted.")

        # Delete all data from Redis
        elif choice == "5":
            confirm = input(
                "\nAre you sure you want to delete ALL database data? (yes/no):\n"
            )
            if confirm.lower() == "yes":
                r.flushdb()
                print("\nAll database data deleted.")
            else:
                print("\nDelete all cancelled.")

        # Exit the program
        elif choice == "6":
            print("\nExiting program.")
            break

        else:
            print("\nInvalid option. Please try again.")


# Run the application
if __name__ == "__main__":
    main_menu()
