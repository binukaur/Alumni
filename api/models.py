from django.db import models

# Create your models here.

class AlumniInfo(models.Model):
    AlumniID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50, null=True, blank=True)  # Optional field
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    GradYear = models.IntegerField(null=True, blank=True)
    DateOfBirth = models.DateField(null=True, blank=True)
    CurrentCity = models.CharField(max_length=50, null=True, blank=True)

    @property
    def FullName(self):
        return f"{self.FirstName} {self.MiddleName or ''} {self.LastName}"

    def __str__(self):
        return self.FullName


class AlumniPhone(models.Model):
    Alumni = models.ForeignKey(AlumniInfo, on_delete=models.CASCADE)  
    CountryCode = models.CharField(max_length=5)
    MobileNumber = models.CharField(max_length=10)

    class Meta:
        unique_together = ('Alumni', 'MobileNumber')    

    def __str__(self):
        return f"{self.CountryCode} {self.MobileNumber}"


class AcademicHistory(models.Model):
    Alumni = models.ForeignKey(AlumniInfo, on_delete=models.CASCADE)    
    Degree_Name = models.CharField(max_length=100)
    CGPA = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    StartYear = models.IntegerField(null=True, blank=True)
    EndYear = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('Alumni', 'Degree_Name')      

    def __str__(self):
        return f"{self.Degree_Name} ({self.StartYear}-{self.EndYear})"


class Achievements(models.Model):
    Alumni = models.ForeignKey(AlumniInfo, on_delete=models.CASCADE)     
    AwardTitle = models.CharField(max_length=100)
    Description = models.TextField()
    DateAwarded = models.DateField()

    def __str__(self):
        return self.AwardTitle


class ProfessionalHistory(models.Model):
    Alumni = models.ForeignKey(AlumniInfo, on_delete=models.CASCADE)    
    CompanyName = models.CharField(max_length=100)
    JobTitle = models.CharField(max_length=100)
    StartDate = models.DateField()
    EndDate = models.DateField(null=True, blank=True)
    Skills = models.TextField()

    def __str__(self):
        return f"{self.JobTitle} at {self.CompanyName}"


class SocialMedia(models.Model):
    Alumni = models.ForeignKey(AlumniInfo, on_delete=models.CASCADE)    
    Platform = models.CharField(max_length=50)
    Username = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Platform}: {self.Username}"
