from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
    
GENDER = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other')
)
LEVEL_OF_STUDY = (
        ('UG', 'Undergraduate'),
        ('GA', 'Graduate')
)

YEAR = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('MS', 'Graduate'),
        ('PHD', 'PhD')
)

COLLEGE = (
        ('EDUC', 'College of Education'),
        ('ENG', 'College of Engineering'),
        ('CHFA', 'College of Humanities and Fine Arts'),
        ('CICS', 'College of Information and Computer Sciences'),
        ('CNS', 'College of Natural Sciences'),
        ('EMCON', 'Elaine Marieb College of Nursing'),
        ('CSBS', 'College of Social and Behavioral Sciences'),
        ('ISOM', 'Isenberg School of Management'),
        ('SPHHS', 'School of Public Health & Health Sciences'),
        ('SSA', 'Stockbridge School of Agriculture'),
        ('OTHER', 'Other')
)

PROGRAM = (
        ('ACC', 'Accounting'),
        ('AAS', 'Afro-American Studies'),
        ('AI', 'Alternative Investments'),
        ('ASAB', 'Animal Science, Animal Biotechnology, and Biomedical Sciences'),
        ('ANTH', 'Anthropology'),
        ('ACFM', 'Arboriculture and Community Forest Management'),
        ('ARCH', 'Architecture'),
        ('ART', 'Art'),
        ('AED', 'Art Education'),
        ('ARTH', 'Art History'),
        ('ASTR', 'Astronomy'),
        ('BMB', 'Biochemistry and Molecular Biology'),
        ('BIO', 'Biology'),
        ('BME', 'Biomedical Engineering'),
        ('BST', 'Biostatistics'),
        ('BCT', 'Building and Construction Technology'),
        ('BA', 'Business Analytics'),
        ('CHE', 'Chemical Engineering'),
        ('CHEM', 'Chemistry'),
        ('CHN', 'Chinese Language and Literature'),
        ('CE', 'Civil Engineering'),
        ('CLAS', 'Classics'),
        ('COMM', 'Communication'),
        ('CDIS', 'Communication Disorders'),
        ('CHE', 'Community Health Education'),
        ('COLIT', 'Comparative Literature'),
        ('CS', 'Computer Science'),
        ('DANCE', 'Dance'),
        ('DACS', 'Data Analytics and Computational Social Science'),
        ('ECON', 'Economics'),
        ('EDUC', 'Education'),
        ('ECE', 'Electrical and Computer Engineering'),
        ('EM', 'Engineering Management'),
        ('ENG', 'English'),
        ('EVCON', 'Environmental Conservation'),
        ('EVE', 'Environmental Engineering'),
        ('EHS', 'Environmental Health Sciences'),
        ('ENVS', 'Environmental Science'),
        ('EPID', 'Epidemiology'),
        ('FILM', 'Film Studies through BDIC'),
        ('FIN', 'Finance'),
        ('FSCI', 'Food Science'),
        ('FREN', 'French & Francophone Studies'),
        ('GEOG', 'Geography'),
        ('GEOL', 'Geology'),
        ('GEOSCI', 'Geosciences'),
        ('GER', 'German and Scandinavian Studies'),
        ('HPM', 'Health Policy and Management'),
        ('HLL', 'Hispanic Literatures and Linguistics'),
        ('HIST', 'History'),
        ('HAA', 'History of Art and Architecture'),
        ('HORT', 'Horticultural Science'),
        ('HTM', 'Hospitality and Tourism Management'),
        ('IE', 'Industrial Engineering'),
        ('INFO', 'Informatics'),
        ('ITAL', 'Italian Studies'),
        ('JPN', 'Japanese Language & Literature'),
        ('JOUR', 'Journalism'),
        ('JUDS', 'Judaic Studies'),
        ('KIN', 'Kinesiology'),
        ('LS', 'Labor Studies'),
        ('LARCH', 'Landscape Architecture'),
        ('LCON', 'Landscape Contracting'),
        ('LS', 'Legal Studies'),
        ('LING', 'Linguistics'),
        ('MGMT', 'Management'),
        ('MKTG', 'Marketing'),
        ('MATH', 'Mathematics'),
        ('ME', 'Mechanical Engineering'),
        ('MICRO', 'Microbiology'),
        ('MES', 'Middle Eastern Studies'),
        ('MUS', 'Music'),
        ('NRC', 'Natural Resource Conservation'),
        ('NB', 'Neuroscience and Behavior'),
        ('NURS', 'Nursing'),
        ('NUTR', 'Nutrition'),
        ('OIM', 'Operations and Information Management'),
        ('PHIL', 'Philosophy'),
        ('PHYS', 'Physics'),
        ('PBIO', 'Plant Biology'),
        ('PSS', 'Plant and Soil Science'),
        ('POL', 'Political Science'),
        ('PSE', 'Polymer Science and Engineering'),
        ('PORT', 'Portuguese'),
        ('PMED', 'Pre-Medical, Pre-Health'),
        ('PVT', 'Pre-Veterinary'),
        ('PSYCH', 'Psychology'),
        ('PHS', 'Public Health Sciences'),
        ('PPA', 'Public Policy and Administration'),
        ('RP', 'Regional Planning'),
        ('RECON', 'Resource Economics'),
        ('REES', 'Russian and East European Studies'),
        ('STPEC', 'Social Thought and Political Economy'),
        ('SOC', 'Sociology'),
        ('SPAN', 'Spanish'),
        ('SM', 'Sport Management'),
        ('SFF', 'Sustainable Food and Farming'),
        ('SH', 'Sustainable Horticulture'),
        ('SSCI', 'Sustainability Science'),
        ('THEA', 'Theater'),
        ('TM', 'Turfgrass Management'),
        ('VETECH', 'Veterinary Technology'),
        ('WGSS', 'Women, Gender, Sexuality Studies')
)

