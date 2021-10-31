import subprocess
import click
import glob
import os
import re

@click.command()
@click.argument('program')
@click.argument('tests_dir')
@click.option('-q', is_flag=True, help='Quiet: Don\'t print output of failed tests')
@click.option('--run_with', help='The program to run your program with')
def cli(program, tests_dir, q, run_with):
    '''
    Test a program. The PROGRAM argument is the path to your program.
    The TESTS_DIR argument is the path to a folder containing tests.
    For Java programs, use the  --run_with parameter (built in support coming soon!)
    '''

    # Make sure the test directory exists
    if not os.path.isdir(tests_dir):
        error(f'Could not find tests directory: {tests_dir}')
        exit(1)

    # Make sure that the program exists
    if not os.path.isfile(program):
        error(f'Could not find program: {program}')
        exit(1)

    # Run test on each file in the target directory
    for fname in glob.glob(tests_dir + '/*'):
        run_test(program, fname, not q)

    summary()


def run_test(program, fname, verbose):
    '''
    Run a test on the program using a given testfile
        program - Path of program to test
        fname   - Path of test file
        verbose - Whether or not to output failed tests
    '''
    # Read in test data
    with open(fname) as f:
        inp, exp = re.split('---+', f.read())

    # if the program is a python program, run with python
    if program.endswith('.py'):
        program = ['python', program]

    # Run the program (note: requires python 3.5+)
    try:
        res = subprocess.run(program, stderr=subprocess.PIPE, stdout=subprocess.PIPE, input=inp.encode())
        out = res.stdout.decode('utf-8')
        err = res.stderr.decode('utf-8')
    except PermissionError:
        error(f'Permission denied when trying to run program. Is it executable?')
        exit(2)

    # Check output
    if out.strip() == exp.strip():
        passed(fname)
    else:
        if verbose:
            failed_verbose(fname, out, exp, err)
        else:
            failed(fname)


n_passed = 0
n_failed = 0

def passed(fname):
    global n_passed
    click.echo('[' + click.style('PASS', bold=True, fg='green') + '] ' + fname)
    n_passed += 1


def failed(fname):
    global n_failed
    click.echo('[' + click.style('FAIL', bold=True, fg='red') + '] ' + fname)
    n_failed += 1


def failed_verbose(fname, out, exp, err):
    failed(fname)
    click.secho('--- Recieved ---', fg='red')
    click.echo(out)
    if err:
        click.secho('--- The following errors occored during program execution ---', fg='red')
        click.secho(err)
    click.secho('--- Expected ---', fg='red')
    click.echo(exp)
    click.secho('----------------', fg='red')


def summary():
    ''' Prints a summary of test results '''
    click.echo()
    if n_failed == 0:
        click.secho(f'✅ Passed all {n_passed + n_failed} tests :)', bold=True, fg='green')
    else:
        click.secho(f'❌ Falied {n_failed} tests', bold=True, fg='red')
    click.echo()


def error(msg):
    click.echo('[' + click.style('-', bold=True, fg='red') + '] ' + click.style(msg, bold=True, fg='red'))


if __name__ == '__main__':
    cli()


