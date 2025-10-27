import click
from collections import defaultdict

@click.command()
@click.option('--file', '-f', type=click.Path(exists=True), required=True, help='File to read')
@click.option('--ignore-case', '-i', is_flag=True, help='Ignore case when comparing lines')
@click.option('--ucount', '-c', is_flag=True, help='Show number of duplicates per line')
@click.option('--lines', '-l', type=int, help='Read only first N lines')
def main(file, ignore_case, ucount, lines):
    """Uniq-like CLI counting all duplicates, not only consecutive ones."""
    try:
        counter = defaultdict(int)
        originals = {}  
        read_count = 0

        click.echo(f"Debug: Reading file '{file}' with ignore_case={ignore_case}, ucount={ucount}, lines={lines}")
        with open(file, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                if lines is not None and read_count >= lines:
                    click.echo(f"Debug: Stopped after {read_count} lines")
                    break
                read_count += 1
                line_stripped = line.rstrip('\r\n').strip()
                click.echo(f"Debug: Line {read_count}: '{line_stripped}'")
                key = line_stripped.lower() if ignore_case else line_stripped
                click.echo(f"Debug: Key='{key}'")
                counter[key] += 1
                if key not in originals:
                    originals[key] = line_stripped

        click.echo(f"Debug: Found {len(counter)} unique lines")
        for key, count in sorted(counter.items()):  
            output = f"{count} {originals[key]}" if ucount else originals[key]
            click.echo(output)

    except FileNotFoundError:
        click.echo(click.style(f"Error: File '{file}' not found", fg='red', bold=True))
    except PermissionError:
        click.echo(click.style(f"Error: Permission denied for file '{file}'", fg='red', bold=True))
    except Exception as e:
        click.echo(click.style(f"Unexpected error: {e}", fg='red', bold=True))

if __name__ == "__main__":
    main()