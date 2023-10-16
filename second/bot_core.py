import re
from typing import Optional


class AssistantBot:
    def __init__(self) -> None:
        """Initialize the bot with an empty contacts dictionary."""
        self.contacts = {}

    def execute_command(self, command: str) -> str:
        """Execute a given command and return the bot's response."""
        command_pattern = re.compile(r'(\w+)(?:\s+(.*))?')
        match = command_pattern.match(command)

        if not match:
            return "Invalid command."

        cmd, args = match.groups()
        cmd = cmd.lower()

        command_function = {
            "hello": self.hello,
            "add": self.add_contact,
            "change": self.change_contact,
            "phone": self.show_phone,
            "all": self.show_all,
        }.get(cmd)

        if command_function:
            return command_function(args)

        if cmd in ["close", "exit"]:
            raise SystemExit("Good bye!")

        return "Invalid command."

    def hello(self, _: Optional[str]) -> str:
        """Handle the 'hello' command."""
        return "How can I help you?"

    def check_args(self, args: Optional[str], expected_arg_count: int) -> bool:
        """Check if the input string contains the expected number of arguments."""
        return args is not None and len(args.split()) == expected_arg_count

    def add_contact(self, args: Optional[str]) -> str:
        """Add a contact to the contacts dictionary with improved error handling."""
        if self.check_args(args, 2):
            return "Invalid format for adding contact. Use 'add [name] [phone]'."

        name, phone = map(str.strip, args.split(None, 1))
        self.contacts[name] = phone
        return "Contact added."

    def change_contact(self, args: Optional[str]) -> str:
        """Change the phone number of an existing contact."""
        if self.check_args(args, 2):
            return "Invalid format for changing contact. Use 'change [name] [new phone]'."

        name, new_phone = map(str.strip, args.split())
        if name not in self.contacts:
            return f"No contact found for name: {name}."

        self.contacts[name] = new_phone
        return "Contact updated."

    def show_phone(self, args: Optional[str]) -> str:
        """Show the phone number for a given contact name."""
        if not args:
            return "Invalid format for showing phone. Use 'phone [name]'."

        name = args.strip()
        return self.contacts.get(name, f"No contact found for name: {name}.")

    def show_all(self, _: Optional[str]) -> str:
        """Show all saved contacts and their phone numbers."""
        if not self.contacts:
            return "No contacts saved."

        return '\n'.join([f"{name}: {phone}" for name, phone in self.contacts.items()])
