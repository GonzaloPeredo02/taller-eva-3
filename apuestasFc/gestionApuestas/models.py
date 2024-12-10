from django.db import models
from django.contrib.auth.models import User

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.pais})"

class Juego(models.Model):
    equipo1 = models.ForeignKey(Equipo, related_name='equipo1', on_delete=models.CASCADE)
    equipo2 = models.ForeignKey(Equipo, related_name='equipo2', on_delete=models.CASCADE)
    ganador = models.ForeignKey(Equipo, related_name='ganador', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.equipo1} vs {self.equipo2}"

class Apuesta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    equipo_apostado = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    resultado = models.BooleanField(default=False)
    fecha_apuesta = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'juego')

    def __str__(self):
        return f"{self.usuario.username} - {self.juego} - {self.equipo_apostado}"
