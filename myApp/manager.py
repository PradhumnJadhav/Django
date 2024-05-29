from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra):
        email=self.normalize_email(email)
        if not email :
         
         raise ValueError("email is Required.")
        user=self.model(email=email,**extra)
         
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self,email,password,**extra):
       extra.setdefault('is_staff',True)
       extra.setdefault('is_superuser',True)
       extra.setdefault('is_active',True)

       return self.create_user(email,password,**extra)

        
    
    
