# Jacob Hammargren
# picoCTF Automation
# level: ALL

import Web.Cookies, Web.getAHEAD, Web.Insp3ct0r, Web.ScavengerHunt, Web.SomeAssemblyRequired, Web.WhereAreTheRobots, Web.logon, Web.DontUseClientSide

global levels
levels = {'0' : Web.Cookies, '1' : Web.getAHEAD, '2' : Web.Insp3ct0r, '3' : Web.ScavengerHunt, '4' : Web.SomeAssemblyRequired,
         '5' : Web.WhereAreTheRobots, '6' : Web.logon, '7' : Web.DontUseClientSide}

def main():
    while True:
        print("Avaliable Levels\n")
        for i in levels:
            print(i + ' ', levels[i].__name__)
        q = input("\nWhich level would you like to solve?: ")
        solve(levels[q], q)
def solve(level, num):
    display(level.run(), num)
    

def display(flag, level):
    print(f'____________\n│FLAG FOUND:\033[1m ====> {flag} \033[0m\n│Level: {levels[level].__name__}\n')
    while True:
        q = input("Do you want to solve another? (y or n): ")
        if q == 'y':
            break
        else:
            exit()

main()
