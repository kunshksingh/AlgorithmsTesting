import subprocess
import click
import os
import glob

@click.command()
@click.argument('program')
@click.option('-q', is_flag=True, help='Quiet: Don\'t print output of failed tests')
@click.option('--run_with', help='The program to run your program with')
def cli(program, q, run_with):
    dir_name = 'module-01/*'

    # Make sure that the binary exists
    if not os.path.isfile(program):
        error(f'Could not find program: {program}')
        exit(1)

    # Get each file in the appropriate directory
    for fname in glob.glob(dir_name):
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
        inp, exp = f.read().split('-----')
        inp = inp.strip()
        exp = exp.strip()

    # if the program is a python program, run with python
    if program.endswith('.py'):
        program = ['python', program]

    # Run the program (note: requires python 3.5+)
    res = subprocess.run(program, stdout=subprocess.PIPE, input=inp.encode())
    out = res.stdout.decode('utf-8')
    if out == exp:
        passed(fname)
    else:
        if verbose:
            failed_verbose(fname, out, exp)
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

def failed_verbose(fname, out, exp):
    failed(fname)
    click.secho('--- Recieved ---', fg='red')
    click.echo(out)
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

def error(msg):
    click.echo('[' + click.style('-', bold=True, fg='red') + '] ' + click.style(msg, bold=True, fg='red'))


if __name__ == '__main__':
    cli()


