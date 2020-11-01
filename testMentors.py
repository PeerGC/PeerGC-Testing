import firebase_admin
from firebase_admin import auth
from google.cloud import firestore
import random
import csv

default_app = firebase_admin.initialize_app()

NUMBER_OF_USERS = 600
db = firestore.Client()

# Account_Type
accountTypes = ["student", "mentor"]

# ZIP_Code
zipCodesFile = open("zipCodes.txt", "r")
zipCodes = zipCodesFile.read().split("\n")
zipCodesFile.close()

# Photo_URL
photoURLs = ["https://images.unsplash.com/photo-1518806118471-f28b20a1d79d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80"]

# First_Name
firstNamesFile = open("firstNames.txt", "r")
firstNames = firstNamesFile.read().split("\n")
firstNamesFile.close()

# State
states = ["Alabama", "Alaska", "American Samoa", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
          "Delaware", "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho", "Illinois", "Indiana",
          "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
          "Minor Outlying Islands", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
          "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Northern Mariana Islands", "Ohio",
          "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota",
          "Tennessee", "Texas", "U.S. Virgin Islands", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
          "Wisconsin", "Wyoming"]

# Financial_Level
financialLevels = ["below_average", "average", "above_average"]

# Gender
genders = ["male", "female", "non_binary", "other"]

# LGBTQ
lgbtqs = ["yes", "no"]

# race
races = ["white", "black_or_african_american", "american_indian_or_alaska_native", "asian", "native_hawaiian_or_pacific_islander"]

# Did_Either_Of_Your_Parents_Attend_Higher_Education
parentsGoToColleges = ["yes", "no", "partially_but_with_no_degree"]

# What_Year_Of_College
schoolYears = ["freshman", "sophomore", "junior", "senior"]

# What_Field_Of_Study_Are_You_Currently_Pursuing
majors = ["humanities", "math_or_computer_science", "sciences", "business", "art_or_theatre"]

# What_College_Do_You_Attend
collegeNames = ["Columbia", "Stanford", "Carnegie Mellon"]

# What_Was_Your_High_School_GPA
highSchoolGPAs = ["two_or_under", "between_two_and_three", "between_three_and_four", "four_or_higher"]

# Which_Test_Did_You_Use_For_Your_College_Application
testTakens = ["sat", "act", "other_or_none"]

# Test_Score
testScores = ["36", "1600"]

# Where_Can_You_Help_A_Student_Most
helpMosts = ["general_guidance_or_keeping_on_track", "info_on_what_colleges_look_for", "finding_a_support_system_in_college", "college_entrance_tests","application_essays"]

# Why_Did_You_Choose_The_College_You_Are_In
whyYourColleges = ["close_to_home", "big_name_school", "best_scholarship", "best_fit_with_your_religion_or_culture", "something_else"]

# What_Are_Your_Post_Grad_Aspirations
postGradAspirationss = ["continued_study", "athletics", "work_in_an_industry_related_to_your_major", "earn_money_with_your_degree", "something_else"]

# Why_Do_You_Want_To_Be_A_Peer_Guidance_Counselor
whyYouWantBeCounselors = ["you_wish_something_like_this_existed_for_you", "you_can_help_write_strong_essays", "you_scored_well_on_admissions_tests",
                            "you_can_socially_or_emotionally_support_mentees", "something_else"]

# What_Kind_Of_Student_Would_You_Be_Most_Excited_To_Mentor
whichStudentTypes = ["financially_underprivileged", "lgtbq", "women_in_stem", "similar_cultural_or_religious_background_as_you",
                     "similar_racial_background_as_you"]

# What_Kind_Of_Degree_Are_You_Currently_Pursuing
whichDegrees = ["aa", "aa_for_transfer", "bachelor_of_art_or_science", "trade_school_degree", "other"]

# firstLanguage
firstLanguages = ["English", "Spanish", "Russian"]

for i in range(NUMBER_OF_USERS):
    firstName = random.choice(firstNames)
    email = firstName + "@example.com"
    password = email.lower()

    try:
        user = auth.create_user(
            email=email,
            password=password,
            display_name=firstName,
            photo_url=random.choice(photoURLs))
    except:
        print("an exception occurred")
        continue

    data = {
        u"Account_Type": random.choice(accountTypes),
        u"ZIP_Code": random.choice(zipCodes),
        u"Photo_URL": random.choice(photoURLs),
        u"First_Name": firstName,
        u"State": random.choice(states),
        u"Financial_Level": random.choice(financialLevels),
        u"Gender": random.choice(genders),
        u"LGBTQ": random.choice(lgbtqs),
        u"Race": random.choice(races),
        u"Did_Either_Of_Your_Parents_Attend_Higher_Education": random.choice(parentsGoToColleges),
        u"What_Year_Of_College": random.choice(schoolYears),
        u"What_Field_Of_Study_Are_You_Currently_Pursuing": random.choice(majors),
        u"What_College_Do_You_Attend": random.choice(collegeNames),
        u"What_Was_Your_High_School_GPA": random.choice(highSchoolGPAs),
        u"Which_Test_Did_You_Use_For_Your_College_Application": random.choice(testTakens),
        u"Test_Score": random.choice(testScores),
        u"Where_Can_You_Help_A_Student_Most": random.choice(helpMosts),
        u"Why_Did_You_Choose_The_College_You_Are_In": random.choice(whyYourColleges),
        u"What_Are_Your_Post_Grad_Aspirations": random.choice(postGradAspirationss),
        u"Why_Do_You_Want_To_Be_A_Peer_Guidance_Counselor": random.choice(whyYouWantBeCounselors),
        u"What_Kind_Of_Student_Would_You_Be_Most_Excited_To_Mentor": random.choice(whichStudentTypes),
        u"What_Kind_Of_Degree_Are_You_Currently_Pursuing": random.choice(whichDegrees),
        u"First_Language": random.choice(firstLanguages)
    }

    db.collection(u"Users").document(user.uid).set(data)

    print("Successfully created new user: {0}".format(user.uid))
