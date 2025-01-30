from django.db import models

# Create your models here.
class Signup(models.Model):
    uname=models.CharField(max_length=100)
    uemail = models.EmailField()
    ucontact = models.CharField(max_length=15)
    upassword=models.CharField(max_length=10)
 
    class Meta:
            db_table = 'signup'

class Team(models.Model):
    team_id = models.CharField(max_length=10, primary_key=True)
    team_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'team'

    def __str__(self):
        return self.team_name

class Coordinator(models.Model):
    coord_name = models.CharField(max_length=20)
    c_email = models.EmailField(unique=True,primary_key=True)
    phone_no = models.BigIntegerField()
    
    class Meta:
        db_table = 'coordinator'
        
    def __str__(self):
        return self.coord_name
    
class Mentor(models.Model):
    m_email = models.EmailField(primary_key=True)
    phone_no = models.BigIntegerField()
    mentor_name = models.CharField(max_length=20)
    c_email = models.ForeignKey(Coordinator, on_delete=models.CASCADE)

    class Meta:
        db_table = 'mentor'
        
    def __str__(self):
        return self.mentor_name
    
class TeamMember(models.Model):
    stu_id = models.CharField(max_length=30, primary_key=True)
    member_name = models.CharField(max_length=30)
    student_class = models.CharField(max_length=20)  # Changed "class" to avoid conflicts with Python keyword
    branch = models.CharField(max_length=30)
    semester = models.IntegerField()
    stu_rollno = models.IntegerField()
    phone_no = models.IntegerField()
    email = models.CharField(max_length=50)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='team_id')  # Foreign key reference to Team

    class Meta:
        db_table = 'team_member'
    
    def __str__(self):
        return self.member_name



# Group Details Model
class GroupDetails(models.Model):
    group_id = models.CharField(max_length=10, primary_key=True)
    mentor_name = models.CharField(max_length=20)
    project_name = models.CharField(max_length=20)
    m_email = models.ForeignKey(Mentor, on_delete=models.CASCADE)   # Mentor Email (Foreign Key Reference)
    c_email = models.ForeignKey(Coordinator, on_delete=models.CASCADE)  # Client Email (Foreign Key Reference)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='team_id')     # Team ID (Foreign Key Reference)
    
    class Meta:
        db_table = 'group_details'

    def __str__(self):
        return self.group_id


# Marks Model
class Marks(models.Model):
    stu_rollno = models.CharField(max_length=20, primary_key=True)
    marks = models.IntegerField()
    member_name = models.CharField(max_length=30)
    stu_id = models.CharField(max_length=30)    # Student ID (Foreign Key Reference)
    c_email = models.ForeignKey(Coordinator, on_delete=models.CASCADE) # Client Email (Foreign Key Reference)
    m_email = models.ForeignKey(Mentor, on_delete=models.CASCADE)  # Mentor Email (Foreign Key Reference)

    class Meta:
        db_table = 'marks'
    def __str__(self):
        return self.stu_rollno

# Project Details Model
class ProjectDetails(models.Model):
    project_id = models.IntegerField(primary_key=True)
    description = models.TextField(max_length=200)
    project_name = models.CharField(max_length=30)
    approval = models.CharField(max_length=10)
    tech_stack = models.TextField(max_length=100)
    team_id = models.CharField(max_length=10)   # Team ID (Foreign Key Reference)
    m_email = models.ForeignKey(Mentor, on_delete=models.CASCADE)  # Mentor Email (Foreign Key Reference)
    c_email = models.ForeignKey(Coordinator, on_delete=models.CASCADE)  # Client Email (Foreign Key Reference)

    class Meta:
        db_table = 'project_details'
    def __str__(self):
        return self.project_name



class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    doc_title = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    upload_file = models.BinaryField()
    start_date = models.DateField()
    end_date = models.DateField()
    m_email = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'task'
        
    def __str__(self):
        return self.doc_title