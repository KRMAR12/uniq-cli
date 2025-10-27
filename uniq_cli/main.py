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
        originals = {}  # щоб зберігати перший оригінальний варіант рядка
        read_count = 0

        with open(file, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                if lines is not None and read_count >= lines:
                    break
                read_count += 1

                line_stripped = line.rstrip('\n')
                key = line_stripped.lower() if ignore_case else line_stripped

                counter[key] += 1
                if key not in originals:
                    originals[key] = line_stripped

        for key, count in counter.items():
            output = f"{count} {originals[key]}" if ucount else originals[key]
            click.echo(output)

    except Exception as e:
        click.echo(click.style(f"Error reading file: {e}", fg='red', bold=True))


if __name__ == "__main__":
    main()
