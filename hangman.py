from random import choice

class Hangman(object):        
    @staticmethod
    def get_failed_image(case):
        options = {
           7 : "\n\n\n\n-+-",
           6 : "\n |  \n | \n | \n-+-",
           5 : " +--- \n | \n | \n | \n-+-",
           4 : " +--+ \n |  O \n | \n | \n-+-",
           3 : " +--+ \n |  O \n |  | \n | \n-+-",
           2 : " +--+ \n |  O \n | /|\ \n | \n-+-",
           1 : " +--+ \n |  O \n | /|\ \n | / \ \n-+-",
        }
        return options[case]
        
    def __init__(self, favourite_words_list):        
        self.name = (choice(favourite_words_list)).lower()
        self.total_success_attempt = 0
        self.attempted_list = [' ' for n in range(len(self.name))]
        self.failed_attempt = 8        
        print "Word length is %s"%len(self.name)
        #~ print self.name
        
    def check_input_val(self, input_char):
        try:
            assert type(input_char) is not 'str'
            assert(input_char) != 1
        except AssertionError:
            print "Please enter a char"
        return input_char.lower()
    
    def update_result(self, input_char):
        if input_char not in self.attempted_list:
            found = False
            for p, v in enumerate(self.name):
                if v == input_char:
                    self.attempted_list[p] = v
                    found = True
                    self.total_success_attempt += 1
            if not found:
                self.failed_attempt -= 1                   
                
        else:
            self.failed_attempt -= 1

favourite_words_list = ['Python', 'Django', 'Flask', 'Postgresql']

HM = Hangman(favourite_words_list)

while (HM.failed_attempt > 1):    
    entered_char = raw_input("\nEnter A Letter:\t")
    entered_char = HM.check_input_val(entered_char)    
    HM.update_result(entered_char)
    if HM.failed_attempt != 8:
        print Hangman.get_failed_image(HM.failed_attempt)
    print ''.join(HM.attempted_list)
    print ''.join(['-' for n in range(len(HM.name))])
    
    if len(HM.name) == HM.total_success_attempt:
        print "Successfully Finished!!!!!!!!!"
        break

