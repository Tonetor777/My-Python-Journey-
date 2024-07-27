import random
capitals = {
    "Algeria": "Algiers", "Angola": "Luanda", "Benin": "Porto-Novo", "Botswana": "Gaborone", "Burkina Faso": "Ouagadougou", "Burundi": "Gitega", "Cabo Verde": "Praia", "Cameroon": "Yaoundé", "Central African Republic": "Bangui", "Chad": "N'Djamena", "Comoros": "Moroni",
    "Democratic Republic of the Congo": "Kinshasa", "Republic of the Congo": "Brazzaville", "Djibouti": "Djibouti", "Egypt": "Cairo", "Equatorial Guinea": "Malabo", "Eritrea": "Asmara", "Eswatini": "Mbabane", "Ethiopia": "Addis Ababa", "Gabon": "Libreville", "Gambia": "Banjul", "Ghana": "Accra", "Guinea": "Conakry", "Guinea-Bissau": "Bissau", "Ivory Coast": "Yamoussoukro", "Kenya": "Nairobi", "Lesotho": "Maseru", "Liberia": "Monrovia", "Libya": "Tripoli", "Madagascar": "Antananarivo", "Malawi": "Lilongwe", "Mali": "Bamako", "Mauritania": "Nouakchott", "Mauritius": "Port Louis", "Morocco": "Rabat",
    "Mozambique": "Maputo", "Namibia": "Windhoek", "Niger": "Niamey",
    "Nigeria": "Abuja", "Rwanda": "Kigali", "São Tomé and Príncipe": "São Tomé", "Senegal": "Dakar",
    "Seychelles": "Victoria", "Sierra Leone": "Freetown", "Somalia": "Mogadishu",
    "South Africa": "Pretoria", "South Sudan": "Juba", "Sudan": "Khartoum", "Tanzania": "Dodoma", "Togo": "Lomé", "Tunisia": "Tunis",
    "Uganda": "Kampala", "Zambia": "Lusaka", "Zimbabwe": "Harare"
}

for quizNum in range(35):
    with open ('Automate-the-boring-stuff/Working-With-Files/African-Countries-Capitals-Quiz/quizes/capitalquiz%s.txt' % (quizNum + 1), 'w') as quizFile:
        with open ('Automate-the-boring-stuff/Working-With-Files/African-Countries-Capitals-Quiz/quizes/capitalquiz_answer%s.txt' % (quizNum + 1), 'w') as answerFile:
            quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
            quizFile.write((' ' * 20 ) + 'State Capitals Quiz (Form %s)' %(quizNum + 1))
            quizFile.write('\n\n')

            states = list(capitals.keys())
            random.shuffle(states)

            for questionNum in range(50):
                correctAnswer = capitals[states[questionNum]]
                wrongAnswers = list(capitals.values())
                del wrongAnswers [wrongAnswers.index(correctAnswer)]
                wrongAnswers = random.sample(wrongAnswers , 3)
                answerOptions = wrongAnswers + [correctAnswer]
                random.shuffle(answerOptions)

                quizFile.write( str(questionNum + 1) + ', What is the capital of ' + states[questionNum] + ' ?\n')

                choices = ['A' , 'B' , 'C' , 'D']
                for choice in range(4):
                    quizFile.write ( '\t' + choices[choice] + ', ' + answerOptions[choice] + '\n')
                quizFile.write('\n')
                answerFile.write('%s. %s\n' % (questionNum + 1 , choices[answerOptions.index(correctAnswer)]))

