import firebase_admin
from firebase_admin import auth
from google.cloud import firestore
import random
import csv

default_app = firebase_admin.initialize_app()

NUMBER_OF_USERS = 600
db = firestore.Client()

# accountType
accountTypes = ["student", "mentor"]

# zipCode
zipCodesFile = open("zipCodes.txt", "r")
zipCodes = zipCodesFile.read().split("\n")
zipCodesFile.close()

# zipCodeMedianIncome

# photoURL
photoURLs = ["https://peaklife.in/wp-content/uploads/2019/06/elon-musk-image.jpg",
             "https://observer.com/wp-content/uploads/sites/2/2020/01/elon-musk-twitter-advice.jpg?quality=80&strip",
             "https://i.insider.com/5ddfa893fd9db26b8a4a2df7?width=1100&format=jpeg&auto=webp"]

# firstName
firstNamesFile = open("firstNames.txt", "r")
firstNames = firstNamesFile.read().split("\n")
firstNamesFile.close()

# state
states = ["Alabama", "Alaska", "American Samoa", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
          "Delaware", "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho", "Illinois", "Indiana",
          "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
          "Minor Outlying Islands", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
          "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Northern Mariana Islands", "Ohio",
          "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota",
          "Tennessee", "Texas", "U.S. Virgin Islands", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
          "Wisconsin", "Wyoming"]

# financialLevel
financialLevels = ["belowAverage", "average", "aboveAverage"]

# gender
genders = ["male", "female", "nonBinary", "other"]

# lgbtq
lgbtqs = ["yes", "no"]

# race
races = ["white", "blackAfricanAmerican", "americanIndianAlaskaNative", "asian", "nativeHawaiianPacificIslander"]

# parentsGoToCollege
parentsGoToColleges = ["yes", "no", "partially"]

# schoolYear
schoolYears = ["freshman", "sophomore", "junior", "senior"]

# major
majors = ["humanities", "mathComputerScience", "sciences", "business", "artTheatre"]

# collegeName
collegeNames = ["Columbia", "Stanford", "Carnegie Mellon"]

# highSchoolGPA
highSchoolGPAs = ["twoOrUnder", "betweenTwoAndThree", "betweenThreeAndFour", "fourPlus"]

# testTaken
testTakens = ["sat", "act", "otherNone"]

# testScore
testScores = ["36", "1600"]

# helpMost
helpMosts = ["generalGuidance", "infoCollegeLookFor", "findingSupportSystem", "collegeEntranceTests",
             "applicationEssays"]

# whyYourCollege
whyYourColleges = ["closeToHome", "bigNameSchool", "bestScholarship", "bestReligionCultureFit", "somethingElse"]

# postGradAspirations
postGradAspirationss = ["continuedStudy", "athletics", "relatedIndustry", "earnMoney", "somethingElse"]

# whyYouWantBeCounselor
whyYouWantBeCounselors = ["wishSomethingLikeThisExisted", "canHelpWriteStrongEssays", "scoredWellOnAdmissionsTests",
                            "sociallyEmotionallySupport", "somethingElse"]

# whichStudentType
whichStudentTypes = ["financiallyUnderpriveleged", "lgtbq", "womenInStem", "similarCultureReligion",
                     "similarRacialBackground"]

# whichDegree
whichDegrees = ["aa", "aaForTransfer", "bachelorArtScience", "tradeSchoolDegree", "other"]

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
            display_name=firstName, )
    except:
        print("an exception occurred")
        continue

    data = {
        u"accountType": random.choice(accountTypes),
        u"zipCode": random.choice(zipCodes),
        u"photoURL": random.choice(photoURLs),
        u"firstName": firstName,
        u"state": random.choice(states),
        u"financialLevel": random.choice(financialLevels),
        u"gender": random.choice(genders),
        u"lgbtq": random.choice(lgbtqs),
        u"race": random.choice(races),
        u"parentsGoToCollege": random.choice(parentsGoToColleges),
        u"schoolYear": random.choice(schoolYears),
        u"major": random.choice(majors),
        u"collegeName": random.choice(collegeNames),
        u"highSchoolGPA": random.choice(highSchoolGPAs),
        u"testTaken": random.choice(testTakens),
        u"testScore": random.choice(testScores),
        u"helpMost": random.choice(helpMosts),
        u"whyYourCollege": random.choice(whyYourColleges),
        u"postGradAspirations": random.choice(postGradAspirationss),
        u"whyYouWantBeCounselor": random.choice(whyYouWantBeCounselors),
        u"whichStudentType": random.choice(whichStudentTypes),
        u"whichDegree": random.choice(whichDegrees),
        u"firstLanguage": random.choice(firstLanguages)
    }

    db.collection(u"users").document(user.uid).set(data)

    print("Successfully created new user: {0}".format(user.uid))
