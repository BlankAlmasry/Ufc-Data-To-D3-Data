from matches import compile_matches
import click


@click.command()
@click.argument("file")
def main(file):
    """
    Compile matches from a csv file.
    """
    compile_matches(file)
    click.echo("Done")


if __name__ == '__main__':
    main()