SLEEP_HABIT = (
        ('EB', 'Early Bird'),
        ('AVG', 'Average'),
        ('NO', 'Night Owl')
)

CLEANLINESS = (
        ('CLEAN', 'Clean'),
        ('AVG', 'Average'),
        ('DIRTY', 'Dirty')
)

SOCIAL_HABIT = (
        ('NG', 'No Overnight Guests'),
        ('YG', 'Overnight Guests')
)

DURATION = (
        ('ONE', 'One Season'),
        ('TWO', 'Two Seasons'),
        ('THREE', 'Three Seasons'),
        ('FOUR', 'Four Seaons')
)

START_SEASON = (
        ('FALL', 'Fall'),
        ('WINTER', 'Winter'),
        ('SPRING', 'Spring'),
        ('SUMMER', 'Summer')
)

HOUSING = (
        ('HAVE', 'Have a place'),
        ('NEED', 'Need a place')
)

class Profile(models.Model):
        userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        phno = models.CharField(max_length=10)
        profile_picture = models.ImageField(upload_to='profile_pictures/')
        gender = models.CharField(max_length=25, choices=GENDER, default=GENDER[0][0])
        level_of_study = models.CharField(max_length=25, choices=LEVEL_OF_STUDY, default=LEVEL_OF_STUDY[0][0])
        year = models.CharField(max_length=25, choices=YEAR, default=YEAR[0][0])
        college = models.CharField(max_length=35, choices=COLLEGE, default=COLLEGE[0][0])
        program = models.CharField(max_length=65, choices=PROGRAM, default=PROGRAM[0][0])
        sleep_habit = models.CharField(max_length=25, choices=SLEEP_HABIT, default=SLEEP_HABIT[0][0])
        cleanliness = models.CharField(max_length=25, choices=CLEANLINESS, default=CLEANLINESS[0][0])
        social_habit = models.CharField(max_length=25, choices=SOCIAL_HABIT, default=SOCIAL_HABIT[0][0])
        duration = models.CharField(max_length=25, choices=DURATION, default=DURATION[0][0])
        start_season = models.CharField(max_length=25, choices=START_SEASON, default=START_SEASON[0][0])
        housing = models.CharField(max_length=25, choices=HOUSING, default=HOUSING[0][0])
                
        def __str__(self):
                return self.userid.username


STATUS = (
        ('pending', 'PENDING'),
        ('accepted', 'ACCEPTED'),
        ('ignored', 'IGNORED')
)

class Request(models.Model):
        requesterid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='requesterid')
        recipientid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipientid')
        staus = models.CharField(max_length=25, choices=STATUS, default=STATUS[0][0])
        date_sent = models.DateField(default=timezone.now)

        def __str__(self):
                return f"requester: {self.requesterid}, recipient: {self.requesterid}, status: {self.status}"