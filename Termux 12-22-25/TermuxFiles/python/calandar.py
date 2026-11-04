import time

            # Class info.
            # ===========
            # Prefix, Section, Credit Hours, CRN
            # Name, length (minutes)

            # Exif info.
            # ==========
            # Instructor, Subject, Type, Grade, Level, Term, startDate, endDate, Building, Room 

            # Schedule info.
            # ==============
            # Day, Begin, End

Classes = [(("ITEC 3290", "001", 3, 84456,
            "Technical Writing", 45), 
            #
            ('Carolyn Dunn', 'NATURAL SCIENCE', 'Lecture', 'Standard Letter Grade',
             'Undergraduate', '08/19/2024', '12/11/2024', 'Flanagan', '00262', 
             ('ENGL 2201')),
            #
            ('Monday', 'AM 9:00', 'AM 9:50'),
            ('Wednesday', 'AM 9:00', 'AM 9:50'), 
            ('Friday', 'AM 9:00', 'AM 9:50')),
            # Title:        Technical Writing
            # College:      College of Engr and Technology TC
            # Department:   Technology Systems TS
            # Hours:
            #       Credit Hours:3
            #       Lecture: 3
            # Levels:
            #       Undergraduate UG
            # Grading Modes:
            #       Forgiveness F
            #       Standard Letter Grade S
            # Schedule Types:
            #       Lecture 04
            #       Individual Study 16
            # Attributes:
            #       Global Diversity GD
            #       Writing Intensive Requirement WRIT

            #
            (("SENG 1020", "001", 3, 84038, 
             "Data Structures for Software Engineers", 45), 
            #
             ('Brian Dietrick', 'CORE', 'Lecture', 'Standard Letter Grade',
             'Undergraduate', '08/19/2024', '12/11/2024', 'Austin', '00201', 
             ('SENG 1000', 'SENG 1010')),
            #
            ('Monday', 'AM 10:00', 'AM 10:50'),
            ('Wednesday', 'AM 10:00', 'AM 10:50'), 
            ('Friday', 'AM 10:00', 'AM 10:50')),
            # Title:        Data Structures for Software Engineers
            # College:      College of Engr and Technology TC
            # Department:   Computer Science CS
            # Hours:
            #       Credit Hours:3
            #       Lecture: 3
            # Levels:
            #       Undergraduate UG
            # Grading Modes:
            #       Forgiveness F
            #       Standard Letter Grade S
            # Schedule Types:
            #       Lecture 04
            # Attributes:
            
            #
            ((("SECS 1000", "001", 3, 82223,
             "Introduction to Security Studies", 45), 
            #
             ('Alethia Cook', 'SOCIAL SCIENCES', 'Lecture', 'Standard Letter Grade',
             'Undergraduate', '08/19/2024', '12/11/2024', 'Brewster', '0C206'),
             (None)),
            #
            (('Monday', 'AM 12:30', 'PM 1:45'),
            ('Wednesday', 'AM 12:30', 'PM 1:45'), 
            ('Friday', 'AM 12:30', 'PM 1:45'))),
            # Title:        Introduction to Security Studies
            # College:      College of Arts and Sciences AS
            # Department:   Political Science PO
            # Hours:
            #       Credit Hours: 3
            #       Lecture:      3
            # Levels:
            #       Undergraduate UG
            # Grading Modes:
            #       Forgiveness F
            #       Standard Letter Grade S
            # Schedule Types:
            #       Lecture 04
            # Attributes:
            #       Social Sciences Requirement SS

            #
            ((("BIOL 1100", "007", 3, 80582,
             "Principles of Biology I", 45),
            #
             ('NATURAL SCIENCE')),
            #
            (('Monday', 'PM 2:00', 'PM 3:00'),
            ('Wednesday', 'PM 2:00', 'PM 3:00'), 
            ('Friday', 'PM 2:00', 'PM 3:00'))),
            
            #
            ((("BIOL 1101", "002", 1, 80586,
             "Principles of Biology Laboratory I", 45),
            # 
             ('NATURAL SCIENCE')),
            #
            (('Monday', 'PM 2:00', 'PM 4:45')))
            ]

            # Grading Modes:
            # =============
            # Forgiveness F
            # Standard Letter Grade S

            # Schedule Types:
            # ==============
            # Lecture 04


def generateCalanderRow():
    
    # var today
    
    def determineFirstRow():
        return True
    
    first_row = determineFirstRow()

    if first_row:
        # Generate Characters #
        # Cell Top
        print('┍', endl='')


def generateCalander():







# ─	━	│	┃	┄	┅	┆	┇	┈	┉	┊	┋	┌	┍	┎	┏
# ┐	┑	┒	┓	└	┕	┖	┗	┘	┙	┚	┛	├	┝	┞	┟
# ┠	┡	┢	┣	┤	┥	┦	┧	┨	┩	┪	┫	┬	┭	┮	┯
# ┰	┱	┲	┳	┴	┵	┶	┷	┸	┹	┺	┻	┼	┽	┾	┿
# ╀	╁	╂	╃	╄	╅	╆	╇	╈	╉	╊	╋	╌	╍	╎	╏
# ═	║	╒	╓	╔	╕	╖	╗	╘	╙	╚	╛	╜	╝	╞	╟
# ╠	╡	╢	╣	╤	╥	╦	╧	╨	╩	╪	╫	╬	╭	╮	╯
# ╰	╱	╲	╳	╴	╵	╶	╷	╸	╹	╺	╻	╼	╽	╾	╿