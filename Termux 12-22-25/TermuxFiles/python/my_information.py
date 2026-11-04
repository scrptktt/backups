from brevard_jobs import Job_History

class information():
    def __init__(self, name, phone, address, cash, credit_score):
        self.name = name
        self.phone = phone
        self.address = address
        self.cash = str(cash)
        self.credit_score = credit_score
        ''' money is cheaper when credit is better
            *Credit score calculated based on FICO® Score 8 model. 
            Your lender or insurer may use a 
            different FICO® Score than FICO® Score 8, 
            or another type of credit score altogether.
            https://www.experian.com/help/fico-score-disclosure/ 
        
            I authorize ConsumerInfo.com, Inc., 
            also referred to as Experian Consumer Services ("ECS"), 
            to obtain my credit report and/or credit score(s), 
            on a recurring basis to:
                Provide my credit report (and/or credit score) to me 
                        for review while I have an account with ECS.
                Notify me of other products and services that may be available to me 
                                    through ECS or through unaffiliated third parties.
                Notify me of credit opportunities and advertised credit offers.
        '''


        # '$' + [ i for i in str(cash) if len(int(cash)) % 3 == 0] 

        self.data = [self.name, self.phone, self.address, self.cash]
    def __str__(self):
        return str(self.data)
    def print_self(self):
        print("Self Information\n================")
        for i in self.data:
            if type(i) == tuple:
                for j in i:
                    print(j)           
            else: print(i)
        print()
    def update_cash(self, value):
        self.data[3] = '$'+str(value)

##################################################################################
############################.__###########################__######___.############
##_____________###_______##_|__|#____##__#__##______#####|__|#____\_ |__###______#
##\____ \_  __ \#/ __ \  \/ /  |/  _ \|  |  \/  ___/#####|  |/  _ \| __ \ /  ___/#
##|  |_> >  |#\/\  ___/\   /|  (  <_> )  |  /\___ \######|  (  <_> ) \_\ \\___ \##
##|   __/|__|####\___  >\_/ |__|\____/|____//____  >#/\__|  |\____/|___  /____  >#
##|__|###############\/##########################\/##\______|##########\/#####\/##
##================================================================================ 
The_brine_and_bottle = Job_History("Dishwasher",
                                   'Dishwasher',
                                   'The Brine and Bottle',
                                   'Andrew',
                                   '(252) 715-1818',
                                   '7531 S Virginia Dare Trail\nNags Head NC, 27959',
                                   '04/01/2010 - 12/15/2013')
                                    # info@thebrineandbottle.com
Luckys_market = Job_History("Pizza",
                            'Pizza Cook',
                            'Luckys Market',
                            'Andrew',
                            '(352) 240-6440',
                            '1459 NW 23rd Ave,\nGainesville FL, 32605',
                            '06/01/2018 - 12/15/2019')
The_Depot = Job_History("Dishwasher",
                        'Dishwasher',
                        'The Depot',
                        'Antonio',
                        '(352) 591-0145',
                        '22060 N US Hwy 441,\nMicanopy FL 32667',
                        '02/01/2020 - 10/15/2020')
Dominos = Job_History("Pizza",
                      'CSR',
                      'Dominos',
                      '-',
                      '(252) 441-1525',
                      '1400 S Croatan Hwy,\nKill Devil Hills NC 27968',
                      '10/01/2021 - 11/15/2021')


################################################################
############________############################################
###########/  _____/______##____##__#________##______###########
##########/   \  __\_  __ \/  _ \|  |  \____ \/  ___/###########
##########\    \_\  \  | \(  <_> )  |  /  |_> >___ \ ###########
###########\______  /__|   \____/|____/|   __/____  >###########
##################\/###################|__|#######\/############
#===============================================================    
favorite_jobs = [The_brine_and_bottle, Luckys_market]
jobs = [The_brine_and_bottle, Luckys_market, The_Depot, Dominos]
job_names = [job.employer for job in jobs]

#&&&&&&&&&&&&&&&&&__&&.__&&&&&&&&&&&&&&&.___&&&&&&&&
#&&&_____&&&_____/  |_|  |__&&&____&&&__| _/______&&
#&&/     \_/ __ \   __\  |  \&/  _ \&/ __ |/  ___/&&
#&|  Y Y  \  ___/|  | |   Y  (  <_> ) /_/ |\___ \&&&
#&|__|_|  /\___  >__| |___|  /\____/\____ /____  >&&
#&&&&&&&\/&&&&&\/&&&&&&&&&&\/&&&&&&&&&&&\/&&&&\/&&&&
def work_history():
    def display_list():
        for index, job in enumerate(job_names):
            print(str(index + 1)+'.', job, end='\n')
    
    display_list()
    print("\nEnter a choice from the list above:\n[\'p\' is for pizza, \'d\' is for dishwasher).")
    user_input = input()
    print()
    
    if user_input.lower() == 'p':
        for job in jobs:
            if job.jobtype.lower() == 'pizza':
                job.print_self()
    elif user_input.lower() == 'd':
        job_list = []
        for job in jobs:
            if job.jobtype.lower() == 'dishwasher':
                job.print_self()
    elif user_input.lower() == 'all':
        for job in jobs:
            job.print_self()   
    else:
        for index, job in enumerate(jobs):
            if int(user_input) == (index + 1):
                job.print_self()
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$_____$$$$$$$$$$$$$$$$$$$$__$$.__$$$$$$$$$$$$$$$$$$$$$$$$
#$_/ ____\_$__$$____$$$_____/  |_|__|$____$$$____$$$______$$
#$\   __\  |  \/    \_/ ___\   __\  |/  _ \$/    \ /  ___/$$
#$$|  | |  |  /   |  \  \___|  |$|  (  <_> )   |  \\___ \$$$
#$$|__| |____/|___|  /\___  >__|$|__|\____/|___|  /____  >$$
#$$$$$$$$$$$$$$$$$$\/$$$$$\/$$$$$$$$$$$$$$$$$$$$\/$$$$$\/$$$

work_history()


