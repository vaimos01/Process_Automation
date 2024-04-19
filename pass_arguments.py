import argparse
def parser():
  pars = argparse.ArgumentParser(description='Mention the purpose of this parser')
  pars.add_argument("-y", "--yes",required=True)
  args = pars.parse_args()
  print(args.yes)
