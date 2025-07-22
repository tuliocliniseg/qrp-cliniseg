import os
from pathlib import Path
from decouple import config
from django.contrib.messages import constants as messages

# ─── Diretório Base ────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ─── Chave Secreta ─────────────────────────────────────────────────
SECRET_KEY = config('SECRET_KEY', default='unsafe-key')  # Busca da variável de ambiente ou valor padrão inseguro para dev

# ─── Modo Debug ────────────────────────────────────────────────────
DEBUG = config('DEBUG', default=False, cast=bool)  # Configuração booleana para debug

# ─── Hosts Permitidos ──────────────────────────────────────────────
ALLOWED_HOSTS = ['*']  # Em produção, especifique domínios reais

# ─── Aplicações Registradas ────────────────────────────────────────
INSTALLED_APPS = [
    # Apps Django padrão
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps do projeto
    'usuarios',
    'empresas',
    'formulario',
    'relatorios',
    'painel',
    'respostas',

    # Biblioteca para manipulação de widgets em templates
    'widget_tweaks',
]

# ─── Middlewares ───────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Proteção CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Proteção contra clickjacking
]

# ─── URL Principal ─────────────────────────────────────────────────
ROOT_URLCONF = 'qrp_cliniseg.urls'

# ...

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Diretório global para templates
        'APP_DIRS': True,  # Busca automática de templates em apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Necessário para acessar request no template
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'painel.context_processors.empresa_slug',  # <<< Aqui!
            ],
        },
    },
]

# ─── WSGI ───────────────────────────────────────────────────────────
WSGI_APPLICATION = 'qrp_cliniseg.wsgi.application'

# ─── Banco de Dados PostgreSQL ─────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),       # Nome do banco (env)
        'USER': config('DB_USER'),       # Usuário do banco (env)
        'PASSWORD': config('DB_PASSWORD'),  # Senha do banco (env)
        'HOST': config('DB_HOST'),       # Host do banco (env)
        'PORT': config('DB_PORT'),       # Porta do banco (env)
    }
}

# ─── Validação de Senhas ───────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8,}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ─── Internacionalização ───────────────────────────────────────────
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ─── Arquivos Estáticos ────────────────────────────────────────────
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # Pasta para arquivos estáticos no desenvolvimento
STATIC_ROOT = BASE_DIR / "staticfiles"   # Pasta para coletar arquivos estáticos na produção

# ─── Arquivos de Mídia ─────────────────────────────────────────────
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# ─── Mensagens Bootstrap (para o framework de mensagens) ───────────
MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# ─── Configurações de autenticação ─────────────────────────────────
AUTH_USER_MODEL = 'usuarios.Usuario'  # Modelo customizado de usuário
LOGIN_URL = '/'                       # URL para login
LOGIN_REDIRECT_URL = '/painel/inicio/'  # Após login, redireciona para o painel
LOGOUT_REDIRECT_URL = '/'            # Após logout, redireciona para home/login

# ─── Segurança Extra (opcional) ────────────────────────────────────
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# ─── Configuração padrão para campos automáticos de ID ────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
