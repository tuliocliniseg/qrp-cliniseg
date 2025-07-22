from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings  # ← IMPORTANTE!

# ─── Modelo Personalizado de Usuário ──────────────────────────────────────
class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome_completo, cargo, password=None):
        if not email:
            raise ValueError('O usuário deve ter um endereço de e-mail.')
        email = self.normalize_email(email)
        user = self.model(email=email, nome_completo=nome_completo, cargo=cargo)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome_completo, cargo, password):
        user = self.create_user(email, nome_completo, cargo, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome_completo = models.CharField(max_length=150)
    cargo = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_completo', 'cargo']

    def __str__(self):
        return self.nome_completo

# ─── Log de Ações Administrativas ─────────────────────────────────────────
class LogUsuario(models.Model):
    ACOES = [
        ('editou', 'Editou'),
        ('excluiu', 'Excluiu'),
    ]

    executado_por = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='acoes_executadas', on_delete=models.CASCADE)
    usuario_alvo = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='foi_alvo', on_delete=models.CASCADE)
    acao = models.CharField(max_length=10, choices=ACOES)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.executado_por.email} {self.acao} {self.usuario_alvo.email} em {self.data_hora:%d/%m/%Y %H:%M}"
