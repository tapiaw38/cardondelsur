from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# utilities
from utils.models import CardonModel

# Create your models here.

class User(CardonModel, AbstractUser):
    """ Modelo de usuario.
    hereda del modelo abstracto AbstractUser
    cambiando la autenticacion de usuario por
    el campo email.
    """
    email = models.EmailField(
        'email addres', 
        unique = True,
        error_messages = {
            'unique': 'Ya existe un usuario con este correo electrónico.',
        }
        )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    is_commerce = models.BooleanField(
        'commerce',
        default = False
    )

    is_verfied = models.BooleanField(
        'verified',
        default = True
    )

    def __str__(self):
        """ Retorna el nombre de usuario. """
        return str(self.username)

    def get_short_name(self):
        """ Retorna el primer nombre. """
        return self.username


class City(models.Model):
    '''Modelo de ciudades Ciudades
    registradas'''

    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name
    

class Profile(CardonModel):
    """ Modelo de perfil del usuario. 
    Perfil publico de cada usuario. """

    user = models.OneToOneField(User,related_name="profile", on_delete=models.CASCADE)
    commerce_name = models.CharField(max_length=100, blank=True, null=True) 
    picture = models.ImageField(
        'profile picture', 
        upload_to = 'users/pictures/',
        blank = True,
        null = True,
        )
    phone_regex = RegexValidator(
        regex=r'\d{10,10}$',
        message= "Debes ingresar un número con el siguiente formato: 3837430000. Hasta 10 digitos."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True, null=True)

    city = models.ForeignKey(City, related_name="city", on_delete=models.CASCADE)

    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

    @property
    def my_city(self):
        return str(self.city.name)

class Offers(CardonModel):
    '''Modelo ofertas de los comercios, 
    icluye datos del perdil de los usuarios'''

    user = models.ForeignKey(User, related_name="related_users", on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, related_name='related_profiles', on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to="users/pictures")
    
    def __str__(self):
        return str(self.user)

