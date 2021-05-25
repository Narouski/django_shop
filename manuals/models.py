from django.db import models


class Annotation(models.Model):
    annotation = models.TextField(
        verbose_name="Аннотация"
    )

    def __str__(self) -> str:
        return f"Аннотация {self.annotation}"

    class Meta:
        verbose_name = "Аннотацию"
        verbose_name_plural = "Аннотации"


class Series(models.Model):
    count_series = models.IntegerField(
        verbose_name="Количество серий"
    )

    def __str__(self) -> str:
        return f"Серия {self.count_series}"

    class Meta:
        verbose_name = "Серию"
        verbose_name_plural = "Серии"


class Publishers(models.Model):
    publisher = models.CharField(
        verbose_name="Издательская компания",
        max_length=100
    )

    def __str__(self) -> str:
        return f"Издатель {self.publisher}"

    class Meta:
        verbose_name = "Издателя"
        verbose_name_plural = "Издатели"


class Genres(models.Model):
    genre = models.CharField(
        verbose_name="Жанр",
        max_length=30
    )

    def __str__(self) -> str:
        return f"Жанр {self.genre}"

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Authors(models.Model):
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=30
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=30
    )
    biography = models.TextField(
        verbose_name="Биография",
        blank=True,
        null=True
    )
    genre_author = models.ForeignKey(
        Genres,
        on_delete=models.PROTECT,
        related_name="genres"
    )
    series_author = models.ForeignKey(
        Series,
        on_delete=models.PROTECT,
        related_name="series"
    )
    annotation_author = models.ForeignKey(
        Annotation,
        on_delete=models.PROTECT,
        related_name="annotations"
    )
    publisher_author = models.ForeignKey(
        Publishers,
        on_delete=models.PROTECT,
        related_name="publishers"
    )
    created = models.DateTimeField(
        verbose_name="Дата регистрации Автора",
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name="Дата последнего редактирования",
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self) -> str:
        return f"Автор {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Автора"
        verbose_name_plural = "Авторы"
