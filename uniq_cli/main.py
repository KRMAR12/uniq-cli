import click
import os

def read_first_lines(file_path, num_lines=None, num_bytes=None):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    if num_bytes is not None:
        with open(file_path, 'rb') as f:
            data = f.read(num_bytes)
        return data.splitlines()
    elif num_lines is not None:
        lines = []
        with open(file_path, 'rb') as f:
            for _ in range(num_lines):
                line = f.readline()
                if not line:
                    break
                lines.append(line.rstrip(b'\n'))
        return lines
    else:
        raise ValueError("Specify either num_lines or num_bytes.")

@click.command()
@click.option('--name', '-n', default='World', help='Your name')
@click.option('--count', '-c', default=1, help='Number of greetings')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
@click.option('--uppercase', is_flag=True, help='Print in uppercase')
@click.option('--color', type=click.Choice(
    ['black','red','green','yellow','blue','magenta','cyan','white'], case_sensitive=False),
    default='green', help='Color of greetings')
@click.option('--file', '-f', type=click.Path(exists=True), help='File to read')
@click.option('--lines', '-l', type=int, help='Number of lines')
@click.option('--bytes', '-b', type=int, help='Number of bytes')
def main(name, count, verbose, uppercase, color, file, lines, bytes):
    """Main CLI function"""
    

    message = f"Hello, {name}!"
    if uppercase:
        message = message.upper()
    for i in range(count):
        text = f"[{i+1}/{count}] {message}" if verbose else message
        click.echo(click.style(text, fg=color.lower(), bold=True))

    if file:
        try:
            result = read_first_lines(file, num_lines=lines, num_bytes=bytes)
            click.echo(click.style(f"\nContents from {file}:", fg='magenta', bold=True))
            for idx, line in enumerate(result, start=1):
                click.echo(click.style(f"{idx:>3}: {line.decode('utf-8', errors='replace')}", fg='yellow'))
        except Exception as e:
            click.echo(click.style(f"Error reading file: {e}", fg='red', bold=True))

if __name__ == "__main__":
    main()
