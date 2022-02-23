# django-creating-custom-user-model
I don't want a classic user model. (AbstractUser)
* Created a new class called CustomUser that subclasses AbstractUser
* Removed the username field
* Made the email field required and unique
* Set the USERNAME_FIELD -- which defines the unique identifier for the User model -- to email
* Specified that all objects for the class come from the CustomUserManager
![custom-user-model](https://user-images.githubusercontent.com/85527587/155242776-88998a3b-47be-46e7-9639-73384cfdb47a.png)
