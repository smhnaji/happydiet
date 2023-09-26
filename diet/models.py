from django.db import models


class DietPlan(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    diet_count = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class DietPlanSubscription(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    diet_package = models.ForeignKey('DietPlan', on_delete=models.CASCADE)
    usage_date = models.DateTimeField(auto_now_add=True)
    prescribed_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user} used {self.diet_package} on {self.usage_date}"


class DietOrder(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    diet_package_usage = models.ForeignKey('DietPlanSubscription', on_delete=models.CASCADE)
    inquiry_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('answered', 'Answered'), ('cancelled', 'Cancelled')])

    def __str__(self):
        return f"{self.user} inquired about {self.diet_package_usage} on {self.inquiry_date}"


class Diet(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    diet_inquiry = models.OneToOneField('DietOrder', on_delete=models.CASCADE)
    doctor = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='responses')
    response_date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return f"{self.doctor} responded to {self.diet_inquiry} on {self.response_date}"