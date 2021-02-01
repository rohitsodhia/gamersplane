# Generated by Django 3.1 on 2021-01-31 22:52

from django.db import migrations, models
import tokens.models.token


class Migration(migrations.Migration):

    dependencies = [("tokens", "0002_accountactivation_passwordreset")]

    operations = [
        migrations.AlterField(
            model_name="token",
            name="token",
            field=models.CharField(
                default=tokens.models.token.Token.generate_token, max_length=36
            ),
        )
    ]