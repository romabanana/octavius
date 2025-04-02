import time
import random
import sys
import readline
from rich.console import Console
from rich.progress import Progress, BarColumn, track
from rich.spinner import Spinner
from rich.text import Text

# Create a console object for rich output
console = Console()

# Fake database of commands
fake_commands = {
    "ls": "Desktop  Documents  Downloads  Music  Pictures",
    "cat file.txt": "This is a fake file content.",
    "ping google.com": "Pinging google.com [64 bytes from 172.217.10.46]: 32 bytes=32 time=15ms",
    "clear": "",
    "LOAD": "",
}
def classic_progress_bar(total, current, bar_length=30):
    """Simulate a classic progress bar that updates in place."""
    progress = int((current / total) * bar_length)
    bar = f"[{'=' * progress}{' ' * (bar_length - progress)}] {current}%"
    
    sys.stdout.write("\r" + bar)  # Use \r to overwrite the line
    sys.stdout.flush()  # Force the update to appear
    time.sleep(0.1)  # Control speed of the progress

def simulate_download_and_install():
    """Simulate a download and installation process with realistic progress bar."""
    
    # Simulating download
    print("Downloading file...")
    total_steps = 100
    for step in range(total_steps + 1):
        classic_progress_bar(total_steps, step)
    print("\nDownload complete!\n")
    
    # Simulate installation with classic animation
    steps = [
        "Unpacking files...",
        "Configuring system...",
        "Installing dependencies...",
        "Finalizing installation..."
    ]
    
    for step in steps:
        print(step)
        time.sleep(1)  # Simulate a small delay for each installation step
    
    # Completion message
    print("Installation Complete!")

def welcome():
    console.clear()
    with open('welcome.txt', 'r') as file:
        content = file.read()
        console.print(content, style="cyan")                        
    console.print("[bold magenta]Welcome to Octavius[/bold magenta]")
        

def loading_effect():
    """Show a loading spinner for a fake process"""
    spinner = Spinner(name="dots", text="Loading...", style="green")
    with console.status("[bold green]Processing..."):
        time.sleep(3)  # Simulate processing

def fake_command_output(command):
    """Display fake command output based on the input"""
    if command in fake_commands:
        console.print(f"[bold green]$ {command}[/bold green]")
        readline.add_history(command)
        console.print(fake_commands[command])
    else:
        console.print("[bold red]Command not found[/bold red]")

def complete(text, state):
    """Provide completions for the command input"""
    options = [cmd for cmd in fake_commands if cmd.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None

def fake_console():
    """Fake console interface simulation"""
    welcome()
    
    # Enable autocompletion
    readline.set_completer(complete)
    readline.parse_and_bind("tab: complete")
    
    while True:
        user_input = console.input("[bold cyan]$ [/bold cyan]")
        
        if user_input.lower() == "exit":
            console.print("[bold red]Exiting Fake Terminal...[/bold red]")
            break
        elif user_input.lower() == "help":
            console.print("[bold blue]Available commands: ls, cat file.txt, ping google.com, clear[/bold blue]")
            readline.add_history("help")
        elif user_input.lower() == "clear":
            console.clear()
            readline.add_history("clear")
        elif user_input.lower() == "load":
            simulate_download_and_install()
            readline.add_history("load")
        elif user_input.lower().startswith("ping"):
            loading_effect()
            fake_command_output(user_input)
        else:
            fake_command_output(user_input)

if __name__ == "__main__":
    fake_console()

