import click
import os

@click.command()
@click.option('--file', '-f', type=click.Path(exists=True), required=True, help='File to read')
@click.option('--ignore-case', '-i', is_flag=True, help='Ignore case when comparing lines')
@click.option('--ucount', '-c', is_flag=True, help='Show number of duplicates per line')
@click.option('--lines', '-l', type=int, help='Read only first N lines')
def main(file, ignore_case, ucount, lines):
    """Unix uniq-like CLI (streaming, optionally limited lines)."""

    try:
        prev_line = None
        prev_line_proc = None
        line_count = 0
        read_count = 0

        with open(file, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                if lines is not None and read_count >= lines:
                    break
                read_count += 1

                line_stripped = line.rstrip('\n')
                line_proc = line_stripped.lower() if ignore_case else line_stripped

                if line_proc == prev_line_proc:
                    line_count += 1
                else:
                    if prev_line is not None:
                        output = f"{line_count} {prev_line}" if ucount else prev_line
                        click.echo(output)
                    prev_line = line_stripped
                    prev_line_proc = line_proc
                    line_count = 1

        if prev_line is not None:
            output = f"{line_count} {prev_line}" if ucount else prev_line
            click.echo(output)

    except Exception as e:
        click.echo(click.style(f"Error reading file: {e}", fg='red', bold=True))


if __name__ == "__main__":
    main()
