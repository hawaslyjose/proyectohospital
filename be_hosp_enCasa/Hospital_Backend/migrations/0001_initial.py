# Generated by Django 4.1.1 on 2022-10-04 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Medico",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("especialidad", models.CharField(max_length=45)),
                ("rol", models.CharField(max_length=35, verbose_name="Rol")),
                ("licencia", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Paciente",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "medico",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Hospital_Backend.medico",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "username",
                    models.CharField(
                        max_length=15, unique=True, verbose_name="Username"
                    ),
                ),
                ("password", models.CharField(max_length=256, verbose_name="Password")),
                ("perfil", models.CharField(max_length=30, verbose_name="Perfil")),
                ("nombre", models.CharField(max_length=35, verbose_name="Nombre")),
                (
                    "apellidos",
                    models.CharField(max_length=35, verbose_name="Apellidos"),
                ),
                ("telefono", models.CharField(max_length=35, verbose_name="Telefono")),
                ("genero", models.CharField(max_length=35, verbose_name="Genero")),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Signos_vitales",
            fields=[
                ("id_sigvitales", models.AutoField(primary_key=True, serialize=False)),
                ("oximetria", models.IntegerField(default=0)),
                ("frec_cardiaca", models.IntegerField(default=0)),
                ("frec_respiratoria", models.IntegerField(default=0)),
                ("temperatura", models.IntegerField(default=0)),
                ("glicemias", models.IntegerField(default=0)),
                ("presion", models.CharField(max_length=7)),
                ("fecha_registro", models.DateTimeField()),
                (
                    "id_paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sig_vitales",
                        to="Hospital_Backend.paciente",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="paciente",
            name="usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="medico",
            name="usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="Historia_clinica",
            fields=[
                ("id_histClinica", models.AutoField(primary_key=True, serialize=False)),
                (
                    "sugerencias",
                    models.CharField(max_length=250, verbose_name="Sugerencias"),
                ),
                (
                    "diagnostico",
                    models.CharField(max_length=250, verbose_name="Diagnostico"),
                ),
                ("entorno", models.CharField(max_length=250, verbose_name="Entorno")),
                ("fecha_sugerencia", models.DateField()),
                (
                    "descipcion",
                    models.CharField(max_length=250, verbose_name="Descripcion"),
                ),
                (
                    "id_paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hist_clinica",
                        to="Hospital_Backend.paciente",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Familiar",
            fields=[
                ("id_familiar", models.AutoField(primary_key=True, serialize=False)),
                (
                    "parentesco",
                    models.CharField(max_length=35, verbose_name="Parentesco"),
                ),
                ("correo", models.EmailField(max_length=100, verbose_name="Correo")),
                (
                    "id_paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="familiar",
                        to="Hospital_Backend.paciente",
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="familiar",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
